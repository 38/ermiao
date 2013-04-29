# coding:utf-8
import tornado.web
url = r"/"
class workclass(tornado.web.RequestHandler):
	def get(self):
		"""首页就省略了,要是能有你们整个的代码,
		   可以在中间增加,但是只能这样mock一下"""
		self.redirect("/talk/")
