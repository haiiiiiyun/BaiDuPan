#! -*- coding:utf-8 -*-

'''
操作百度网盘，自动添加资源到网盘。
注意点：
爬取源码可以使用urllib2模块，不需要使用phantomjs，因为不需要执行js。
* 获取cookie（可以手动登录然后抓包获取）
* 首先爬取如：http://pan.baidu.com/s/1o8LkaPc页面，获取源码
* 解析源码，筛选出该页面分享资源的名称、shareid、from（uk)、bdstoken、appid（app_id）。
* 构造post包（用来添加资源到网盘），该包需要用到以上4个参数，当然还有一个最重要的就是cookie

在post包的url中还有一个logid参数，内容可以随便写，应该是个随机值然后做了base64加密。
在post包的payload中，filelist是资源名称，格式filelist=["/name.mp4"]，path为保存到那个目录下，格式path=/pathname
'''
__author__="nMask"
__Blog__="http://thief.one"
__Date__="20170412"

import re
import urllib2
import urllib
import json

res_content=r'"app_id":"(\d*)".*"uk":(\d*).*"bdstoken":"(\w*)".*"shareid":(\d*)'  #正则，获取参数值
res_title=r"<title>([^_]*)_.*</title>"  #正则，获取资源名称
headers = {
    'Host':"pan.baidu.com",
    'Accept':'*/*',
    'Accept-Language':'en-US,en;q=0.8',
    'Cache-Control':'max-age=0',
    'Referer':'https://pan.baidu.com/s/1kUOxT0V?errno=0&errmsg=Auth%20Login%20Sucess&&bduss=&ssnerror=0&',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Cookie':''
}
#cookie要手动获取添加。

class bdpanSpider:
	def __init__(self):
		self.p_t=re.compile(res_title)
		self.p=re.compile(res_content)

	def run(self,url):
		self.getbody(url)  ##获取源码并分析
		self.addziyuan()   ##添加资源到网盘

	def getbody(self,url):
		'''
		获取分享页面源码
		'''
		try:
			req=urllib2.Request(url,headers=headers)
			f=urllib2.urlopen(req)
			content=f.read()
		except Exception,e:
			print "[Error]",str(e)
		else:
			'''
			从源码title提取分享的资源名称
			'''
			L_t=self.p_t.findall(content)
			if len(L_t)>0:
				self.title=L_t[0]
			else:
				self.title=""
			print "[Info]Title:",self.title
			'''
			从源码中提取资源的一些参数
			'''
			L=self.p.findall(content)
			if len(L)>0:
				self.app_id=L[0][0]
				self.uk=L[0][1]
				self.bdstoken=L[0][2]
				self.shareid=L[0][3]
			else:
				self.app_id=""
				self.uk=""
				self.bdstoken=""
				self.shareid=""

	def addziyuan(self):
		'''
		添加该资源到自己的网盘
		'''
		url_post="https://pan.baidu.com/share/transfer?shareid="+self.shareid+"&from="+self.uk+"&bdstoken="+self.bdstoken+"&channel=chunlei&clienttype=0&web=1&app_id="+self.app_id+"&logid=MTQ5MjA0ODExOTE0NTAuNjg1ODk3MTk4ODIyNDE2Mw=="
		payload="filelist=%5B%22"+urllib.quote("/"+self.title)+"%22%5D&path=%2F" #资源名称与要保存的路径
		print "[Info]Url_Post:",url_post
		print "[Info]payload:",payload
		try:
			req=urllib2.Request(url=url_post,data=payload,headers=headers)
			f=urllib2.urlopen(req)
			result=json.loads(f.read())
			tag=result["errno"]
			print tag
			if tag==0:
				print "[Result]Add Success"
			elif tag==12:
				print "[Result]Already Exist"
			else:
				print "[Result]Have Error"
		except Exception,e:
			print "[Error]",str(e)


if __name__=="__main__":
	
	cur=bdpanSpider()
	cur.run("https://pan.baidu.com/s/1o8lJVOe")

	'''
	从文件中读取百度分享链接，自动化添加到自己的网盘当中。
	'''
	# f=open("baidu_pan.txt","r")
	# url_list=f.readlines()

	# cur=bdpanSpider()

	# for url in url_list:
	# 	url=url.strip("\n")
	# 	cur.run(url)
	# 	print "************************"


