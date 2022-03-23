#! /usr/bin/env python
# -*- coding: utf-8 -*_
# Author: ***<***gmail.com>
from distutils.core import setup
import setuptools

setup(
    name='hello_world', # 包的名字
    version='0.0.1',  # 版本号
    description='project describe',  # 描述
    author='watermelon', # 作者
    author_email='1533938229@qq.com',  # 你的邮箱**
    url='https://github.com/Zhl1102',  # 可以写github上的地址，或者其他地址
    packages=setuptools.find_packages(exclude=['test', 'examples', 'script', 'tutorials']),  # 包内不需要引用的文件夹
    
    # 依赖包
    install_requires=[]
)