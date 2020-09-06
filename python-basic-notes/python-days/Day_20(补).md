### 协程 

+ #### 比线程更小的可执行单元,协程是线程调度的
+ #### 协程只是单纯的操作 cpu 的上下文,比线程切换更快速
+ #### 1:N 模式 : 一个线程作为容器可以部署多个线程
+ #### 协程的使用方式 yield, 使用 gevent库
    ```
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
  ```
  
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
        ```
      systemctl status network  # 查看网络状态
      systemctl stop network    # 停止网络服务
      ```
      
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
            ```
          crontab -u root -e
            # -u : 用户名
            # -e : 编辑
            # -l : 查看所有定时任务
            # -r : 删除所有定时任务 (慎用)
          ```
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
        ```
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
       ```
       
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
    


           