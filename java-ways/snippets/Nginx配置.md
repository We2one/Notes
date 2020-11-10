```yaml
   Author: Gentleman.Hu
   Create Time: 2020-11-09 22:53:52
   Modified by: Gentleman.Hu
   Modified time: 2020-11-09 23:27:06
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description: 一些nginx配置
 ```

## Index of 目录

- nginx 开启对某目录的index

```nginx
location /somedirectory/ {
    autoindex on;
    autoindex_exact_size off;
    autoindex_format html;
    autoindex_localtime on;
}
```

## 反代不显示图片等信息

```nginx
location /
{
    proxy_pass http://127.0.0.1:8083;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header REMOTE-HOST $remote_addr;
    
    add_header X-Cache $upstream_cache_status;
    
    #Set Nginx Cache
    
    	add_header Cache-Control no-cache;
    expires 12h;
}
location ~ .*.(js|css|png|img|gif|jpg)$ {
proxy_pass http://127.0.0.1:8083;
}
```

### Apache 的多目录分流代理

```apache
<VirtualHost *:80>
    ServerAdmin webmasterexample.com
    DocumentRoot "/www/wwwroot/tt.521521.ml/blackhole/blackhole/"
    ServerName SSL.tt.521521.ml
    ServerAlias tt.521521.ml 
    #errorDocument 404 /404.html
    ErrorLog "/www/wwwlogs/tt.521521.ml-error_log"
    CustomLog "/www/wwwlogs/tt.521521.ml-access_log" combined
	#引用重定向规则，注释后配置的重定向代理将无效
	IncludeOptional /www/server/panel/vhost/apache/redirect/tt.521521.ml/*.conf
	#HTTP_TO_HTTPS_START
    <IfModule mod_rewrite.c>
        RewriteEngine on
        RewriteCond %{SERVER_PORT} !^443$
        RewriteRule (.*) https://%{SERVER_NAME}$1 [L,R=301]
    </IfModule>
    #HTTP_TO_HTTPS_END
	#SSL
    SSLEngine On
    SSLCertificateFile /www/server/panel/vhost/cert/tt.521521.ml/fullchain.pem
    SSLCertificateKeyFile /www/server/panel/vhost/cert/tt.521521.ml/privkey.pem
    SSLCipherSuite EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH
    SSLProtocol All -SSLv2 -SSLv3 -TLSv1
    SSLHonorCipherOrder On
    
    #PHP
    <FilesMatch \.php$>
            SetHandler "proxy:unix:/tmp/php-cgi-72.sock|fcgi://localhost"
    </FilesMatch>
    
    #Proxypass /ray http://127.0.0.1:51816
    #ProxyPassReverse /ray http://127.0.0.1:51816
    
     <Location "/feel">
    RewriteEngine On
    RewriteCond %{HTTP:Upgrade} =websocket [NC]
    RewriteRule    /(.*)  ws://localhost:51816/feel [P,L]
    RewriteCond %{HTTP:Upgrade} !=websocket [NC]
    RewriteRule   /(.*)   http://localhost:51816/feel [P,L]
    Proxypass  http://127.0.0.1:51816/feel
    ProxyPassReverse  http://127.0.0.1:51816/feel

  </Location>
    #DENY FILES
     <Files ~ (\.user.ini|\.htaccess|\.git|\.svn|\.project|LICENSE|README.md)$>
       Order allow,deny
       Deny from all
    </Files>

    #PATH
    <Directory "/www/wwwroot/tt.521521.ml/">
        SetOutputFilter DEFLATE
        Options FollowSymLinks
        AllowOverride All
        Require all granted
        DirectoryIndex index.php index.html index.htm default.php default.html default.htm
    </Directory>
</VirtualHost>
<VirtualHost *:443>
    ServerAdmin webmasterexample.com
    DocumentRoot "/www/wwwroot/tt.521521.ml/blackhole/blackhole/"
    ServerName SSL.tt.521521.ml
    ServerAlias tt.521521.ml 
    #errorDocument 404 /404.html
    ErrorLog "/www/wwwlogs/tt.521521.ml-error_log"
    CustomLog "/www/wwwlogs/tt.521521.ml-access_log" combined
	#引用重定向规则，注释后配置的重定向代理将无效
	IncludeOptional /www/server/panel/vhost/apache/redirect/tt.521521.ml/*.conf
	#HTTP_TO_HTTPS_START
    <IfModule mod_rewrite.c>
        RewriteEngine on
        RewriteCond %{SERVER_PORT} !^443$
        RewriteRule (.*) https://%{SERVER_NAME}$1 [L,R=301]
    </IfModule>
    #HTTP_TO_HTTPS_END
	#SSL
    SSLEngine On
    SSLCertificateFile /www/server/panel/vhost/cert/tt.521521.ml/fullchain.pem
    SSLCertificateKeyFile /www/server/panel/vhost/cert/tt.521521.ml/privkey.pem
    SSLCipherSuite EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH
    SSLProtocol All -SSLv2 -SSLv3 -TLSv1
    SSLHonorCipherOrder On
    
    #PHP
    <FilesMatch \.php$>
            SetHandler "proxy:unix:/tmp/php-cgi-72.sock|fcgi://localhost"
    </FilesMatch>
    
    #Proxypass /ray http://127.0.0.1:51816
    #ProxyPassReverse /ray http://127.0.0.1:51816
    
     <Location "/feel">
    RewriteEngine On
    RewriteCond %{HTTP:Upgrade} =websocket [NC]
    RewriteRule    /(.*)  ws://localhost:51816/feel [P,L]
    RewriteCond %{HTTP:Upgrade} !=websocket [NC]
    RewriteRule   /(.*)   http://localhost:51816/feel [P,L]
    Proxypass  http://127.0.0.1:51816/feel
    ProxyPassReverse  http://127.0.0.1:51816/feel

  </Location>
    #DENY FILES
     <Files ~ (\.user.ini|\.htaccess|\.git|\.svn|\.project|LICENSE|README.md)$>
       Order allow,deny
       Deny from all
    </Files>

    #PATH
    <Directory "/www/wwwroot/tt.521521.ml/">
        SetOutputFilter DEFLATE
        Options FollowSymLinks
        AllowOverride All
        Require all granted
        DirectoryIndex index.php index.html index.htm default.php default.html default.htm
    </Directory>
</VirtualHost>
```