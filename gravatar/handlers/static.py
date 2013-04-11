import tornado.web
url = r"/static/(.*)"
parameter = {"path": "./static"}
workclass = tornado.web.StaticFileHandler
