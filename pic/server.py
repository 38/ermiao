# coding: utf-8
import handlers
import tornado.web
import config
import db

#data for testing
db.set("User", "admin@ermiao.com", {"NickName": "管理员", "Password": "e10adc3949ba59abbe56e057f20f883e", "IsAdmin": True})
db.set("User", "user@ermiao.com", {"NickName": "普通用户", "Password": "e10adc3949ba59abbe56e057f20f883e", "IsAdmin": False})

if __name__ == "__main__":
	handlist = []
	for handler in handlers.handlers:
		if "url" not in handler.__dict__ or "workclass" not in handler.__dict__:
			continue		
		if "parameter" in handler.__dict__:
			handlist.append((handler.url,handler.workclass,handler.parameter))
		else:
			handlist.append((handler.url,handler.workclass))
		print handlist[-1]
	app = tornado.web.Application(handlist, **config.Flags)
	app.listen(config.Port)
	tornado.ioloop.IOLoop.instance().start()
