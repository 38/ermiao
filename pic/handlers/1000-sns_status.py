# coding : utf-8
import tornado.web
import db
import msgqueue

url = r'/sns_status'

def escape(string):
	return '"' + repr(string)[1:-1] + '"'

class workclass(tornado.web.RequestHandler):
	def get_current_user(self):
		return self.get_secure_cookie('user')
	@tornado.web.authenticated
	def get(self):
		user = db.get('User', self.current_user)
		if not user or not user.IsAdmin:
			self.write('{"error":1}')
			return
		try: num = int(self.request.arguments.get('num',10)[0])
		except TypeError: num = 10
		info = []
		for i in msgqueue.top(num):
			user = db.get('User',i['user'])
			if not user: continue
			username = user.NickName
			info.append( '{"user": %s, "url": %s},'%(escape(username), escape(i['url'])))
		info = "".join(info)
		if info != "" : info = info[:-1]   # strip the last ','
		self.write('{"error":0,"info":[%s]}'% info)

