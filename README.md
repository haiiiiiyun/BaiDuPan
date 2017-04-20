# BaiDuPan 百度网盘自动添加资源项目

### 说明
本项目用于自动化添加百度分享资源到个人百度网盘，若要成功运行，需要提供个人账户cookie，百度分享链接（无密码），存在密码的百度分享链接，暂时不支持。

### Project List
* baiduspider.py  （Shell版本）
* baiduspider_GUI.py （GUI版本）
* paidupan.txt  （百度网盘分享链接地址文件）

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

![](/image/cmd_1.png)

* -h 帮助
* -filename 文件名称，存放百度分享链接。（可选）
* -shareurl 单个百度分享链接。（可选）
* -path     存储的个人网盘路径，缺省为/根目录。（可选）
* -cookie   cookie值（必填）

#### baiduspider（GUI版）
##### 单个添加百度分享资源
![](/image/gui_1.png)
运行程序
![](/image/gui_2.png)
##### 批量添加百度分享资源
![](/image/gui_3.png)
运行程序
![](/image/gui_4.png)

### screenshot
![](http://thief.one/upload_image/20170412/22.png)
![](http://thief.one/upload_image/20170412/11.png)

### ResultStatus
* 0  ADD SUCCESS
* 12 ALREADY EXISTS
* otherstatus cookie or path or shareurl have error


详情请参考：[色情资源引发的百度网盘之战|nMask'Blog](http://thief.one/2017/04/12/2/)


@By nMask
20170413

更新于20170420---增加GUI版。
