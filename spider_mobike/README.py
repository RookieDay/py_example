#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/17
# @Author  : RookieDay
# @Site    : 
# @File    : README
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition


# 手机代理 以手机端摩拜小程序请求为例
# 参考 xlzd的回答 强烈推荐
# https://www.zhihu.com/question/53141781/answer/260874988?utm_medium=social&utm_source=wechat_session

# 官网：http://anyproxy.io
# 配置参考1 http://aiezu.com/article/windows_anyproxy_install.html
# 配置参考2：https://www.cnblogs.com/yoable/p/6374134.html
# 配置参考3：http://blog.csdn.net/lilongsy/article/details/74161851
# request.png / response.png 查看效果截图
# response_data.json 下载下来的部分json数据


# 使用AnyProxy 手机代理进行抓包
# 参考网址http://anyproxy.io/cn.html
# 环境 python3.5 、win7 x64、iPhone、node

# 1. 安装AnyProxy(需要提前安装好nodejs)
# npm install -g anyproxy@beta #本文档对应的AnyProxy为4.0Beta版
# 2. 命令行启动AnyProxy，默认端口号8001
# anyproxy
# 启动后将终端http代理服务器配置为127.0.0.1:8001即可
# 访问http://127.0.0.1:8002 ，web界面上能看到所有的请求信息
# 点击Filter 设置为 ： http://mobike.com
# 打开后点击RootCA 下载证书到本地 安装证书 (具体配置可以点击这里 http://anyproxy.io/cn.html#配置帮助)
# windows下双击证书安装

# 3. cmd下输入ip config 查看笔记本IPv4地址
#
# 4. 打开手机浏览器 输入http://ip:8002/fetchCrtFile (ip为第三步中的)  进而手机端安装证书
#
# 5. 安装证书成功以后
# iphont -- 设置 - 通用 - 关于本机 - 证书信任设置 - AnyProxy 打开 (见图02.jpg)
#
# 6. 手机wifi设置中，手动设置http代理，在服务器中输入安装上面的代理IP，端口输入8001，保存即可 (见图03.png)

# 7. 打开微信小程序 即可在网页看到我们的请求 对应的查看数据