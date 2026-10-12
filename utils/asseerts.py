
#HTTP状态断言
def http_assert(resp, expected_code) :
    assert resp.status_code == expected_code,f"状态码错误：预期：{expected_code},实际：{resp.status_code},URL:{resp.url}"

#关键字断言
def key_assert(resp, key):
    assert key in resp.json(),f"响应没有该字段：{key}"

