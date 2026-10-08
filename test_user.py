"""
import requests

def test_get_user_1():
    url = "https://jsonplaceholder.typicode.com/users/1"
    resp = requests.get(url,timeout = 10)

    # 2. 断言（质检员拿尺子量）
    assert resp.status_code == 200
    assert resp.json()["id"] == 1
    assert resp.json()["name"] == "Leanne Graham"

    print("测试通过！拿到数据了！")
"""
    #没有 assert 的代码叫“脚本”，有了 assert 的代码才叫“测试”


import pytest
import allure
"""
@allure.feature("用户模块")
@allure.story("获取用户信息")
@pytest.mark.parametrize(
    "user_id,expected_name",#自己定义的两个参数
    [
        (1, "Leanne Graham"),   
        (2, "Ervin Howell"),    
        (3, "Clementine Bauch") 
    ]
)#def函数不能换行，否则@装饰器会找不到要装饰的函数
def test_get_user_1(api_client,user_id,expected_name):#必须在函数的参数中提到(base_url和timeout)才能用到conftest的夹具fixture
    resp = api_client.get(f"/users/{user_id}") # 6. 用f-string拼凑URL

    assert resp.status_code == 200
    assert resp.json()["id"] == user_id
    assert resp.json()["name"] == expected_name
"""

@allure.feature("认证模块")
@allure.story("用户登录")
def test_login(api_client):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    resp = api_client.post("/api/login", json=payload)
    assert resp.status_code == 200
    assert "token" in resp.json()