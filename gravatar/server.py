import handlers
import tornado.web
import config
import db
db.set("NickName","fuck")
if __name__ == "__main__":
	handlist = []
	for handler in handlers.handlers:
		if "url" not in handler.__dict__ or "workclass" not in handler.__dict__:
			continue		
		if "parameter" in handler.__dict__:
			handlist.append((handler.url,handler.workclass,handler.parameter))
		else:
			handlist.append((handler.url,handler.workclass))
	print handlist
	app = tornado.web.Application(handlist, **config.Flags)
	app.listen(config.Port)
	tornado.ioloop.IOLoop.instance().start()
