#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/14
# @Author  : RookieDay
# @Site    : 
# @File    : zhihu_login
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

import re,requests,time,json
from PIL import Image
import http.cookiejar

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
           "Host": "www.zhihu.com",
           "Referer": "https://www.zhihu.com/",
           }
# 建立一个会话，可以把同一用户的不同请求联系起来；直到会话结束都会自动处理cookies
session = requests.Session()
# 建立LWPCookieJar实例，可以存Set-Cookie3类型的文件。
# 而MozillaCookieJar类是存为'/.txt'格式的文件
# 使用登录cookie信息
session.cookies = http.cookiejar.LWPCookieJar('cookie')
# 若本地有cookie则不用再post数据了
try:
    # 从本地加载已存的cookie数据，这样我们就可以携带着cookie（相当于带了一块令牌）访问服务器，服务器核对成功后，就可以访问那些登录后才能访问的页面。
    # 参数ignore_discard = True表示即使cookies将被丢弃也把它保存下来，它还有另外一个参数igonre_expires表示当前数据覆盖（overwritten）原文件
    session.cookies.load(ignore_discard=True)
except IOError:
    print('Cookie未加载！')

def get_xsrf():
    # 获取xsrf
    response = session.get('https://www.zhihu.com', headers=headers)
    html = response.text
    get_xsrf_pattern = re.compile(r'<input type="hidden" name="_xsrf" value="(.*?)"')
    _xsrf = re.findall(get_xsrf_pattern,html)
    return _xsrf[0]

def get_captcha():
    # 获取验证码
    t = str(int(time.time()*1000))
    captcha_url = 'http://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    # 服务器会返回一个json格式的数据若'r'为0则登陆成功若为1可以查看 'msg'得到登陆失败的原因
    response = session.get(captcha_url,headers=headers)
    # 验证码图片保存到本地
    # resp.text返回的是Unicode型的数据。
    # resp.content返回的是bytes型也就是二进制的数据。
    # 也就是说，如果你想取文本，可以通过r.text。
    # 如果想取图片，文件，则可以通过r.content。
    with open('captcha.jpg','wb') as f:
        f.write(response.content)
    # Pillow显示验证码
    img = Image.open('captcha.jpg')
    img.show()
    captcha = input('本次登录需要输入验证码： ')
    return captcha

def login(username,password):
    if re.match(r'\d{11}$',username):
        url = 'http://www.zhihu.com/login/phone_num'
        data = {'_xsrf': get_xsrf(),
                'password': password,
                'remember_me': 'true',
                'phone_num': username
                }
    else:
        url = 'https://www.zhihu.com/login/email'
        data = {'_xsrf': get_xsrf(),
                'password': password,
                'remember_me': 'true',
                'email': username
                }
    # 若不用验证码，直接登录
    result = session.post(url, data=data, headers=headers)
    # 打印返回的响应，r = 1代表响应失败，msg里是失败的原因
    # 其中text以文本形式返回，content以二进制数据形式返回，比如我们请求的网址是图片，就返回content，便可以以wb方式写入文件了。
    # loads可以反序列化内置数据类型，而load可以从文件读取
    # {
    #     "r": 1,
    #     "errcode": 1991829,
    #
    #     "data": {"captcha": "\u9a8c\u8bc1\u7801\u9519\u8bef"},
    #
    #     "msg": "\u9a8c\u8bc1\u7801\u9519\u8bef"
    #
    # }
    # r为1表示登录失败，0
    # 表示登录成功。msg里反映的是登录失败的原因是”验证码会话失效“。

    if (json.loads(result.text))["r"] == 1:
        # 要用验证码，post后登录
        data['captcha'] = get_captcha()
        result = session.post(url, data=data, headers=headers)
        print((json.loads(result.text))['msg'])
        # 保存cookie到本地
    session.cookies.save(ignore_discard=True, ignore_expires=True)

def isLogin():
    # 通过查看用户个人信息来判断是否已经登录
    url = "https://www.zhihu.com/settings/profile"
    # 禁止重定向，否则登录失败重定向到首页也是响应200
    login_code = session.get(url, headers=headers, allow_redirects=False).status_code
    if login_code == 200:
        return True
    else:
        return False

if __name__ == '__main__':
    if isLogin():
        print('您已经登录')
    else:
        account = input('输入账号：')
        secret = input('输入密码：')
        login(account, secret)