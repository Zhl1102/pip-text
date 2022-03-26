第一次使用python创建一个pip包

1.配置pip包的配置
mkdir package_name
cd package_name
添加初始化文件__init__.py
添加一个requirements.txt
修改配置文件setup.py
2.编写package代码
(1)新建文件夹
(2)添加初始化文件__init__.py
(3)创建package包文件，编写代码
3.上传到github仓库
4.创建一个releases版本
5.到环境下使用pip install -e git+https://github.com/Zhl1102/pip-text.git#egg=hello_world 命令安装
