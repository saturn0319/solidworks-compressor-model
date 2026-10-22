# GitHub 发布说明

## 仓库名称

推荐：`solidworks-compressor-model`

名称直接说明软件、对象和成果类型，便于作为机械 CAD 作品集展示。

中文展示标题：**SolidWorks 压缩机三维建模与装配**。

## About 简介

可直接复制到 GitHub 的 Description：

> 基于 2024 年河南省工业软件创新大赛图纸的 SolidWorks 压缩机建模项目，包含 34 个零件文件、78 个装配组件实例、真实模型预览及使用文档，展示机械识图、三维建模与装配实践。

英文简介：

> SolidWorks compressor CAD project based on the 2024 Henan Industrial Software Innovation Competition drawings, with 34 part files, 78 component instances, model previews, and documentation.

建议 Topics：`solidworks`、`cad`、`3d-modeling`、`mechanical-design`、`compressor`、`assembly`、`engineering`。

## 当前打包方式

完整目录保留原文件名，模型直接放在根目录。`dist/solidworks-compressor-model.zip` 是本次整理的上传副本，ZIP 内只有应发布的项目文件，不包含临时检查脚本、历史绝对路径日志或本地缓存。

向 GitHub 上传时应将 ZIP **解压后的内容**作为仓库文件，保留 `.github`、`.gitignore` 和 `.gitattributes`。ZIP 本身可另外作为 Release 附件。

## 通过 Git 上传

先在 GitHub 创建空仓库，仓库名使用 `solidworks-compressor-model`；不要让 GitHub 再次生成 README、License 或 `.gitignore`。按当前作者选择，GitHub 的许可证下拉框不应选择 MIT、CC 或其他开放许可，保留本仓库的自定义权利声明。

在项目根目录运行：

```powershell
python scripts/check_repository.py
git init -b main
git add .
git status --short
git commit -m "Initial release: SolidWorks compressor CAD project"
```

本项目对应的 GitHub 仓库地址如下；如果用于其他账户或仓库，请相应修改：

```powershell
git remote add origin https://github.com/saturn0319/solidworks-compressor-model.git
git remote -v
git push -u origin main
```

若本地已经有 Git 仓库或远程地址，先检查 `git status` 和 `git remote -v`，按实际情况沿用；不要重复初始化或覆盖已有远程。身份认证按 GitHub 提示完成，不要将令牌写进仓库文件或远程 URL。

以上流程依据 [GitHub 官方导入说明](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github) 整理。项目仓库地址为 https://github.com/saturn0319/solidworks-compressor-model 。

## 发布前与发布后

原创内容按作者选择保留全部权利。图纸及标准件的权利说明已列在 [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md)，其公开再分发授权尚未核实；在确认适用条款前，可先使用私有仓库归档。

上传后确认 README 图片、中文链接、全部 34 个零件和 GitHub Actions 文件检查正常。若后续调整任何模型，更新清单和检查记录；当前 ZIP 是整理时点的快照，修改后需重新打包。
