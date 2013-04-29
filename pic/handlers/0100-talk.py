# coding: utf-8
import tornado.web
import db
import sns_share
url = r"/talk/(.*)"

class workclass(tornado.web.RequestHandler):
	def get_current_user(self):
		return self.get_secure_cookie("user")
	@tornado.web.authenticated
	def get(self, *args):
		user = db.get('User', self.current_user)
		if not user:
			self.clear_cookie("user")
			self.redirect("/")
			return 
		return self.render("../template/publish.html", NickName = user.NickName, IsAdmin = user.IsAdmin)
	@tornado.web.authenticated
	def post(self, *args):
		sns_share.share(user = self.current_user, **self.request.arguments)
		self.write(self.request.arguments)
