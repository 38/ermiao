# coding: utf-8
import tornado.web

url = r"/logout"

class workclass(tornado.web.RequestHandler):
	def get_current_user(self):
		return self.get_secure_cookie("user")
	@tornado.web.authenticated
	def get(self):
		self.clear_cookie("user")
		self.redirect("/")
