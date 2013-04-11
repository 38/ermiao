import tornado.web
import db 
import hashlib
import tornado.template
url=r"/index"
template_loader = tornado.template.Loader("template/")
class workclass(tornado.web.RequestHandler):
	def get(self):
		email = self.get_cookie("email")
		nickname = db.get('User',email).NickName
		avatar = "http://en.gravatar.com/avatar/" + hashlib.md5(email.strip()).hexdigest() + ".jpg"
		self.write( template_loader.load("index.html").generate(nickname = nickname, avatar = avatar))

		
			
