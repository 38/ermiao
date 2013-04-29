# coding: utf-8
import tornado.web
import tornado.escape
import db 
import hashlib
url = "/accounts/login"
class workclass(tornado.web.RequestHandler):
	def get(self):
		self.render("../template/login.html", error_msg = "" )
	def post(self):
		email = self.get_argument('email',"")
		passwd = self.get_argument('password',"")
		user = db.get('User', email)
		if user and passwd and hashlib.md5(passwd).hexdigest() == user.Password:
			self.set_secure_cookie("user", email)
			next = self.get_argument("next");
			if next : next = tornado.escape.url_unescape(next)
			else: next = "/"
			self.redirect(next)
		else:
			self.render("../template/login.html", error_msg = "用户名或密码错误")
