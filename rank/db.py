#A mock for K-V DB using dict
import datamodels
import re
_tables = {}
dm_pattern = re.compile("^__[A-Za-z0-9 ]+(_[A-Za-z0-9 ]+)*__$")
for dm in dir(datamodels):
	if dm_pattern.match(dm): continue
	print "Data module %s defined"%dm
	model = getattr(datamodels, dm)
	_tables[dm] = (model, {})
def get(table,key):
	if table not in _tables: return None
	if key not in _tables[table][1]: return None
	return _tables[table][1][key]
def set(table,key,value = {}):
	if table not in _tables: return False
	_tables[table][1][key] = _tables[table][0](**value)
