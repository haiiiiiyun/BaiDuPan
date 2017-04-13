# BaiDuPan
百度网盘自动添加资源脚本

### 项目文件
* mp4paspider.py  抓取mp4pa网站爬虫，用来获取百度网盘分享链接以及torrent地址
* baiduspider.py  通过百度分享链接，自动添加资源到网盘
* paidupan.txt    抓取到的百度网盘分享链接地址
* torrent.txt     抓取到的torrent链接地址

### Usage
* 运行mp4paspider.py文件，可生成paidupan.txt与torrent.txt文件。（可通过修改代码中range()）范围，指定要爬取的页面范围。
* 运行baiduspider.py，将会读取paidupan.txt文件，遍历每一条百度分享链接，自动添加到个人网盘。（需要修改代码，填写自己账号所对应的cookie，代码中的cookie我做了修改已不能用;另外需要修改payload里面的path值，默认为/也就是根目录，后面可跟目录地址，比如说我想保存到网盘的test目录下，对应的写上：/test/）

注意：在运行baiduspider.py前，先检查cookie与path，然后查看百度分享地址是否还可用。

详情请参考：[色情资源引发的百度网盘之战|nMask'Blog](http://thief.one/2017/04/12/2/)

@By nMask
20170413
