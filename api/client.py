import requests
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class ApiClient:
    def __init__(self,base_url):
        self.base_url = base_url
        self.session = requests.Session()#调用方法初始化一个对象并赋予
    
    def get(self,endpoint):
        url = f"{self.base_url}{endpoint}"
        logging.info(f"发送GET: {url}")
        resp = self.session.get(url,timeout = 10)
        logging.info(f"状态码: {resp.status_code}")
        return resp

    def post(self,endpoint,data = None,json = None,**kwargs):
        url = f"{self.base_url}{endpoint}"
        logging.info(f"发送POST: {url}")
        resp = self.session.post(url,data = data,json = json,timeout = 10,**kwargs)
        logging.info(f"状态码：{resp.status_code}" )
        return resp