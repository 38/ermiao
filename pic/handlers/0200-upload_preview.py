import tornado.web
import db
import hashlib
import Image

MAX_IMG_SIZE = (610,500)

url = r'/upload_preview'

class workclass(tornado.web.RequestHandler):
	def get_current_user(self):
		return self.get_secure_cookie('user')
	@tornado.web.authenticated
	def post(self):
		img = self.request.files.get('image',[None])[0]
		self.write('{\n\treturn:')
		if img:
			next_id = hashlib.md5(img['body']).hexdigest()
			filename = "image/userimg_%s.jpg"%next_id
			try:
				fp = open(filename, "wb")
				fp.write(img['body'])
				fp.close()
				img = Image.open(filename)
				img_sz = img.size
				#try to compress the image 
				if img_sz[0] > MAX_IMG_SIZE[0] or img_sz[1] > MAX_IMG_SIZE[0]:
					rate = min(MAX_IMG_SIZE[0]/float(img_sz[0]),
							   MAX_IMG_SIZE[1]/float(img_sz[1]))
					img = img.resize((int(img_sz[0]*rate), int(img_sz[1]*rate)),1)
				img.save(filename)
			except IOError:
				self.write('1\n}')
				return
			self.write('0,\n')
			self.write('\tid: \'%s\'\n}'%next_id)
			db.set('Image', next_id, { 'Path': filename, 'User': self.current_user })
		else:
			self.write('1\n}')
