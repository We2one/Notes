### Linux 系统

+ #### 文件操作命令 : 主要用于文件/目录的管理, 包含文件/夹的创建、重命名以及删除, 文件/目录的复制、剪贴等操作
    + echo : 信息打印展示
    + touch : 创建文件
    + cp : 复制文件
    + mv : 移动文件
    + mkdir (-p) : (-p 创建级联文件夹) 创建文件夹
    + rm : 删除文件
        + -r : 递归删除指定路径中的所有文件/目录
        + -f : 忽略文件提醒,直接删除
        + rm -rf * : 删除当前目录中所有文件 ***慎用***
        + rm -rf / : 删除根目录 ***慎用***
    
+ #### 压缩解压命令 : 压缩解压操作一般称为文件归档
    + tar : 文件归档, 可以将多个文件打包成一个文件,也可以将打包的文件拆分成多个文件
        + tar -cvf 文件名.tar file1 file2 file... : 将多个文件打包成 文件名.tar 文件
        + tar -tvf 文件名.tar : 查看 文件名.tar 包文件中包含的文件列表
        + tar -xvf 文件名.tar : 将 文件名.tar 包中的文件释放到当前目录
    + gzip : 文件 .gz 格式压缩, 按比例将文件进行压缩,通常与 tar 归档命令一起使用,将文件归档为一个tar包然后进行压缩 (不能压缩目录)
        + gzip 文件名.tar : **压缩** tar 包文件
        + tar -zcvf 文件名.tar.gz file1 file2 ... : **压缩拓展**
        + gzip -d 文件名.tar.gz 或者 gunzip 文件名.tar.gz : **解压缩为 tar 包**
        + tar -zxvf 文件名.tar.gz : **解压缩出新的文件而非tar包**
    + bzip2 : 文件 .bz 格式压缩
        + bzip2 -k 文件名.tar : **压缩**,后缀为 .tar.bz2
        + bzip2 -d 文件名.tar.bz2 : 或者 bunzip2 文件名.tar.bz2 : **解压缩**
    + zip : 文件 .zip 格式压缩,通用压缩,主要用于windows操作系统平台之间的通用压缩格式
        + zip -r [压缩后的文件名称] [要压缩文件] : **压缩**, -r 指定可以压缩目录
        + unzip 压缩文件 : **解压缩**
    + xz : 文件 .xz 格式压缩,通常与 tar 归档命令一起使用
        + xz -z 归档文件名.tar : **压缩**
        + tar -Jcf 归档文件.tar.xz file1 file2 ... : **压缩拓展**
        + xz -d 归档文件.tar.xz : **解压缩**
        + tar -Jxf 归档文件名.tar.xz : **解压缩拓展**
    
+ #### 权限管理命令
    + ls -al 或 ll -a 查看到的文件
        ```
        drwx------. 15 angleliuliu angleliuliu 4096 9月   4 09:12 .
        drwxr-xr-x.  3 root        root          25 9月   3 15:28 ..
        -rw-------.  1 angleliuliu angleliuliu  358 9月   3 20:04 .bash_history
        -rw-r--r--.  1 angleliuliu angleliuliu   18 10月 31 2018 .bash_logout
        --. 15 angleliuliu angleliuliu 4096 9月   3 17:31 .cache
        drwxr-xr-x. 14 angleliuliu angleliuliu  261 9月   3 17:26 .config
        drwx------.  3 angleliuliu angleliuliu   25 9月   3 15:32 .dbus
        -rw-------.  1 angleliuliu angleliuliu   16 9月   3 15:32 .esd_auth
        drwx------.  3 angleliuliu angleliuliu   19 9月   3 15:32 .local
        drwxr-xr-x.  4 angleliuliu angleliuliu   39 9月   3 15:15 .mozilla
      ```
        + d / - / l : 文件性质
            + \- : 表示文件
            + d : 表示目录
            + l : 表示符号链接
        + rw- / rwx : 当前用户权限
            + r : 可读权限
            + w : 可写权限
            + x : 执行权限
        + r-- / r-x : 当前用户所属组操作文件的权限
        + r-- / r-x : 当前系统其他用户操作文件权限
        + 15 / 3 / 1 : 文件个数; 文件的话为 1, 目录的话为目录中文件的个数
        + angleliuliu / root : 文件所属用户
        + 4096 / 25 : 文件大小; 单位 "字节"
        + 9 月 / 10 月 : 文件创建日期
        + .config / .local : 文件名称
    
    + 文件可读性、可写以及执行权限,三种权限对应二进制与十进制 (十进制表示在进行文件权限操作时十分方便)
      
        权限 | r 可读 | w 可写 | x 执行 | 十进制表示
        :---: | :---: | :---: | :---: | :---: 
        可读 | 1      | 0     | 0     | 4
        可写 | 0      | 1     | 0     | 2
        可执行 | 0     | 0     | 1     | 1
        可读可写 | 1    | 1     | 0     | 6
        读写执行 | 1    | 1     | 1     | 7     
        
        ```
      chmod 744 test.txt
      # 直接修改文件访问权限
      # 7 = 4 + 2 + 1 == r + w + x  : 赋予 user 当前用户权限
      # 4 == r  : 赋予 group 用户组权限
      # 4 == r  : 赋予 other 其他用户权限
      ```
    
+ #### 用户管理命令 (Linux/Unix 系统超级管理员 root 可以创建多个管理员用户或者普通用户,不同用户可以同时远程登录系统各自独立完成任务，做到多用户多任务操作) 
  
    1. useradd : root 用户在系统中创建用户
        + 语法格式 : Usage:useradd -D [options]
    
    2. userdel : root 用户在系统中删除用户
        + 语法格式 : Usage:userdel [options] LOGIN
            -r, --remove : 删除 home 目录 和 假脱机邮件
        
    3. passwd : 修改用户密码
        + 语法格式 : Usage:passwd [OPTION...]<accountName>
            + -d, --delete : root 用户删除此用户名用户的密码
            + -l, --lock : root 用户 锁定此用户名用户密码
            + -u, --unlock : root 用户 解锁此用户名用户密码
            + -e, --expire : root 用户 失效此用户名用户密码
    
+ #### 系统管理命令 (针对系统进行查看、配置以及维护的操作命令,类似于 windows 系统的任务管理器)

    1. free : 查看系统内存信息
        + free : 直接查看当前计算机中内存使用情况
        + free -h : 更友好, 方便人查看的方式展示内存使用
        
    2. df : 查看系统存储信息
        + df : 查看当前系统的磁盘使用情况
        + df -h : 更友好, 方便人查看的方式展示当前系统的磁盘使用情况
    
    3. top : 查看当前系统所欲工作进程信息
       
    4. ps : 进程管理命令,查看和检索指定的进程信息
        + a : 显示一个终端所有进程
        + x : 显示没有控制终端的进程
        + u uid / username : 选择有效的用户 id 或者用户名
            ```
          ps u 18600
          """
          USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
          angleli+  18600  0.0  0.1 317964  3520 ?        Sl   09:13   0:00 /usr/libexec/gvfsd-me
          """
          ```
        + f : 全部列出,通常与其它选项共用
        + e : 命令之后现实环境
        + ps aux | sort -rnk 4 : 按内存资源的使用量对进程进行排序
        + ps aux | sort -nk 3 : 按 CPU 资源的使用量对进程进行排序
        + ps -aux | grep python : 查看 python 进程是否已启用
            + USER : 用户名
            + PID : 进程 ID (Process ID)
            + %CPU : 进程 CPU 占用率
            + %MEM : 进程 内存 占用率
            + VSZ : 进程所使用的虚拟内存大小 (Virtual Size)
            + RSS : 进程使用驻留集大小或者实际内存大小, Kbytes 字节
            + TTY : 与进程关联的终端 (tty)
            + STAT : 进程的状态 (进程状态使用字符表示的 STAT 状态码)
            + TIME : 进程使用的总 CPU 时间
            + COMMAND : 正在执行的命令行命令
        
    5. kill : 结束指定的进程
        + kill 进程id : 结束指定编号的进程
        + kill -9 进程id : 强制杀死指定编号的进程
    
+ #### 软件管理命令
    + Ubuntu 包管理工具 apt-get
    
    1. rpm : RPM 软件包的管理工具.(遵循 GPL 规则)
        + rpm -ivh xxx.rpm : 安装 rpm 包
        
        + rpm -e xxx : 卸载 rpm 包
        
        + rpm -qa : 列出所有安装过的包
        
    3. yum  : 在 Fedora 和 RedHat 以及 SUSE 中基于 rpm 的软件包管理器,可以使系统管理人员交互和自动化地更新与管理 RPM 软件包，
        能够从指定的服务器自动下载 RPM 软件包并安装, 可以自动处理依赖性关系,并且一次安装所有依赖的软件包,无需繁琐一次次下载安装
        
        1. 安装操作
            + yum install : 全部安装
            + yum install package1 : 安装指定的安装包 package1
            + yum groupinstall group1 : 安装程序组 group1
            
        2. 更新操作
            + yum update : 全部更新
            + yum update package1 : 更新指定程序包 package1
            + yum check-update : 检查可更新的程序
            + yum upgrade package1 : 升级指定程序包 package1
            + yum groupupdate group1 : 升级程序组 group1
            
        3. 查找操作
            + yum info package1 : 显示安装包信息 package1
            + yum list : 显示所有已安装和可以安装的程序包
            + yum list package1 : 显示指定程序包 package1 安装情况
            + yum groupinfo group1 : 显示程序组 group1 信息 yum search string 根据关键字 string 查找安装包
            + yum search <keyword> : 查找软件包
            
        4. 删除程序
            + yum remove <package_name> : 删除指定名程序包
            + yum groupremove group1 : 删除程序组 group1
            + yum deplist package1 : 查看程序 package1 依赖情况
            
        5. 清除缓存
            + yum clean packages : 清除缓存目录下的软件包
            + yum clean headers : 清除缓存目录下的 headers
            + yum clean oldheaders : 清除缓存目录下旧的 headers
            
### vim 编辑器

+ #### 文本查看命令
    1. more 分页查看
        + more file : 分页查看文件内容
        + more +n file : 设定从第 n 行开始显示 file 内容
        + more +/string file : 从包含 string 的前两行开始展示
        + 操作方式
            + 空格 : 向下滚动一页内容
            + 回车 : 向下滚动一行内容
            + b : 向上滚动一页内容 back
            + q : 退出浏览 quit
            + = : 展示当前行号
            + :f : 展示当前文件名和当前行号
    2. cat 全文浏览
        + cat file : 全文本浏览
        + cat -n file : 带行号全文本浏览
        + cat file1 file2 > file : 合并文件
        + tac filename : 倒序浏览文本内容
    3. head 头部浏览,默认查看 10 行
        + head -n 100 file : 显示 file 文件前 100 行内容
        + head -n -100 file : 显示 file 文件后 100 行内容
    4. tail 尾部浏览,默认查看 10 行
        + tail -100 file : 显示最后 100 行内容
        + tail -n +100 file : 从第 100 行开始显示 file 内容
        + tail -100f file : 显示最后 100 行内容,并持续监控文件内容
    5. less 分页浏览，类似于 more 命令
        + less file : 分页浏览 file
        + less -N file : 分页浏览 file，并展示行号
        + less -m file : 分页浏览 file，并展示百分比
        + 操作方式
            + f : 向前滚动一页
            + b : 向后滚动一页
            + j | 回车 : 向前滚动一行
            + k : 向后滚动一行
            + G : 移动到最后一行
            + g : 移动到第一行
            + /string : 向下搜索 string, n查看下一个,N查看上一个
            + ?string : 向上搜索 string, n查看下一个,N查看上一个
            + q : 退出
    6. sort 排序浏览,对文本文件中内容进行排序查看，默认为字典升序
        + sort 文件 : 字典升序查看文件内容
        + sort -r 文件 : 字典降序查看文件内容
        + sort -u 文件 : 剔除文本文件中重复的内容
        + sort -n 文件 : 按照数字升序
    7. sed 流式浏览，流式编辑器
        + sed -n "/string/p" 文件 : 查看包含关键字的行
        + sed -n "1,5p" 文件 : 打印第 1~5 行内容
        + sed -n "3,5{=;p}" 文件 : 打印第 3~5 行内容, 并且打印行号
        + sed -n "10p" 文件 : 打印第 10 行内容

+ #### Vim 编辑器 : 系统内置 vi 编辑器, 可以在系统中安装独立的 vim 编辑器 `yum install -y vim`
    + vim 文本文件
    
    + 编辑器三种模式切换
        1. Command mode (命令模式\查看模式\视图模式) : 打开文件时处于命令模式，按 : 或 / 进入末行模式
        2. Insert mode (插入模式\输入模式)  : 命令模式下按 a 进入插入模式，ESC 返回命令模式 
        3. Last Line mode (底线模式\末行模式\末行命令模式) : 输入固定格式的内容，处理特定功能，按 ESC 或 Enter 退回命令模式
    
    + 命令模式命令
        1. 文本操作
           
            按键 | 描述
            :---: | :---:
            x | 删除光标后面字符,相当于 delete (常用)
            X | 删除光标前面字符,相当于 backspace
            dd | 删除光标所在行 (常用)
            ndd | n 为数字,连续删除光标后 n 行
            yy | 复制光标所在行 (常用)
            nyy | n 为数字,复制光标所在的行下 n 行
            p | 将已复制的数据在光标下一行粘贴
            P | 将已复制的数据在光标上一行粘贴
            u | 复原前一个动作
            
        2. 进入编辑模式
           
            按键 | 描述
            :---: | :---:
            a | 光标后面插入字符
            A | 行尾插入字符
            i | 光标前面插入字符
            I | 行首插入字符
            o | 光标下一行输入字符
            O | 光标上一行输入字符
            
        3. 末行模式 (冒号指令)
           
            按键 | 描述
            :---: | :---:
            :w | 保存文件
            :w! | 强制保存文件
            :q | 不保存退出
            :q! | 不保存并强制退出文件
            :wq | 保存并退出文件
            :wq! | 强制保存并退出文件

### 协程 

+ #### 比线程更小的可执行单元,协程是线程调度的
+ #### 协程只是单纯的操作 cpu 的上下文,比线程切换更快速
+ #### 1:N 模式 : 一个线程作为容器可以部署多个线程
+ #### 协程的使用方式 yield, 使用 gevent库

    ````
    import time
    # 利用生成器实现多任务

    def func1(num):
        while True:
            print(f"开始爬取数据{num}")
            time.sleep(1)
            yield

    def func2(num):
        while True:
            print(f"开始处理数据{num}")
            time.sleep(1)
            yield

    if __name__ == '__main__':
        num = 0
        while True:
            next(func1(num))
            next(func2(num))
            num += 1
    
    # gevent 创建协程实现多任务
    import time
    import gevent

    def task(n):
        for i in range(n):
            print(gevent.getcurrent().name, i)
            gevent.sleep(1)
    
    if __name__ == '__main__':
        # 创建协程
        g1 = gevent.spawn(task, 5)
        g2 = gevent.spawn(task, 10)
        # 启动协程
        # g1.join()
        # g2.join()
        gevent.joinall([g1, g2])
  ````
  
### Centos 7 网络配置 (配置静态 ip 地址)

+ #### 通常情况下，我们的开发环境中不需要自动配置(自动配置导致IP地址的动态变化不是我们期望的)，通过修改配置文件的方式，指定IP地址以及网络配置信息。

+ #### 网络配置文件位置 /etc/sysconfig/network-scripts/ifcfg-网卡名

+ #### 配置前先备份

    ```
    TYPE="Ethernet"
    PROXY_METHOD="none"
    BROWSER_ONLY="no"
    DEFROUTE="yes"
    IPV4_FAILURE_FATAL="no"
    IPV6INIT="yes"
    IPV6_AUTOCONF="yes" 
    IPV6_DEFROUTE="yes" 
    IPV6_FAILURE_FATAL="no"
    IPV6_ADDR_GEN_MODE="stable-privacy"
    NAME="ens33" 
    UUID="434fc2b9-dd08-456f-8a5c-4a266201371a"
    DEVICE="ens33"
    ONBOOT="yes"
    # 配置 IP 地址 dhcp 自动获取 IP
    # BOOTPROTO=dhcp
    # 静态 IP 地址分配
    BOOTPROTO="static"
    # 配置IP 地址
    IPADDR=192.168.0.100
    # 配置子网掩码 默认
    NETMASK=255.255.255.0
    # 配置 DNS
    DNS1=114.114.114.114
    DNS2=8.8.8.8
    # 配置网关
    GATEWAY=192.168.0.2                   
  ```

+ #### 改完配置文件后需要重新启动

    + 重启网络服务

        ```
      systemctl restart network.service
      ```
      
+ #### 服务管理命令 (针对服务的开启、重启、停止)

    + systemctl start 服务名 : 开始服务

    + systemctl restart 服务名 : 重启服务

    + systemctl stop 服务名 : 停止服务

    + systemctl status 服务名 : 查看服务状态

        ````
      systemctl status network  # 查看网络状态
      systemctl stop network    # 停止网络服务
      ````
      
### 计划任务

1. #### 突发任务 atd (了解, 临时性，一次性的任务)

    1. 查看服务是否启动 atd (默认运行)

        ```
       systemctl status atd
       ```
       
    2. 编辑突发任务

        + 格式 `at 时间`
            + 时间单位:
                + min : 分钟
                + day : 天
                + 12:30 2020-09-10 制定具体时间执行任务
            + at now+1min : 一分钟后执行
        + ctrl + d : 保存任务
        + ctrl + c : 编辑过程中撤销任务
        + at -l : 查看所有突发任务
        + atrm 任务 id : 删除指定的突发任务
    
2. #### **定时性任务** (crontab 掌握)

    1. 周期性的，循环执行,一般用于定时删除日志、备份文件、爬取数据
    2. 查看服务状态

        ```
       systemctl status crond
       ```
       
    3. 编辑定时任务, 进入一个类似于 vim 编辑器的页面创建任务
        + 格式

            ````
          crontab -u root -e
            # -u : 用户名
            # -e : 编辑
            # -l : 查看所有定时任务
            # -r : 删除所有定时任务 (慎用)
          ````
          
        + 创建任务格式

            ```
          *     *    *     *     *      需要执行的命令
          分    时    日    月     周    定时执行任务
          0-59  0-23      0-12   0-7   0 和 7 代表周日
          ```
          
            + \* : 代表任意数字
            + \- : 代表 范围
            + \/ : 代表 频率
            + \, : 离散的数字
   
    4. 查看异常
        + 脚本输出,或者脚本出现异常 ---- 终端看不到信息
            + 输出信息和异常信息 : /var/spool/mail 目录下对应用户的文件中
    5. 例子

        ````
       # 每天的 8:00 执行一次 1.py 文件
       0 8 * * * python 1.py
       # 每年的五月一日 10:05 执行一次 1.py 文件
       5 10 1 5 * python 1.py
       # 每天的 1 点、5 点 各执行一次 1.py 文件
       0 1,5 * * * python 1.py
       # 每天的3,4,5点 每五分钟各执行一次 1.py 文件
       60/5 3-5 * * * python 1.py
       # 每周的周一 10点执行一次  1.py 文件
       0 10 * * 1 python 1.py
       ````
       
### ssh 服务 : 连接远程服务器

+ ##### ssh 服务介绍
    + SSH是专门为远程登录会话和其它网络服务提供的安全性协议
    + SSH服务端是一个进程.在后台运行并相应来自客户端的链接.
    + ssh服务端的进程名是sshd,负责监听远程客户端的链接,并处理.

+ #### ssh 客户端  (ssh 链接、sshd 远程拷贝、slogin 远程登录、sftp 安装FTP文件传输)

    1. 检查 sshd 启动状态，关闭安全协议
        ```
        systemctl status sshd
        setenforce 0
       ```
    
    2. windows 链接 服务器 (Mac 直接通过命令 ssh 用户名@IP 地址 即可连接) 
        1. Windows 10 通过 powershell 直接使用 ssh 链接 `ssh 用户名@IP 地址`
        2. Windows 10 通过 Git Bash 界面链接 `ssh 用户名@IP 地址`
        3. Windows 10 通过 Termius 软件链接
    
+ #### ssh 免密登录 (Termius 等可视化界面记住密码, 命令行使用私钥登录服务器)
    1. 在客户端生成 密钥对 (生成密钥对默认位置 私钥 : `C:\Users\用户名\.ssh\id_rsa` 公钥 : `C:\Users\用户名\.ssh\id_rsa.pub`)
        ```
       ssh-keygen -t rsa
       ```
    
    2. 将生成 公钥 上传到服务器
        ```
       ssh-copy-id 用户名@IP 地址
        <==>
       ssh -i 本地私钥路径 用户名@IP 地址
       ```

+ #### scp 命令 传输文件
  
    1. 从本地向服务端上传文件
        ```
       scp 本地文件路径 用户名@IP 地址:/上传后文件放置地
       ```
    
    2. 从服务端下载文件到本地
        ```
       scp 用户名@IP 地址:下载文件路径 本地存放路径
       ```
       
    3. `scp -r` 上传或下载文件夹
    
### 链接

+ 硬链接:
    ```
  ln 源文件 目标文件
  ```
    + 硬连接的大小等于原文件大小
    + 源文件删除，链接文件仍然可以使用
    + 类似于复制原文件

+ 软链接
    ```
  ln -s 源文件绝对路径 目标文件绝对路径
  ```
    + 软连接的大小，基于原文件的名字
    + 源文件删除，链接失效
    + 只是存储链接指向关系,如果定义的是相对路径,会出现符号报错 [连接的层数过多] 而无法调用
           