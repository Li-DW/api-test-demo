import pytest
from api.client import ApiClient


# @pytest.fixture == “中央厨房专属标签”，作用域是 session（整个测试过程只执行一次）若是function（默认）则重复执行函数
@pytest.fixture(scope = "session")
def api_client():
    return ApiClient(base_url = "https://dummyjson.com")#以后诺频繁更换要测试的网址，直接来替换这里的网址
