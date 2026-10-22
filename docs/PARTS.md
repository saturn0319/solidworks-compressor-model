# 零件文件与实际装配清单

本清单基于现有文件、参考图纸与 SolidWorks API 读取的默认配置。数量为装配体中的实际实例数，不是图纸要求数量的验收结论。

## 计数口径

| 项目 | 数量 |
| --- | --- |
| 初始工作区零件文件 | 28 |
| 补齐的原装配依赖文件 | 6 |
| 当前零件文件合计 | 34 |
| 装配体 | 1 |
| 默认配置组件实例 | 78 |

一个标准件文件可以提供多个配置，一个零件可以被插入多次，因此不能用文件数量推算图纸明细表条数或装配实例数量。

## 初始工作区零件

以下 28 个文件均保留原文件名与原始内容。图纸序号与页码按参考 PDF 标题栏整理。

| 图纸序号 | 零件文件 | PDF 页码 | 实际实例数 |
| --- | --- | --- | --- |
| 1 | [法兰垫圈.SLDPRT](../%E6%B3%95%E5%85%B0%E5%9E%AB%E5%9C%88.SLDPRT) | 7 | 1 |
| 3 | [带轮.SLDPRT](../%E5%B8%A6%E8%BD%AE.SLDPRT) | 3 | 1 |
| 4 | [曲轴.SLDPRT](../%E6%9B%B2%E8%BD%B4.SLDPRT) | 3 | 1 |
| 7 | [顶盖.SLDPRT](../%E9%A1%B6%E7%9B%96.SLDPRT) | 5 | 1 |
| 8 | [轴套.SLDPRT](../%E8%BD%B4%E5%A5%97.SLDPRT) | 5 | 1 |
| 9 | [密封圈.SLDPRT](../%E5%AF%86%E5%B0%81%E5%9C%88.SLDPRT) | 5 | 1 |
| 10 | [法兰.SLDPRT](../%E6%B3%95%E5%85%B0.SLDPRT) | 7 | 1 |
| 11 | [冷却器.SLDPRT](../%E5%86%B7%E5%8D%B4%E5%99%A8.SLDPRT) | 3 | 1 |
| 12 | [法兰垫片.SLDPRT](../%E6%B3%95%E5%85%B0%E5%9E%AB%E7%89%87.SLDPRT) | 6 | 1 |
| 14 | [阀板.SLDPRT](../%E9%98%80%E6%9D%BF.SLDPRT) | 7 | 1 |
| 16 | [出气盖.SLDPRT](../%E5%87%BA%E6%B0%94%E7%9B%96.SLDPRT) | 4 | 1 |
| 17 | [控制杆.SLDPRT](../%E6%8E%A7%E5%88%B6%E6%9D%86.SLDPRT) | 6 | 2 |
| 18 | [活塞.SLDPRT](../%E6%B4%BB%E5%A1%9E.SLDPRT) | 6 | 1 |
| 20 | [转销.SLDPRT](../%E8%BD%AC%E9%94%80.SLDPRT) | 6 | 1 |
| 21 | [拨叉.SLDPRT](../%E6%8B%A8%E5%8F%89.SLDPRT) | 6 | 1 |
| 22 | [轴塞.SLDPRT](../%E8%BD%B4%E5%A1%9E.SLDPRT) | 7 | 1 |
| 23 | [阀盖.SLDPRT](../%E9%98%80%E7%9B%96.SLDPRT) | 6 | 1 |
| 24 | [泵体.SLDPRT](../%E6%B3%B5%E4%BD%93.SLDPRT) | 2 | 1 |
| 26 | [底板垫片.SLDPRT](../%E5%BA%95%E6%9D%BF%E5%9E%AB%E7%89%87.SLDPRT) | 7 | 1 |
| 27 | [底板.SLDPRT](../%E5%BA%95%E6%9D%BF.SLDPRT) | 4 | 1 |
| 30 | [锁紧套.SLDPRT](../%E9%94%81%E7%B4%A7%E5%A5%97.SLDPRT) | 6 | 1 |
| 33 | [气管接头.SLDPRT](../%E6%B0%94%E7%AE%A1%E6%8E%A5%E5%A4%B4.SLDPRT) | 5 | 2 |
| 34 | [垫片1.SLDPRT](../%E5%9E%AB%E7%89%871.SLDPRT) | 5 | 1 |
| 35 | [进气盖垫片.SLDPRT](../%E8%BF%9B%E6%B0%94%E7%9B%96%E5%9E%AB%E7%89%87.SLDPRT) | 5 | 1 |
| 36 | [进气盖.SLDPRT](../%E8%BF%9B%E6%B0%94%E7%9B%96.SLDPRT) | 4 | 1 |
| 37 | [锁紧螺钉.SLDPRT](../%E9%94%81%E7%B4%A7%E8%9E%BA%E9%92%89.SLDPRT) | 5 | 1 |
| 38 | [垫片2.SLDPRT](../%E5%9E%AB%E7%89%872.SLDPRT) | 5 | 1 |
| 39 | [气路卡套.SLDPRT](../%E6%B0%94%E8%B7%AF%E5%8D%A1%E5%A5%97.SLDPRT) | 5 | 2 |

## 补齐的标准件依赖

下面 6 个文件原来由装配体从工作区外引用，本次从本机原位置复制到根目录；没有重新创建近似替代件。文件数量不等于实例数量。

| 文件 | 实际实例数 |
| --- | --- |
| [hexagon head bolts gb.sldprt](../hexagon%20head%20bolts%20gb.sldprt) | 5 |
| [hexagon nuts grade c gb.sldprt](../hexagon%20nuts%20grade%20c%20gb.sldprt) | 3 |
| [hexagon socket head cap screws gb.sldprt](../hexagon%20socket%20head%20cap%20screws%20gb.sldprt) | 33 |
| [parallel pins unhardening steel gb.sldprt](../parallel%20pins%20unhardening%20steel%20gb.sldprt) | 3 |
| [plain washers-n series-grade a gb.sldprt](../plain%20washers-n%20series-grade%20a%20gb.sldprt) | 2 |
| [挡圈.SLDPRT](../%E6%8C%A1%E5%9C%88.SLDPRT) | 1 |

标准件来源与权利说明见 [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md)。

## 标准件实际配置

配置标识直接来自装配组件。以下结果用于如实记录当前模型；尚未与参考图纸的每项标准号、规格和数量逐一验收。

| 零件文件 | 实际引用配置 | 实例数 |
| --- | --- | --- |
| `hexagon head bolts gb.sldprt` | `GB_FASTENER_BOLT_SB A M8X45-N` | 5 |
| `hexagon nuts grade c gb.sldprt` | `GB_FASTENER_NUT_SNC1 M10-N` | 1 |
| `hexagon nuts grade c gb.sldprt` | `GB_FASTENER_NUT_SNC1 M8-N` | 2 |
| `hexagon socket head cap screws gb.sldprt` | `GB_FASTENER_SCREWS_HSHCS M8X12-N` | 16 |
| `hexagon socket head cap screws gb.sldprt` | `GB_FASTENER_SCREWS_HSHCS M8X20-N` | 6 |
| `hexagon socket head cap screws gb.sldprt` | `GB_FASTENER_SCREWS_HSHCS M8X25-N` | 11 |
| `parallel pins unhardening steel gb.sldprt` | `GB_CONNECTING_PIECE_PIN_PPUS 3X14` | 1 |
| `parallel pins unhardening steel gb.sldprt` | `GB_CONNECTING_PIECE_PIN_PPUS 3X18` | 2 |
| `plain washers-n series-grade a gb.sldprt` | `GB_FASTENER_WASHER_PWNA 8` | 2 |
| `挡圈.SLDPRT` | `GB_CONNECTING_PIECE_RINGS_RSRS 10` | 1 |

例如，当前装配中的内六角螺钉配置包括 M8×12、M8×20 和 M8×25；图纸明细表还需另行核对，不能把这一实际配置表当作制造用 BOM。

逐实例明细可查看 [assembly-components.csv](assembly-components.csv)，包括实例名称、文件、引用配置和读取时的解析状态。

## 按结构阅读

| 结构 | 推荐先查看的零件 |
| --- | --- |
| 主体与安装 | 泵体、底板、法兰 |
| 传动与往复运动 | 带轮、曲轴、拨叉、转销、活塞 |
| 进排气与控制 | 进气盖、出气盖、阀板、阀盖、控制杆、气管接头、气路卡套 |
| 支承、封闭与密封 | 轴套、轴塞、顶盖、密封圈、各类垫片 |
| 连接与紧固 | 锁紧套、锁紧螺钉、标准螺钉/螺栓/螺母/销/垫圈/挡圈 |

此分类仅帮助定位现有文件，不替代装配图中的结构定义。
