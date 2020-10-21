### Django

#### Django 项目部署

##### 环境准备

1. 安装 python3
   1. 安装 python 依赖包
   2. 下载 python 包
   3. 解压安装
   4. 创建软链接
      + `ln -s /user/local/python3/bin/python3 /usr/bin/python3`
      + `ln -s /user/local/python3/bin/pip3 /usr/bin/pip3`
2. 安装 MariaDB
   1. 下载 : `yum install mariadb mariadb-server.x86_64 mariadb-devel.i686 -y`
   2. 启动 : `systemctl start mariadb`
   3. 设置数据库密码 : `mysql_secure_installation`

##### 项目部署

1. 导出 Django 的开发环境 : `pip freeze > package.txt`
2. 将包目录上传服务器,并进行安装
   + 将 package.txt 放在 /opt 目录下并安装 : `pip3 install -r package.txt`
3. 上传 Django 项目 (将 Django 项目放在 /opt 目录下)
   1. 修改 `settings.py` 文件
      + 修改 数据库文件 配置
      + 将 ALLOWED_HOSTS=['*'] 允许所有主机访问
   2. 创建库,数据迁移
      1. `python manage.py check`
      2. `python manage.py makemigrations`
      3. `python manage.py migrate`
   3. 关闭防火墙 : `systemctl stop firewawll`
   4. 启动项目 : `python3 manage.py runserver 0.0.0.0:8000`

##### Nginx + uWSGI 部署项目

1. uWSGI

   1. 安装配置 uWSGI : `pip3 install uwsgi`

   2. 创建软链接 : `ln /usr/local/python3/bin/uwsgi /usr/bin/uwsgi`

   3. 进入项目主目录 测试 uWSGI : `uwwsgi --http 192.168.33.131:8000 --file Qshop/wsgi.py --static-map=/static=static`

   4. 配置文件形式 使用 uWSGI

      1. 创建 `uwsgi.ini` 配置文件

         1. `cd /opt`
         2. `mkdir script`
         3. `cd script`
         4. `touch wusgi.ini`

      2. 编写配置文件 `uwshi.ini` (部署项目时要删除注释的空格)

         ```ini
         [uwsgi]
         
         chdir=/opt/Qshop  ## 项目目录
         module=Qshop.wsgi:application  ## 项目指定的 application
         socket=/opt/script/uwsgi.sock  ## 指定 sock 文件路径
         workers=5 ## 进程个数
         pidfile=/opt/script/uwsgi.pid
         http=192.168.33.131:8000  ## 指定 ip 端口
         static-map=/static=/opt/Qshop/static  # 指定静态文件
         uid=root  ## 用户
         gid=root  ## 组
         master=true  ## 启用主线程
         vacuum=true  ## 自动移除 unix Socket 和 pid 文件,当服务网停止时
         enable-threads=true  ## 启用线程
         thunder-lock=true  ## 序列化接受的内容,如果可能的话
         harakiri=30  ## 设置自中断时间
         post-buffreing=4096
         daeminize=/opt/script/uwsgi.log  ## 设置日志目录
         ```

      3. 启动 uWSGI

         + `cd /opt/script`
         + `uwsgi --ini uwsgi.ini`

      4. 停止 uWSGI

         + `netstat -ntlp | grep 8000`
         + `ps aux | grep uwsgi`

2. Nginx

   1. 下载 Nginx 包 : `wget -c https://nginx.org/download/nginx-1.12.2.tar.gz`
   2. 安装 Nginx
      1. 解压 : `tar -zxvf nginx-1.12.2.tar.gz`
      2. 进入解压目录安装
         + `cd nginx-1.12.2`
         + `./configure \`
         + `make && make install`
      3. 创建软链接
         + `ln -s /usr/local/nginx/sbin/nginx /usr/bin/nginx`
   3. 启动 Nginx
      + nginx: 启动 Nginx
      + nginx -s stop: 停止 Nginx
      + nginx -s reload: 重启 Nginx
      + nginx -t: 检测是否正确

##### Django + uWSGI + Nginx

1. Nginx 配置

   + 备份配置文件 : `cp /usr/local/nginx/conf/nginx.conf /usr/local/ngiinx/conf/nginx.conf.bak`

   + 修改配置文件 `nginx.conf` (部署项目时要删除注释的空格)

     ```
     http {
     	# 文件拓展名与文件类型映射表
     	include		mime.types;
     	# 默认文件类型, 默认为 text/plain
     	default_type	application/octet-stream;
     	# 日志格式和名字
     	log_format	main '$remote_addr	-	$remote_user [$time_local] "$request"'
     					 '$status $body_bytes_sent "$http_referer"'
     					 '"$http_user_agent" "$http_x_forwawrded_for"';
         # 访问记录日志
         access_log	logs/access.log	main;
         # 允许 sendfile 方式传输文件
         sendfile	on;
         # tcp_nopush	on;
         
         # keepalive_timeout	0;
         # 连接超时时间
         keepalive_timeout	65;
         # 允许 gzip 压缩
         gzip	on;
         # 设置支持压缩的 content-type
         gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;
         
         
         server {
         	# 端口号
         	listen		80;
         	server_name	Qshop;
         	
         	charset		utf-8;
         	
         	location / {
         		include uwsgi_params;
         		uwsgi_connect_timeout 30;
         		uwsgi_pass unix:/opt/script/uwsgi.sock;
         	}
         	
         	error_page 500 502 503 504 /50.html;
         	
         	location = /static/ {
         		alias	/opt/Qshop/static;
         		index	index.html	index.html,
         	}
         	
         }
     }
     ```

     

2. 启动项目

   1. 确保 nginx 与 uwsgi 都已经关闭
   2. `uwsgi --ini uwsgi.ini`
   3. `nginx`

3. 修改 `uwwsgi.ini` (修改 http=127.0.0.1:8000 不允许外网通过 ip + :8000 端口直接访问) (部署项目时要删除注释的空格) 

   ```ini
   [uwsgi]
   
   chdir=/opt/Qshop  ## 项目目录
   module=Qshop.wsgi:application  ## 项目指定的 application
   socket=/opt/script/uwsgi.sock  ## 指定 sock 文件路径
   workers=5 ## 进程个数
   pidfile=/opt/script/uwsgi.pid
   http=1127.0.0.1:8000  ## 指定 ip 端口
   static-map=/static=/opt/Qshop/static  # 指定静态文件
   uid=root  ## 用户
   gid=root  ## 组
   master=true  ## 启用主线程
   vacuum=true  ## 自动移除 unix Socket 和 pid 文件,当服务网停止时
   enable-threads=true  ## 启用线程
   thunder-lock=true  ## 序列化接受的内容,如果可能的话
   harakiri=30  ## 设置自中断时间
   post-buffreing=4096
   daeminize=/opt/script/uwsgi.log  ## 设置日志目录
   ```

   

