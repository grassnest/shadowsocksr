# ShadowsocksR Server for WHMCS

# 背景

    2014年前后开始接触Shadowsocks，当时只是下载Windows客户端，然后每天上网找免费账号，一年后在Google+上偶然看到了Alpharacks $2.99/年
    的 OpenVZ 架构的VPS，自此开始研究自己搭建服务器，从单用户到基于ss-panel的多用户版，去年底开始尝试whmcs版的多用户版，新近又入手几个
    便宜的KVM VPS，经过对比打算使用ShadowsocksR，基于[破瓦匠](https://github.com/shadowsocksr/shadowsocksr)的多用户版本进行修改，
    基于Whmcs API与数据库进行交互
    
# 说明
    
    源代码基础上新增了两个文件
    whmcs.py
    config.py
    
    修改了db_transfer.py
    
# 部署

    参考原版部署说明，之后在config.py里设置whmcs api的地址，用户名和密码
    一定要将VPS的IP地址放在WHMCS的服务器白名单中，否则无法成功连接
