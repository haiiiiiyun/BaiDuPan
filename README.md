# BaiDuPan 百度网盘自动添加资源项目

### 说明
本项目用于自动化添加百度分享资源到个人百度网盘，若要成功运行，需要提供个人账户cookie，百度分享链接（无密码），存在密码的百度分享链接，暂时不支持。目前项目分为Shell版与GUI版本，GUI目前仅限windows下运行，Shell版任何平台都可以。

### Project List
* baiduspider.py  （Shell版本）
* baiduspider_GUI.py （GUI版本）
* paidupan.txt  （百度网盘分享链接地址文件）

### Usage
```bash
git clone https://github.com/tengzhangchao/BaiDuPan.git
```
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
##### 依赖
* gooey
* wxpython

```bash
pip install gooey
```
wxpython请从官网编译安装，或者使用
```bash
pip install wxpython
```

### screenshot
![](http://thief.one/upload_image/20170412/11.png)

### ResultStatus
* 0  （ADD SUCCESS）
* 12 （ALREADY EXISTS）
* otherstatus （cookie or path or shareurl have error）

有问题可以在Issues中留言。


详情请参考：[色情资源引发的百度网盘之战|nMask'Blog](http://thief.one/2017/04/12/2/)


@By nMask
2017.04.13

更新于2017.04.20---增加GUI版
更新于2017.05.09---修改GUI为中文版   By  cxgreat2014
