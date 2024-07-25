# 本程序仅供学习测试,请勿用于非法用途
# 指路
中间人攻击完整代码以及原理:  
https://github.com/Qmeimei10086/gsm-mitm  
gsm中间人攻击的mobile部分：  
https://github.com/Qmeimei10086/mobile-gsm-mitm  
# 简介
***
本程序是经过修改的OpenBTS rP3.1.3加入了gsm中间人所需的功能  
众所周知,gsm中间人需要伪基站程序和攻击手机,与网上大部分选择OpenBSC作为伪基站程序不同(其实我只见过相关内容两个一个是seeker的采访,一个是来自西安电子科技大学的论文里实现了这种攻击方式)  
我选择了OpenBTS作为伪基站程序,实现了可以获取IMSI和IMEI,以及自定义rand并发送鉴权的功能,并且设计了python程序作为服务端,方便拓展以及与攻击手机交换信息  
另外攻击手机的部分我还没有修改,但本程序已经完全实现了在gsm中间人攻击中伪基站的所有所需的额外功能  

## 添加了如下功能
1.当设备附着时自动发送Identity Request获取imsi和imei  
2.当设备附着时发送设定好rand的Authentication Requests并返回sres  
3.将openbts的sendsms重新改造为再次发送设定好rand的Authentication Requests并返回sres的命令，同时也可正常用来发送短信  

***
# 编译
***
环境:Ubuntu9.04(其实我在Ubuntu20.04也成功编译,不过需改修改很多源文件,我把修改好的也作为Release发布了一个)  
其实没有那么难,只是现在国内的很多教程太老了，所用的文件以及丢失或不适用现在的版本  
首先要换源,因为ubuntu9.04早就不被支持,所以你需要更换旧源,具体过程自己百度  
下面安装编译所需的环境:  
```javascript
apt-get install autoconf libtool libosip2-dev libortp-dev libusb-1.0-0-dev g++ sqlite3 libsqlite3-dev libreadline6-dev libncurses5-dev libsqlite3-dev libreadline6-dev libncurses5-dev
```
过程参考:  
https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458280897&idx=1&sn=694e08910e1e32c1159a8eab34a374b5&chksm=b181534b86f6da5d01eda9cd5ac2c10c4dbd93b3c9197f0c3aaddf06b9e9ea297556f625c66a&scene=27  

http://www.360doc.com/content/14/0415/09/11764545_369096041.shtml  

## 编译顺序:
1.a53  
2.openbts  
3.subscriberRegistry  
```javascript
cd a53 
autoreconf -i 
./configure 
make 
make install 
ldconfig -i 
cd .. 
```
三个的过程都差不多，有的可能不需要那么多步，反正你都敲一遍总不会错（笑）  
只需要编译这三个,上述链接中提到的别的东西一概不需要编译  
## 另一种方式
如果嫌麻烦可以使用我已经编译过的文件,而且包括了所需的.so文件(可能有缺),推荐使用环境Ubuntu16.04/20.04 amd64 
```javascript
cd bin
cp *.so.* /usr/lib
chmod +x ./*
mkdir /etc/OpenBTS
sqlite3 -init OpenBTS.exmaple.sql /etc/OpenBTS/OpenBTS.db ".quit"
sqlite3 -init subscriberRegistry.example.sql /etc/OpenBTS/sipauthserve.db ".quit"
这时候你就可以愉快的修改OpenBTS.db这个配置文件啦
```
***
# 配置OpenBTS
***
```javascript
mkdir /etc/OpenBTS
sqlite3 -init OpenBTS.exmaple.sql /etc/OpenBTS/OpenBTS.db ".quit"
sqlite3 -init subscriberRegistry.example.sql /etc/OpenBTS/sipauthserve.db ".quit"
这时候你就可以愉快的修改OpenBTS.db这个配置文件啦
```
参考  
https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458280897&idx=1&sn=694e08910e1e32c1159a8eab34a374b5&chksm=b181534b86f6da5d01eda9cd5ac2c10c4dbd93b3c9197f0c3aaddf06b9e9ea297556f625c66a&scene=27  
  
***
# 使用
***
为保证该程序也可作为正常基站程序使用，工具人攻击的部分默认关闭  
## 启用中间人攻击
### server.py只是测试功能程序,为您提供一些接口以供开发,并不是gsm中间人攻击的最终server程序!
先运行server.py(python3环境),然后再运行OpenBTS   
运行OpenBTSCLI，输入mitm_open命令即可开启，或者在本目录下创建open_mitm文件    
## 关闭中间人攻击
运行OpenBTSCLI，输入mitm_close命令即可开启，或者删除本目录下open_mitm文件 
## 关于server.py使用教程:
set rand/sres xxx :设置rand和sres  
show rand/sres    :显示rand和sres  
tmsis             :显示注册在伪基站上的用户的imsi和iemi  
auth [IMSI]       :对目标设备发起鉴权,rand为你设置的,默认为aaaabbbbccccddddeeeeffffgggghhhh  
***
# 关于作者
***
bilibili：https://space.bilibili.com/431312664?spm_id_from=333.1007.0.0  
有问题来这里找我，本人已高三，可能不能及时回
***
# 参考:
参考论文：张浩 基于USRP的无线移动通信网络隐蔽定点攻击研究 西安电子科技大学 June 2018  
https://www.doc88.com/p-6314772688570.html?_refluxos=a10  

参考报道：如何利用LTE4G伪基站GSM中间人攻击攻破所有短信验证，纯干货！|硬创公开课  
https://mr.baidu.com/r/1mu2ZKDWZc4?f=cp&u=eaecb9839550917e  

参考视频：GSM中间人攻击演示 科技张工  
https://b23.tv/oMYL3BO  
# Finally:
***
请勿用于非法用途!!!!!!!  
本程序只是试验品,尚未成熟,需要你们自己摸索使用  
~~剩下的攻击手机部分下次再说吧（应该不难实现，不过估计得等到我高三毕业上大学） ！~~  
mobile部分已完成，没想到这么快，竟然在暑假就完成了： 
https://github.com/Qmeimei10086/mobile-gsm-mitm 

我希望能填补网上关于gsm中间人攻击代码的空白。。。。  
