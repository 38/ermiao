# coding: utf-8
# 由于不知道数据存储的方式,所以用这种方式
# 模拟一个SNS分享URL的队列
# 如果实际需要,这部分可以换做实际和数据存储方式适应的实现

# 在这里之考虑有一个admin的情况, 如果有多个admin, 则考虑在一定时间内记录所有的
# 分享记录

__queue__ = []

enqueue = __queue__.append

top = lambda N: __queue__[:min(len(__queue__),N)]

