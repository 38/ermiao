import tornado.web
url = r"/"
class workclass(tornado.web.RequestHandler):
	def get(self):
		self.redirect("/static/register.html")
