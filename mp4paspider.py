#! -*- coding:utf-8 -*-

__author__="nMask"
__Blog__="http://thief.one"
__Date__="20170412"

import gevent
from gevent import monkey, pool
monkey.patch_all()
import urllib2
import re


url="http://www.mp4pa.com/mp4/hd"
res=r'<a href="(http://www\.mp4pa\.com/bt4/[^"]*)".*<a href="(http://pan\.baidu\.com/[^"]*)"'
p=re.compile(res,re.DOTALL)

f1=open("baidu_pan.txt","a")
f2=open("torrent.txt","a")


def getbaiduurl(i):
	'''
	获取网页源码，并提取出百度网盘地址
	'''
	urls=url+str(i)+".html"
	try:
		f=urllib2.urlopen(urls)
		content=f.read()
	except Exception,e:
		print str(e)
	else:
		L=p.findall(content)

		print L

		if len(L)>0:
			if len(L[0])>1:
				f1.write(L[0][1]+"\n")
				f2.write(L[0][0]+"\n")
				print i,L[0][0],L[0][1]
			else:
				f1.write(L[0][0]+"\n")
				print i,L[0][0]
		else:
			print i


po = pool.Pool(10)
jobs=[]
for i in range(4000,5000):
    jobs.append(po.spawn(getbaiduurl, i))
gevent.joinall(jobs)

f.close()