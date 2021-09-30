import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornato_config
import tornato_application

if __name__ == '__main__':
    application = tornato_application.Application()
    httpserver = tornado.httpserver.HTTPServer(application)
    httpserver.bind(tornato_config.options["port"])
    httpserver.start(1)
    tornado.ioloop.IOLoop.current().start()
