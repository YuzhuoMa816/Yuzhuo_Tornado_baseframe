import os

from tornado.web import RequestHandler

# 业务处理类
import tornato_config


class IndexHandler(RequestHandler):
    def get(self):
        # 给浏览器响应信息
        url = self.reverse_url("json_name")
        self.write('<a href = "%s" >go to another page</a>' % url)


class HomePageHandler(RequestHandler):
    def initialize(self, word1, word2) -> None:
        self.word1 = word1
        self.word2 = word2

    def get(self):
        # 给浏览器响应信息
        self.write('home page')


class WriteHandler(RequestHandler):
    def get(self):
        self.write('write page')
        self.write('write page2')
        self.finish()


class JsonHandler(RequestHandler):
    def get(self):
        person = {
            "name": "Yuzhuo",
            "age": 21,
            "height": 182
        }
        self.write(person)


class RedirectHandler(RequestHandler):
    def get(self):
        self.redirect("/")


class HTTPRequestHandler(RequestHandler):
    def get(self, h1, h2, h3):
        print(h1, h2, h3)
        self.write("in HTTPRequestHandler")


class GetHandler(RequestHandler):
    def get(self):
        print(self.get_argument("a", default="10"))
        self.write("in GetHandler")


class PostHandler(RequestHandler):
    def get(self):
        self.render("postfile.html")

    def post(self):
        username = self.get_argument("username")
        passwd = self.get_argument("passwd")
        hobbylist = self.get_argument("hobby")
        print(username, passwd, hobbylist)
        self.write("Login success")


class RequestAttributeHandler(RequestHandler):
    def get(self):
        # print(self.request.method)
        print("in")
        print(self.request.path)
        print(self.request.host)
        print("query", self.request.query)
        print("body", self.request.body)
        print(self.request.uri)
        print(self.request.version)
        print(self.request.headers)
        print(self.request.remote_ip)
        self.write("in requestattribute")


class UpfileHandler(RequestHandler):
    def get(self):
        self.render("upfile.html")

    def post(self):
        files = self.request.files
        for inputfile in files:
            fileArr = files[inputfile]
            for file_obj in fileArr:
                file_path = os.path.join(tornato_config.BASE_DIRS, "upfile/" + file_obj.filename)
                with open(file_path, "wb") as f:
                    f.write(file_obj.body)
        self.write("Upload Success")


class ErrorHandler(RequestHandler):
    def write_error(self, status_code: int, **kwargs) -> None:
        if status_code == 500:
            code = 500
            # 返回500页面
            self.write("server error")
        elif status_code == 404:
            code = 404
            # 返回404页面
            self.write("forbidden")
        self.set_status(code)

    def get(self):
        flag = self.get_query_argument("flag")
        if flag == "0":
            self.send_error(500)
        self.write("correct")


class ReverseDNSHandler(RequestHandler):
    def get(self):
        # 给浏览器响应信息
        self.write('reverseDNS example')
