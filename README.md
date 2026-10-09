# API 自动化测试框架

基于 Python + Pytest + Requests + Allure + GitHub Actions 的接口自动化测试框架。

## 📁 项目结构
- `api/client.py`：Requests 二次封装，统一管理会话（Session）、超时与日志。
- `conftest.py`：全局配置，基于 Fixture 实现依赖注入。
- `testcases/`：测试用例，支持数据驱动（Parametrize）。
- `data/`：测试数据（YAML 文件），实现数据与代码分离。
- `utils/`：工具类（如 YAML 读取）。
- `.github/workflows/test.yml`：GitHub Actions 持续集成配置。

## 🚀 技术栈
- Python 3.11
- Pytest / Requests / PyYAML / Allure
- CI/CD：GitHub Actions

## ⚙️ 运行方式
1. 安装依赖：`pip install -r requirements.txt`
2. 运行测试：`pytest -v`
3. 查看报告：`allure serve allure-results`
