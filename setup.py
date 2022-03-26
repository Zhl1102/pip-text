#! /usr/bin/env python
# -*- coding: utf-8 -*_
# Author: ***<***gmail.com>
from distutils.core import setup
import setuptools

setup(
    name='first_pip', # 包的名字
    version='1.0.1',  # 版本号
    description='pip text',  # 描述
    author='watermelon', # 作者
    author_email='1533938229@qq.com',  # 你的邮箱**
    url='https://github.com/Zhl1102',  # 可以写github上的地址，或者其他地址
    packages=setuptools.find_packages(exclude=['test', 'examples', 'script', 'tutorials']),  # 包内不需要引用的文件夹
    
    # 依赖包
    install_requires=[
        'numpy',
        'torchvision',
        'flask'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: MacOS'  # 你的操作系统
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # BSD认证
        'Programming Language :: Python',   # 支持的语言
        'Programming Language :: Python :: 3',  # python版本 。。。
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    zip_safe=True,
)