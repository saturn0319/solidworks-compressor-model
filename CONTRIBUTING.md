# 协作与反馈

欢迎反馈文件缺失、模型打开异常、零件与图纸对应问题，以及文档错误。

提交 Issue 时，请提供 SolidWorks 版本及 Service Pack、打开的文件与配置、提示文字和复现步骤。截图请去除个人路径、用户名等无关信息。

CAD 文件为二进制，Git 无法像文本一样合并几何修改。模型修改前请先通过 Issue 协商范围与授权，避免并行修改同一文件。反馈或提交修改本身不改变 [LICENSE](LICENSE) 中的使用授权。

如已获准提交模型修改，请：

1. 保留原命名，或通过 CAD 工具同步处理文件引用。
2. 说明修改的零件、原因、软件版本及图纸依据。
3. 完整解析并重建装配体，检查依赖、配置和受影响的配合。
4. 更新预览、`docs/assembly-components.csv` 与 `docs/model-manifest.json`；哈希可用 Python 标准库 `hashlib.sha256` 计算。
5. 运行 `python scripts/check_repository.py`，并在提交中区分文件检查和实际 CAD 检查结果。

不要提交锁文件、备份、恢复文件、个人软件配置、凭据或与本项目无关的资料。
