@echo off
echo 更改pip源为清华镜像...

echo 在user目录下创建pip文件夹...
md "C:\Users\pip"

cd C:\Users\pip

echo 创建pip.ini文件
echo=> pip.ini

echo [global] >> pip.ini
echo. >> pip.ini
echo index-url = https://pypi.tuna.tsinghua.edu.cn/simple >> pip.ini

echo 开始安装依赖

goto start
在下面添加想要安装的依赖
:start

pip install numpy
pip install matplotlib
echo 依赖安装完成
PAUSE
