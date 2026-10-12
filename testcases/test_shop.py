import allure
import pytest

from utils.yaml_reader import read_yaml

login_data = read_yaml("data/login_data.yaml")

@allure.feature("认证函数")
@pytest.mark.parametrize("case_name,user_info",login_data.items())
def test_login_with_yaml(api_client,case_name,user_info):
    resp = api_client.post("/auth/login",json = user_info)

    if  case_name == "valid_login":
        assert resp.status_code == 200
        assert "accessToken" in resp.json()
    else:
        assert resp.status_code in [400,401]

@allure.feature("电商业务")
@allure.story("加入购物车")
def test_add_to_cart(api_client):
    login_resp = api_client.post("/auth/login",json={"username": "emilys", "password": "emilyspass"})
    token = login_resp.json()['accessToken']

    # 2. 带着 Token 查商品 1
    product_resp = api_client.get("/products/1")
    assert product_resp.status_code == 200
    assert product_resp.json()["id"] == 1

    headers = {"Authorization": f"Bearer {token}"}
    cart_resp = api_client.post("/carts/add",json={"userId": 1, "products": [{"id": 1, "quantity": 1}]}, headers=headers)
    assert cart_resp.status_code == 201
    assert len(cart_resp.json()["products"]) > 0