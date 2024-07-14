# 本程序仅供学习测试,请勿用于非法用途
# 简介
***
本程序是经过修改的OpenBTS rP3.1.3加入了gsm中间人所需的功能  
众所周知,gsm中间人需要伪基站程序和攻击手机,与网上大部分选择OpenBSC作为伪基站程序不同(其实我只见过相关内容两个一个是seeker的采访,一个是来自西安电子科技大学的论文里实现了这种攻击方式)  
我选择了OpenBTS作为伪基站程序,实现了可以获取IMSI和IMEI,以及自定义rand并发送鉴权的功能,并且设计了python程序作为服务端,方便拓展以及与攻击手机交换信息  
另外攻击手机的部分我还没有修改,但本程序已经完全实现了在gsm中间人攻击中伪基站的所有所需的额外功能  
***
# 编译
***
环境:Ubuntu9.04  
首先要换源,因为ubuntu9.04早就不被支持,所以你需要更换旧源,具体内容自己百度  
下面安装编译所需的环境:  
｀｀｀
apt-get install autoconf libtool libosip2-dev libortp-dev libusb-1.0-0-dev g++ sqlite3 libsqlite3-dev erlang libreadline6-dev libncurses5-dev libsqlite3-dev erlang libreadline6-dev libncurses5-dev  
｀｀｀
过程参照:  
https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458280897&idx=1&sn=694e08910e1e32c1159a8eab34a374b5&chksm=b181534b86f6da5d01eda9cd5ac2c10c4dbd93b3c9197f0c3aaddf06b9e9ea297556f625c66a&scene=27  
http://www.360doc.com/content/14/0415/09/11764545_369096041.shtml  
***
编译顺序:
***
1 a53  
2 openbts  
3 subscriberRegistry  
只需要编译这三个,上述链接中提到的一概不需要编译  
如果嫌麻烦可以使用我已经编译过的文件,而且包括了所需的.so文件(可能有缺),推荐使用环境Ubuntu16.04 amd64  
***
# 配置
***
参照  
https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458280897&idx=1&sn=694e08910e1e32c1159a8eab34a374b5&chksm=b181534b86f6da5d01eda9cd5ac2c10c4dbd93b3c9197f0c3aaddf06b9e9ea297556f625c66a&scene=27  
只需要初始化openbts和subscriberRegistry的两个sql文件即可  
***
# 使用
***
先运行server.py(python3环境),然后在运行OpenBTS  
## 关于server.py使用教程:
set rand/sres xxx :设置rand和sres  
show rand/sres    :显示rand和sres  
tmsis             :显示祖册在伪基站上的用户的imsi和iemi  
auth [IMSI]       :对目标设备发起鉴权,rand为你设置的,默认为aaaabbbbccccddddeeeeffffgggghhhh  
***
# 关于作者
***
bilibili：https://space.bilibili.com/431312664?spm_id_from=333.1007.0.0  
有问题来这里找我  
***
# Finally:
***
请勿用于非法用途!!!!!!!  
本程序只是试验品,尚未成熟,需要你们自己摸索使用  
剩下的攻击手机部分下次再说吧！  
我希望能填补网上关于gsm中间人攻击代码的空白。。。。  
