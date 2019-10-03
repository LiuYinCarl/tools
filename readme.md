项目简介

本项目主要收集平时写的一些小工具, 欢迎改进

---

## git_auto_backup

### 使用介绍

- 此工具主要用来将git项目每次开机自动备份

### 使用环境

- windows

### 使用方法

- 将auto_backup.bat文件放置到Windows开机启动文件夹 C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp

- 将自己本机的git项目地址放在 repo.txt 文件中，项目最好放置在F盘中，否则需要更改批处理文件（bat文件）
- 阅读bat文件，根据文件中注释结合实际情况进行更改

### 使用前提

- 电脑上安装了git

- 需要备份的库已经在github上存在，或者是直接克隆的最好

- git 已经配置，否则需要配置

- - 配置方法（配制git登录名和邮箱）

  - ```git
     git config --global user.name "John Doe"
     git config --global user.email johndoe@example.com
    ```

------

## python安装依赖.bat

### 使用介绍

- 此工具用于给pip 换成国内源以及批量安装库

### 使用环境

- Windows

### 使用方法

- 根据bat文件内注释，添加想要安装的库
- 添加格式 pip install 你想安装的库
- 完成上述两条后以管理员权限执行该批处理文件

### 使用前提

- 电脑上安装了python, pip

---

## recite_words

### 使用介绍

- 此工具是一个命令行的背单词小工具

### 使用环境

- Windows, Linux

### 使用方法

- python recite_words.py 启动

#### 功能介绍

```
    '<>' express you need to add a argument here. such as 
            command:add apple 苹果
    help:                       print help info
    all:                        show all words 
    info:                       show statistics
    next:                       show next word
    quit:                       quit
    import:                     import words from file
    export:                     export words into file 
    add <word> <translation>:   add a word and it's translation
    del <word> <translation>:   delete a word
    mod <word> <translation>:   modify word's translation
    auto_cls <on/off>:          open/close auto clear screen
    search <word>:              search word in word table

```
### 使用前提

- 安装了python 和 PrettyTable 包






















