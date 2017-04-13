# BaiDuPan
百度网盘自动添加资源脚本

### 项目文件
* mp4paspider.py  抓取mp4pa网站爬虫，用来获取百度网盘分享链接以及torrent地址
* baiduspider.py  通过百度分享链接，自动添加资源到网盘
* paidupan.txt    抓取到的百度网盘分享链接地址
* torrent.txt     抓取到的torrent链接地址

### Usage
* 运行mp4paspider.py文件，可生成paidupan.txt与torrent.txt文件。（可通过修改代码中range()）范围，指定要爬取的页面范围。
* 运行baiduspider.py，将会读取paidupan.txt文件，遍历每一条百度分享链接，自动添加到个人网盘。（需要修改代码，填写自己账号所对应的cookie，代码中的cookie我做了修改已不能用）

详情请参考：[色情资源引发的百度网盘之战|nMask'Blog](http://thief.one/2017/04/12/2/)

@By nMask
20170413
