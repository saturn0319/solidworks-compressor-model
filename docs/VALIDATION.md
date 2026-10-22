# 文件与装配检查记录

检查日期：2026-10-22（Asia/Shanghai）。检查对象为当前仓库默认配置与整理时点的文件快照。

## 已执行检查

| 检查项 | 结果与依据 |
| --- | --- |
| 初始文件盘点 | 28 个零件、1 个装配体、1 份 7 页 PDF，共 30 个原始文件 |
| 依赖读取 | 使用已安装的 SolidWorks 2020 SP1 API 读取，发现 34 个零件依赖 |
| 缺失文件补齐 | 从本机原引用位置复制 6 个现存文件，保留原文件名；清单见第三方说明 |
| 仓库内依赖存在性 | 34/34 个依赖均可在根目录找到 |
| 默认配置打开 | 只读打开成功；打开错误码为 0 |
| 组件解析状态 | 78 个组件实例，读出状态均为 `swComponentFullyResolved`（数值 2） |
| 打开警告 | 掩码 34 = 2（只读）+ 32（需要重建）；只读为检查时主动选择 |
| 内存中重建 | `ForceRebuild3(false)` 返回 `true`；`NeedsRebuild2` 由 1 变为 0 |
| 模型预览 | 对内存重建后的默认配置直接导出 1600 × 1200 位图，再无损保存为 PNG；已人工查看图像 |
| 原始内容保留 | 比较整理前后 SHA-256，初始 30 个文件内容均未改变 |
| 文件清单 | 模型、参考 PDF 与正式预览的大小及 SHA-256 保存在 `model-manifest.json` |
| 组件快照 | 实际实例名称、文件、配置和状态保存在 `assembly-components.csv` |

内存重建没有回写原生文件。因此，重新打开原文件时仍可能出现“需要重建”提示；这是保留原始内容的结果，不应表述为原文件已经保存了重建状态。

## 本次未交付的导出

尝试将只读装配导出为 STEP 时，API 返回失败（保存错误码 1，警告码 0），未生成可交付 STEP 文件。当前交付以原生文件和已验证的 PNG 预览为准，未将失败导出列入清单。

## 检查边界

本次没有对每个建模特征、草图约束、装配配合与图纸尺寸进行完整审计，没有执行整机干涉检查、物理运动验证、应力/热流仿真或制造验证。

组件完全解析表示引用文件可用，不代表配合全部正确。重建成功也不等于已确认全部组件无干涉或满足图纸精度。实际标准件配置和数量见 [PARTS.md](PARTS.md)，尚未与图纸明细表逐项验收。

本次仅核查 SolidWorks 2020 SP1，未声称兼容所有 CAD 软件或所有 SolidWorks 版本。原生 CAD 可能保留历史引用路径与文档内部属性；临时导出的绝对路径日志未纳入发布包。

## 可重复执行的文件检查

```powershell
python scripts/check_repository.py
```

该脚本检查必需文件、清单中的哈希、34 个组件文件依赖、78 个实例记录与 Markdown 本地链接。GitHub Actions 执行同一文件检查；它不启动 SolidWorks，不能替代上面的人工与本机 CAD 检查。

涉及的 API 语义可参阅 SolidWorks 官方说明：[依赖读取](https://help.solidworks.com/2023/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentDependencies2.html)、[模型重建](https://help.solidworks.com/2019/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ForceRebuild3.html)。
