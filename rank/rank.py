#coding=utf8
import db
import config
#在这里需要用优先队列实现一个猫、狗、其他动物的排行榜，这里省略，如果考虑性能可以用Ｃ来写这一块
class RankList:
	def GetItem(self): pass #获得随机的一个排行榜中的元素
	def Update(self, item): pass #更新排行榜(淘汰表现不好的元素，把新的热门图加进来)
catlist = RankList()
doglist = RankList()
otherlist = RankList()

def GetItemFromList(lst,N):
	ret = []
	for i in xrange(0,N):
		ret.append(lst.GetItem())
	return ret
def GetItemFromDb(type,hotlist,N):
	ret = []
	for i in xrange(0,N):
		item = None
		while True:
			item = GetRandomItemFromDB(type)
			if item not in hotlist : break
		ret.append(item)
	return ret
def GetItems(N):
	"在第一页显示Ｎ个元素"
	dbcat = N * config.cat * (100 - config.cat_hot) / 10000
	lscat = N * config.cat * conf.cat_hot / 10000

	dbdog = N * config.dog * (100 - config.dog_hot) / 10000
	lsdog = N * config.dog * conf.dog_hot / 10000

	dbother = N * config.other * (100 - config.other_hot) / 10000
	lsother = N * config.other * conf.other_hot / 10000

	tmp = [ ('Cat', dbcat, catlist, lscat),
			('Dog', dbdog, doglist, lsdog),
			('Other', dbcat, catlist, lscat)]
	ret = []
	for name,dbc,lst,lsc in tmp:
		hot = GetItemFromList(lst,lsc)
		dbs = GetItemFromDb(name,hot,dbc)
		ret += hot + bds
	
	randomize_seq(ret) #随机打乱序列
	return ret
