@echo off
echo ����pipԴΪ�廪����...

echo ��userĿ¼�´���pip�ļ���...
md "C:\Users\pip"

cd C:\Users\pip

echo ����pip.ini�ļ�
echo=> pip.ini

echo [global] >> pip.ini
echo. >> pip.ini
echo index-url = https://pypi.tuna.tsinghua.edu.cn/simple >> pip.ini

echo ��ʼ��װ����

goto start
�����������Ҫ��װ������
:start

pip install numpy
pip install matplotlib
echo ������װ���
PAUSE
