#define Data Model here
class __DataModel__:
	"""Base Class of Data Models"""
	def __init__(self, **kwargs):
		for member in dir(self):
			if member in __DataModel__.__dict__: continue
			setattr(self, member, kwargs.get(member, getattr(self.__class__,member)))
class User(__DataModel__):
	NickName = ""
	Email = ""
	Password = ""
	GravatarUrl = ""
class NickName(__DataModel__):
	pass
