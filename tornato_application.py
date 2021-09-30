import tornado.web
from views import index
import tornato_config


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', index.IndexHandler),
            # pass parameter
            (r'/home', index.HomePageHandler, {"word1": "good", "word2": "nice"}),
            # Reverse DNS 反向解析
            tornado.web.url(r'/reverseDNS', index.ReverseDNSHandler,name="json_name"),
            # extract url
            (r'/request/(\w+)/(\w+)/(\w+)', index.HTTPRequestHandler),
            # or  (r'/request/(?<p1>\w+)/(?<p2>\w+)/(?<p3>\w+)', index.HTTPRequestHandler),
            # get parameter  http://192.168.1.105:7000/get?a=1&b=2
            (r'/get', index.GetHandler),
            # post
            (r'/post', index.PostHandler),
            # request_attribute
            (r'/requestattribute', index.RequestAttributeHandler),
            # upfile
            (r'/upfile',index.UpfileHandler ),
            # write
            (r'/write', index.WriteHandler),
            # json
            (r'/json', index.JsonHandler),
            # redirect
            (r'/index', index.RedirectHandler),
            # error handle
            (r'/iserror', index.ErrorHandler),

        ]
        super(Application, self).__init__(handlers, **tornato_config.settings)
