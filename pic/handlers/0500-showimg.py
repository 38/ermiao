import tornado.web
import db

url = r'/showimg'

class workclass(tornado.web.RequestHandler):
	def get_current_user(self):
		return self.get_secure_cookie('user')
	def get(self):
		id = self.request.arguments.get('id',None)
		if not id: return
		image = db.get('Image', id[0])
		if image:
			self.set_header('Content-Type', 'image/jpeg')
			fp = file(image.Path,"rb")
			self.write(fp.read())
			#self.write(image.Data['body'])

