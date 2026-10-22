# SolidWorks Compressor Modeling and Assembly

[中文说明](../README.md) · [CAD guide (Chinese)](CAD_GUIDE.md) · [Parts inventory](PARTS.md) · [Validation record](VALIDATION.md)

![Compressor assembly exported from SolidWorks](images/assembly-isometric.png)

A mechanical CAD portfolio project based on the compressor drawings supplied for the 2024 Henan Industrial Software Innovation Competition. It preserves native SolidWorks parts and an assembly, with a model preview, an actual component inventory, reference-drawing index, and file-integrity checks.

## Included

- 34 native part files and one assembly, `装配体1.SLDASM`.
- 78 fully resolved component instances in the default configuration.
- The original seven-page reference PDF, with separate third-party notices.
- A PNG preview exported directly from the rebuilt assembly.
- SHA-256 asset inventory, component/configuration CSV, and a standard-library Python validator.

The initial workspace held 28 parts. Six existing external dependencies were recovered from their original local reference locations and copied into the repository. These include standard fastener and retaining-ring files; they are identified separately from the original project models.

## Open the assembly

Download or clone the entire repository and keep all CAD files together in the root directory. Open `装配体1.SLDASM` in SolidWorks and select the default configuration (`默认`). If prompted for an old reference location, select the matching file in the repository root.

The assembly was checked read-only using **SolidWorks 2020 SP1**, API revision **28.1.0**. Opening returned no errors. The read-only and rebuild-required warnings were recorded; rebuilding in memory succeeded and cleared the rebuild-needed state. Original native files were not overwritten, so a rebuild prompt may still appear on reopening. Compatibility with other versions has not been tested.

## Verify the archive

With Python 3.10 or later, run from the repository root:

```sh
python scripts/check_repository.py
```

The validator checks asset hashes, the dependency/component snapshot, required documents and local Markdown links. It does not run SolidWorks or validate geometry, mates, interference or manufacturability.

## Scope and rights

The archive does not include separate 2D drawing files or motion animation. STEP export was attempted but did not produce a deliverable file. Model dimensions and fastener configurations have not been fully reconciled with every drawing requirement, and no manufacturing or simulation validation is claimed.

Original models and original documentation are **all rights reserved**; no additional reuse license is granted. The reference drawings and standard components retain their respective owners' rights. See [LICENSE](../LICENSE) and [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md). Feedback is welcome through Issues; coordinate model changes and permissions before submitting them.
