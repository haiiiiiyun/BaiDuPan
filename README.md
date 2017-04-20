# BaiDuPan 百度网盘自动添加资源脚本

### 项目文件
* baiduspider.py  通过百度分享链接，自动添加资源到网盘
* baiduspider_GUI.py GUI版本
* paidupan.txt    百度网盘分享链接地址


### 说明
* 运行baiduspider.py，将会读取paidupan.txt文件，遍历每一条百度分享链接，自动添加到个人网盘。（需要修改代码，填写自己账号所对应的cookie，代码中的cookie我做了修改已不能用;另外需要修改payload里面的path值，默认为/也就是根目录，后面可跟目录地址，比如说我想保存到网盘的test目录下，对应的写上：/test/）

### Usage
#### baiduspider（Shell版）
```bash
python baiduspider.py --help
```
#### Options
```bash
usage: baiduspider.py [-h] [-filename FILENAME] [-shareurl SHAREURL]
                      [-path PATH] [-cookie COOKIE]

optional arguments:
  -h, --help          show this help message and exit
  -filename FILENAME  name of the file to process
  -shareurl SHAREURL  add your shareurl
  -path PATH          add your baidupan-path
  -cookie COOKIE      add your baidupan-cookie
```

* -h 帮助
* -filename 文件名称，存放百度分享链接。（可选）
* -shareurl 单个百度分享链接。（可选）
* -path     存储的个人网盘路径，缺省为/根目录。（可选）
* -cookie   cookie值（必填）

#### baiduspider（GUI版）
##### 添加单个百度分享链接地址
![](/image/gui_1.png)
运行
![](/image/gui_2.png)
##### 添加百度分享链接文件（批量添加）
![](/image/gui_3.png)
运行
![](/image/gui_4.png)


### 运行效果
![](http://thief.one/upload_image/20170412/22.png)
查看百度网盘：
![](http://thief.one/upload_image/20170412/11.png)

注意：在运行baiduspider.py前，先检查cookie与path，然后查看百度分享地址是否还可用。

详情请参考：[色情资源引发的百度网盘之战|nMask'Blog](http://thief.one/2017/04/12/2/)

@By nMask
20170413
