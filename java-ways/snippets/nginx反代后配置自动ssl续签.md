```yaml
   Author: Gentleman.Hu
   Create Time: 2020-11-13 13:56:23
   Modified by: Gentleman.Hu
   Modified time: 2020-11-13 13:59:37
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description:
 ```

## Nginx配置反代后,如何自动续签ssl

> [引用](https://blog.csdn.net/fjh1997/article/details/105765531)

- 反代

```nginx
  RewriteEngine On
  RewriteCond %{HTTP:Upgrade} =websocket [NC]
  RewriteRule /(.*)           ws://localhost:8080/$1 [P,L]
  RewriteCond %{HTTP:Upgrade} !=websocket [NC]
  RewriteRule /(.*)           http://localhost:8080/$1 [P,L]

  ProxyRequests off
  ProxyPass        / http://localhost:8080/ nocanon
  ProxyPassReverse / http://localhost:8080/
```

- 自动续签

```nginx
server {
  listen  443 ssl;
  listen       [::]:443 ssl;
  ssl_certificate       /data/example.com.pem;
  ssl_certificate_key   /data/example.com.pem;
  ssl_protocols         TLSv1 TLSv1.1 TLSv1.2;
  ssl_ciphers           HIGH:!aNULL:!MD5;
  server_name           example.com;
  client_max_body_size    1000m;
  location ^~ /.well-known/acme-challenge/ {
        default_type "text/plain";
        allow all;
        root /var/www/example.com/;
   }

  location / { 
        proxy_redirect off;
        proxy_pass http://xxxxxxx:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $http_host;

       
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

  }
  ```

  - 负载均衡

> https://blog.csdn.net/specter11235/article/details/79922149?depth_1-