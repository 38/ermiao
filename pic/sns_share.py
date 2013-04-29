# coding: utf-8

# 这个模块用来模拟SNS分享的模块

import msgqueue

def share(**kwargs):
	"""这个函数用来模拟SNS分享的过程,主要的过程全部略去
	   只保留和分享相关的内容"""
	#此处省略
	msgqueue.enqueue({'user': kwargs['user'], 'url': 'http://testurl.....'})

