# tornado web basic module
import tornado.web
# io 循环模块 封装了package linux 的 epoll和 bsd的 kqueue
import tornado.ioloop
# httpserver 模块
import tornado.httpserver
import tornato_config_notebook


# 业务处理类
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # 给浏览器响应信息
        self.write('hello ,world')


if __name__ == '__main__':
    print(tornato_config_notebook.options.list)
    # Application 是tornatop web框架的核心应用类，与服务器对应的接口
    # 里面保存了路由映射表
    application = tornado.web.Application([
        (r'/', IndexHandler)
    ])
    # 绑定监听端口
    # 注意，此时服务器没有开启监听
    # application.listen(8000)

    # 或者尝试实例化http服务器对象 -- 创建http服务器
    httpserver = tornado.httpserver.HTTPServer(application)
    # httpserver.listen(8000)

    # 如果启动多进程，不能用listen,改成bind绑定8000端口， start5个线程
    httpserver.bind(tornato_config_notebook.options.port)
    # 如果<=0或者None，开启对应硬件cpu核心个数的子进程
    # 最好不要在这里开多进程，
    # 1.每个子进程都会复制ioloop实例，如果创建子进程时修改了ioloop，会影响所有的子进程
    # 2.无法做到不停止服务的情况下修改代码
    # 3.所有进程分享一个端口，不好监控
    httpserver.start(1)

    # IOLoop.current() 返回当前线程的IOloop实例
    # IOLoop.start() 开启IOloop实例I/O循环，同时开启了监听
    tornado.ioloop.IOLoop.current().start()
