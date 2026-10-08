import requests

# 这是一个免费公开的测试接口
url = "https://jsonplaceholder.typicode.com/users/1"

# 发送 GET 请求
resp = requests.get(url, timeout=10)

# 打印结果
print("状态码:", resp.status_code)
print("响应内容:", resp.json())