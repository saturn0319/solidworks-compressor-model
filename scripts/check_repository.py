#!/usr/bin/env python3
"""Validate the published CAD snapshot using only the Python standard library.

This checks archive integrity, not CAD geometry, mates or manufacturability.
Run from any directory: python /path/to/repository/scripts/check_repository.py
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
CATALOG_EXTENSIONS = {".sldprt", ".sldasm", ".pdf", ".png", ".step", ".stp", ".x_t", ".x_b", ".dwg", ".slddrw"}
LOCAL_ONLY = {".git", "tmp", "dist", "output", ".venv", "venv", ".codex", ".agents"}
REQUIRED = (
    "README.md", "LICENSE", "THIRD_PARTY_NOTICES.md", "CONTRIBUTING.md",
    ".gitignore", ".gitattributes", ".github/workflows/validate.yml",
    "docs/README.en.md", "docs/CAD_GUIDE.md", "docs/PARTS.md",
    "docs/REFERENCES.md", "docs/VALIDATION.md", "docs/PUBLISHING.md",
    "docs/images/assembly-isometric.png", "docs/assembly-components.csv",
)


def repository_path(value: str) -> Path:
    relative = PurePosixPath(value)
    if not value or "\\" in value or relative.is_absolute() or ".." in relative.parts:
        raise ValueError(f"Unsafe repository path: {value!r}")
    result = (ROOT / relative).resolve()
    if not result.is_relative_to(ROOT):
        raise ValueError(f"Path leaves repository: {value!r}")
    return result


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate() -> list[str]:
    errors: list[str] = []
    for name in REQUIRED:
        if not repository_path(name).is_file():
            errors.append(f"Required file missing: {name}")

    manifest = json.loads((ROOT / "docs/model-manifest.json").read_text(encoding="utf-8"))
    if manifest.get("schema_version") != 1:
        raise ValueError("Unsupported manifest schema")
    entries = manifest["files"]
    names: set[str] = set()
    for entry in entries:
        name = entry["path"]
        if name in names:
            errors.append(f"Duplicate manifest entry: {name}")
        names.add(name)
        path = repository_path(name)
        if not re.fullmatch(r"[0-9a-f]{64}", entry["sha256"]):
            errors.append(f"Invalid SHA-256 value: {name}")
        if not path.is_file():
            errors.append(f"Catalog file missing: {name}")
            continue
        if path.stat().st_size != entry["size_bytes"]:
            errors.append(f"File size changed: {name}")
        if sha256(path) != entry["sha256"]:
            errors.append(f"SHA-256 mismatch: {name}")

    actual = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file()
        and not any(part in LOCAL_ONLY for part in path.relative_to(ROOT).parts)
        and not path.name.startswith("~$")
        and path.suffix.lower() in CATALOG_EXTENSIONS
    }
    for name in sorted(actual - names):
        errors.append(f"Asset absent from manifest: {name}")
    for name in sorted(names - actual):
        errors.append(f"Catalog asset not found in publishable files: {name}")

    counts = manifest["expected_counts"]
    parts = {name for name in names if Path(name).suffix.lower() == ".sldprt"}
    assemblies = {name for name in names if Path(name).suffix.lower() == ".sldasm"}
    pdfs = {name for name in names if Path(name).suffix.lower() == ".pdf"}
    for label, observed in (("part_files", len(parts)), ("assembly_files", len(assemblies)), ("reference_pdfs", len(pdfs))):
        if observed != counts[label]:
            errors.append(f"Unexpected {label}: {observed}, expected {counts[label]}")
    if manifest["primary_assembly"] not in assemblies:
        errors.append("Primary assembly is absent from the catalog")
    dependencies = manifest["assembly_dependencies"]
    if len(dependencies) != len(set(dependencies)) or set(dependencies) != parts:
        errors.append("Assembly dependency inventory differs from the part inventory")

    component_path = ROOT / "docs/assembly-components.csv"
    if component_path.is_file():
        with component_path.open(encoding="utf-8-sig", newline="") as stream:
            components = list(csv.DictReader(stream))
        if len(components) != counts["component_instances"]:
            errors.append(f"Unexpected component instance count: {len(components)}")
        instance_names: set[str] = set()
        used_files: set[str] = set()
        for row in components:
            if row["instance"] in instance_names:
                errors.append(f"Duplicate component instance: {row['instance']}")
            instance_names.add(row["instance"])
            used_files.add(row["file"])
            if row["file"] not in parts:
                errors.append(f"Component references uncatalogued part: {row['file']}")
            if not row["configuration"]:
                errors.append(f"Missing component configuration: {row['instance']}")
            if row["state"] != "fully_resolved":
                errors.append(f"Component not fully resolved in recorded snapshot: {row['instance']}")
        if used_files != set(dependencies):
            errors.append("Component file inventory differs from assembly dependencies")

    markdown_files = [ROOT / "README.md", ROOT / "CONTRIBUTING.md", ROOT / "THIRD_PARTY_NOTICES.md"]
    markdown_files += list((ROOT / "docs").rglob("*.md"))
    markdown_files += list((ROOT / ".github").rglob("*.md"))
    for path in markdown_files:
        if not path.is_file():
            continue
        for match in re.finditer(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", path.read_text(encoding="utf-8")):
            target = match.group(1).strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            linked = (path.parent / unquote(parsed.path)).resolve()
            if not linked.is_relative_to(ROOT) or not linked.exists():
                errors.append(f"Broken local link in {path.relative_to(ROOT).as_posix()}: {target}")
    return errors


def main() -> int:
    try:
        errors = validate()
    except (OSError, ValueError, KeyError, TypeError, csv.Error) as error:
        print(f"FAIL: Cannot validate repository: {error}", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("PASS: CAD inventory, SHA-256 hashes, component snapshot and local documentation links.")
    print("Scope: file integrity only; SolidWorks geometry, mates and rebuilds are not checked here.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
