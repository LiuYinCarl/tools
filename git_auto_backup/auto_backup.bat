@echo off
if "%1" == "h" goto begin 
mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit 
:begin 

REM 设置延时为5分钟
set delay1 = 300
REM 设置延时为两小时
set delay2 = 7200

REM 延时5分钟开始第一次备份，主要是防止没有刚开机没有联网
timeout 300

REM 强制关闭上个开启的进程
REM taskkill /f /t /im auto_backup.exe
F:
cd F:\git_auto_backup
REM 对repo.txt文件里面的github项目进行备份
for /f "tokens=1,* delims="  %%p in (repo.txt)  do (
    cd %%p
    git add .
    git commit -m "auto backup"
    git push origin master
)

