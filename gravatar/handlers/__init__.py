import os
import re
from sys import stderr
pattern = re.compile(r"^[^\.]*.py$")
handlers = []
for filename in os.listdir("handlers"):
	if filename == "__init__.py" or pattern.match(filename) == None:
		continue
	basename,_ = filename.split('.')
	importname = "handlers.%s"%basename
	module = __import__(importname)
	handlers.append(getattr(module, basename))
