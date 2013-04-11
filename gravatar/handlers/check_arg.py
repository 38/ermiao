import tornado.web
import db
import gravatar
url=r"/checkarg"
class workclass(tornado.web.RequestHandler):
	def post(self):
		field = self.request.arguments.get('field',None)[0]
		value = self.request.arguments.get('value','')[0]
		if field == None or value == None:
			self.write("1")
			return
		if field == "nickname":
			if db.get("NickName", value):
				self.write("1")
				return
			else:
				self.write("0")
				return
		elif field == "email":
			if db.get("User", value):
				self.write("1")
				return
			else:
				if not gravatar.check_avatar_usable(value):
					self.write("2")
					return
				self.write("0")
				return
		self.write("1")

