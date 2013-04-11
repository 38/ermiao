# coding=utf8
import tornado.web
import db
import hashlib
url=r"/do_reg"
class workclass(tornado.web.RequestHandler):
	def post(self):
		print self.request.arguments
		email = self.request.arguments.get("email", [None])[0]
		nickname = self.request.arguments.get("nickname", [None])[0]
		password = self.request.arguments.get("password", [None])[0]
		if db.get("User", email) or db.get("NickName", nickname): 
			self.write("invaild argument")
			return
		db.set("User", email, {"Email": email, "NickName": nickname, "Password": password})
		self.set_cookie("email", email) #当然这个地方需要认证，不过这个地方先简化
		self.redirect("/index")

		
