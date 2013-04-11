import urllib2
import hashlib
prefix = "http://en.gravatar.com/"
def check_avatar_usable(email):
	email = email.strip()
	md5 = hashlib.md5(email).hexdigest()
	url = prefix + md5 + ".json"
	try:
		urllib2.urlopen(url)
	except urllib2.HTTPError as e:
		if e.getcode() == 404:
			return False
		return None
	return True
