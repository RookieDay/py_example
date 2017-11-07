#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/7
# @Author  : RookieDay
# @Site    : 
# @File    : README
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

# windows virtualenv
# 在开发Python应用程序的时候，系统安装的Python3只有一个版本：3.4。所有第三方的包都会被pip安装到Python3的site-packages目录下。
# 如果我们要同时开发多个应用程序，那这些应用程序都会共用一个Python，就是安装在系统的Python 3。如果应用A需要jinja 2.7，而应用B需要jinja 2.6怎么办？
# 这种情况下，每个应用可能需要各自拥有一套“独立”的Python运行环境。virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。

# pip install virtualenv
# mkdir myproject
# cd myproject/
# 创建一个独立的Python运行环境，命名为venv
# virtualenv --no-site-packages venv
# 命令virtualenv就可以创建一个独立的Python运行环境，我们还加上了参数--no-site-packages，这样，已经安装到系统Python环境中的所有第三方包都不会复制过来，这样，我们就得到了一个不带任何第三方包的“干净”的Python运行环境。
# windows 进入创建的venv--> Scripts 文件夹，命令行直接执行activate即可，然后
# 命令提示符变了，有个(venv)前缀，表示当前环境是一个名为venv的Python环境。
# (venv)[你的目录]:myproject michael$
# 然后正常安装各种第三方包，并运行python命令

# 在venv环境下，用pip安装的包都被安装到venv这个环境下，系统Python环境不受任何影响。也就是说，venv环境是专门针对myproject这个应用创建的。
# 退出当前的venv环境，使用deactivate命令

# 完全可以针对每个应用创建独立的Python运行环境，这样就可以对每个应用的Python环境进行隔离。
# virtualenv是如何创建“独立”的Python运行环境的呢？原理很简单，就是把系统Python复制一份到virtualenv的环境，
# 用命令执行文件夹下activate进入一个virtualenv环境时，virtualenv会修改相关环境变量，让命令python和pip均指向当前的virtualenv环境。


from flask import Flask
# 如果你使用单一的模块（如本例），你应该使用 __name__ ，因为模块的名称将会因其作为单独应用启动还是作为模块导入而有不同（ 也即是 '__main__' 或实际的导入名）。这是必须的，这样 Flask 才知道到哪去找模板、静态文件等等。
app = Flask(__name__)

@app.route('/')
def hello_word():
    return 'hello ana oo word'

# 如果你使用单一的模块（如本例），你应该使用 __name__ ，因为模块的名称将会因其作为单独应用启动还是作为模块导入而有不同（ 也即是 '__main__' 或实际的导入名）。这是必须的，这样 Flask 才知道到哪去找模板、静态文件等等。
if __name__ =='__main__':
    app.run(debug=True)

