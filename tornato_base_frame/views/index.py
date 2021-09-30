import tornado.web
from tornado.web import RequestHandler


# 业务处理类
class IndexHandler(RequestHandler):
    def get(self):
        # 给浏览器响应信息
        self.write('hello ,world')


class HomePageHandler(RequestHandler):
    # def initialize(self, word1, word2) -> None:
    #     print(word1)
    #     self.word1 = word1
    #     self.word2 = word2

    def get(self):
        # 给浏览器响应信息
        self.write('home page')
