import tornado.web
url = r"/(.*)"
parameter = {"path": "./static"}
workclass = tornado.web.StaticFileHandler
