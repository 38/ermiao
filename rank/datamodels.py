#define Data Model here
class __DataModel__:
	"""Base Class of Data Models"""
	def __init__(self, **kwargs):
		for member in dir(self):
			if member in __DataModel__.__dict__: continue
			setattr(self, member, kwargs.get(member, getattr(self.__class__,member)))
class Pet(__DataModel__):
	id = 0
	name = "ermiao"
	avatar_uri = ""
	user = ""
	type = ""
	created_date = None
class __photo__(__DataModel__):
	id = 0
	image_uri = ""
	pet = 0
	user = ""
	text = ""
	like_count = 0
	created_date = None
Cat = __photo__
Dog = __photo__
Other = __photo__
