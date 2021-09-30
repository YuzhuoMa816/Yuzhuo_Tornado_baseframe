import tornado.web
from views import index
import tornato_config


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', index.IndexHandler),
        ]
        super(Application, self).__init__(handlers, **tornato_config.settings)
