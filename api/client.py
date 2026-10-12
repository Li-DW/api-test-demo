import logging

import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class ApiClient:
    def __init__(self,base_url):
        self.base_url = base_url
        self.session = requests.Session()#调用方法初始化一个对象并赋予
    
    def get(self,endpoint,**kwargs):
        url = f"{self.base_url}{endpoint}"
        logging.info(f"发送GET: {url}")  
        resp = self.session.get(url,timeout = 10,**kwargs)
        logging.info(f"状态码: {resp.status_code}")
        return resp

    def post(self,endpoint,data = None,json = None,headers = None,**kwargs):
        url = f"{self.base_url}{endpoint}"
        logging.info(f"发送POST: {url}")
        resp = self.session.post(url,data = data,json = json,headers = headers,timeout = 10,**kwargs)
        logging.info(f"状态码：{resp.status_code}" )

        if resp.status_code == 401:
            logging.warning("Token已过期，尝试重新登录")
            new_token = self._refresh_token()
            if new_token:#返回不为空，替换headers中的token，其他元素不变
                headers =headers or {}
                headers["Authorization"] = f"Bearer {new_token}" 
                resp = self.session.post(url,data = data,json = json,headers = headers,timeout =10,**kwargs)
                logging.info(f"重试后状态码：{resp.status_code}")

        return resp
    def _refresh_token(self):
        try:
            resp = self.session.post(f"{self.base_url}/auth/login",
                    json={"username": "emilys", "password": "emilyspass"},
                    timeout=10
            )
            if resp.status_code == 200:
                return resp.json()["accessToken"]
        except Exception as e:
            logging.error(f"刷新Token失败：{e}")
        return None
        