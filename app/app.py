# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.web
import logging
from tornado.options import options

from conf import settings

from route import routes

class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, routes, **settings)

def main():
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    local_ip = "0.0.0.0"
    logging.info("server started at port {0}".format(options.port))
    main()
