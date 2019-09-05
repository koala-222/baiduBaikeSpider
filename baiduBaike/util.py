import urllib.request


class Util:
    def __init__(self):
        super().__init__()
        self.poolsize = 300
        self.proxies = []
        while len(self.proxies) < self.poolsize:
            self.proxies = self.get_proxy_list(500)
    

    @staticmethod
    def get_proxy_list(num = 500):
            '''
            调用"快代理"API提取代理
            '''
            return []  # 返回列表
