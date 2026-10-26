# 文件与装配检查记录

最新检查日期：2026-10-26（Asia/Shanghai）。检查对象为作者补入平键后保存的 `装配体1.SLDASM` 默认配置。

## 本次更新

作者更新后的装配体新增了 1 个平键组件。本次采用该装配文件，并从其本机原引用位置补齐 `plain parallel keys.sldprt`，未修改作者保存的装配体或已有零件的内容。

| 检查项 | 结果与依据 |
| --- | --- |
| 环境 | SolidWorks 2020 SP1，API 修订号 28.1.0 |
| 依赖完整性 | 35/35 个零件依赖可在仓库根目录找到 |
| 装配打开 | 只读打开成功，错误码 0，警告码 2（只读） |
| 组件解析 | 79 个组件实例，全部为 `swComponentFullyResolved`（数值 2） |
| 新增实例 | `plain parallel keys-1`，共 1 个 |
| 平键文件 | `plain parallel keys.sldprt` |
| 实际配置 | `GB_CONNECTING_PIECE_KEYS_CSK 3X25` |
| 与首版实例对比 | 仅新增上述平键实例，原 78 个实例均保留 |
| 内存重建 | `ForceRebuild3(false)` 返回 `true`；`NeedsRebuild2` 为 0 → 0 |
| 预览 | 从新版装配体导出 1600 × 1200 位图，无损转为 PNG，并查看确认 |
| 既有模型文件对比 | 相较首版清单，仅作者已更新的装配体内容变化；既有 34 个零件和参考 PDF 内容保持一致 |
| 文件清单 | 已更新装配体、平键和预览的大小与 SHA-256，以及 35 个依赖列表 |
| 组件快照 | `assembly-components.csv` 已重新读取并记录 79 个实例的文件、配置和状态 |

上述检查没有回写原生模型。平键的来源记录同时列在 [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md)，实际配置和数量列在 [PARTS.md](PARTS.md)。

## 首版检查历史（2026-10-22）

首版从初始 28 个零件、1 个装配体和 1 份参考 PDF 出发，恢复 6 个外部依赖，归档为 34 个零件文件、78 个组件实例。当时只读打开的警告掩码为 34，即只读（2）加需要重建（32）；在内存中重建成功，重建需求由 1 变为 0。初次整理保留了原始 30 个文件的内容。

本次采用作者之后保存的新版装配体，因此首版的“34 个零件、78 个实例”仅表示历史版本，不代表当前计数。

## 检查边界与导出状态

本次核查依赖、默认配置的组件状态及重建情况，没有对所有尺寸、草图约束、配合和干涉进行完整审计，也未执行强度、热流、物理运动或制造验证。组件完全解析和重建成功不代表已经逐项满足图纸精度或制造要求。

首版曾尝试导出 STEP，但 API 返回保存错误码 1，未生成交付文件；本次未重新执行 STEP 导出。当前交付以原生模型及正式 PNG 预览为准。

其他 SolidWorks 版本和其他 CAD 软件未逐一测试。原生文件可能保留历史引用路径；临时引用路径日志不包含在发布包中。

## 可重复执行的文件检查

```powershell
python scripts/check_repository.py
```

脚本检查必需文件、资产 SHA-256、35 个零件依赖、79 个实例记录及 Markdown 本地链接。GitHub Actions 运行同一检查，不会启动 SolidWorks，也不替代本机 CAD 检查。

API 语义见 SolidWorks 官方说明：[依赖读取](https://help.solidworks.com/2023/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentDependencies2.html)、[模型重建](https://help.solidworks.com/2019/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ForceRebuild3.html)。
