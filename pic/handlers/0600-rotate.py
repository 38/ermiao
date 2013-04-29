# coding: utf8
import tornado.web
import db
import Image


url = r'/rotate'

class workclass(tornado.web.RequestHandler):
	def get_current_user(self):
		return self.get_secure_cookie('user')
	@tornado.web.authenticated
	def post(self):
		print self.request.arguments
		if 'id' not in self.request.arguments or 'dir' not in self.request.arguments:
			return
		id = self.request.arguments['id'][0]
		direct = self.request.arguments['dir'][0]
		try:
			direct = int(direct)
		except:
			return
		if direct == 0 : return
		if direct > 0 : direct = 1
		else: direct = -1
		img = db.get("Image", id)
		if not img or img.User != self.current_user: return
		# 这里需要并发控制,不过图片是存在数据库里就不需要考虑这个问题了
		tmp = Image.open(img.Path)
		res = tmp.rotate((360 + 90 * direct)%360)
		res.save(img.Path)

		
