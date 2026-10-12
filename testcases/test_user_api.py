import allure

from utils.asseerts import http_assert, key_assert


@allure.feature("用户模块")
@allure.story("查询单个用户")
def test_get_single_user(api_client):
    resp = api_client.get("/user/1")

    http_assert(resp, 200)
    assert resp.json()["id"] == 1
    key_assert(resp,"firstName")

@allure.feature("用户模块")
@allure.story("分页查询用户列表")
def test_get_user_list(api_client):
    resp = api_client.get("/users",params = {"limit": 5,"skip": 0})#5条，跳过0条

    http_assert(resp, 200)
    assert len(resp.json()["users"]) == 5
    assert resp.json()["total"] > 0

@allure.feature("用户模块")
@allure.story("搜索用户")
def test_search_user(api_client):
    resp = api_client.get("/users/search",params={"q": "John"})
      
    assert resp.status_code == 200
    assert len(resp.json()["users"]) > 0