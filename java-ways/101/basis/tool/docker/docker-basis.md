```yaml
   Author: Gentleman.Hu
   Create Time: 2020-11-01 10:47:02
   Modified by: Gentleman.Hu
   Modified time: 2020-11-02 11:23:19
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description: Docker new one
 ```

## Docker

### Installation

> [get-started](https://www.docker.com/get-started)

对应系统下载.

安装好,在托盘图标可以看到状态,启动成功

![](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20201101171631.gif)

- 查看版本

![](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20201101171751.png)

### Images,Containers,and Ports

> docker image COMMAND

![](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20201101172030.png)

- show containers

> docker image ps 

![](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20201101172213.png)

- 基本命令平时就查看,其他build等简单使用

> docker container COMMAND

![](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20201101172426.png)

- show containers

> docker container ls [-a] 显示全部(包含未运行的)

![](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20201101172710.png)

>> image就是镜像,静态的,通过image可以生成container

> docker pull COMMAND

![](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20201101173513.png)

拉取image

> docker run COMMAND

![](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20201101175006.png)

> docker run --name name -d imagename 

通过image创建container并运行 -d,dettach

- 开放端口

> docker run -p outer:inner imagename

outer: 外部端口
inner: 内部端口

比如 8080:80  ,外部宿主计算机端口映射到docker内部80端口

- 开放多个端口

-p 8080:80 -p 2222:222 -p etc...


- 删除container

> docker rm -f containername

- 删除image

> docker rmi imagename

### Volumes - Host adn Container

- share file from host

> docker run --name name -v /some/folder:/usr/local/nginx/html:ro -p 8080:80 nginx:latest

- going inside container

> docker exec -it containername bash(/bin/sh)

![](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20201101184623.png)

### Building Images

- Dockerfile

```dockerfile
FROM ubuntu:18.04
COPY . /app
RUN make /app
CMD python /app/app.py
```

> [Reference](https://docs.docker.com/engine/reference/builder/)

- docker build

![](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20201102111111.png)

- docker push 

推送到duckerhub或者其他docker仓库

- .dockerignore

> [Reference](https://docs.docker.com/engine/reference/builder/#dockerignore-file)

```ignore
# comment
*/temp*
*/*/temp*
temp?
```

| Rule        | Behavior                                                     |
| :---------- | :----------------------------------------------------------- |
| `# comment` | Ignored.                                                     |
| `*/temp*`   | Exclude files and directories whose names start with `temp` in any immediate subdirectory of the root. For example, the plain file `/somedir/temporary.txt` is excluded, as is the directory `/somedir/temp`. |
| `*/*/temp*` | Exclude files and directories starting with `temp` from any subdirectory that is two levels below the root. For example, `/somedir/subdir/temporary.txt` is excluded. |
| `temp?`     | Exclude files and directories in the root directory whose names are a one-character extension of `temp`. For example, `/tempa` and `/tempb` are excluded. |


此文件忽略通过规则定义的文件
然而,往往忽略的,需要在`dockerfile`中重新`RUN`来在部署时候生成`module`等

- Alpine

很精简的,体积很小.适合集成docker中

> [official](https://alpinelinux.org/)
> [docker_alpine](https://hub.docker.com/_/alpine)

```dockerfile
FROM alpine:3.7
RUN apk add --no-cache mysql-client
ENTRYPOINT ["mysql"]
```

一个使用例子
36.8MB

### Resources

- [https://hub.docker.com/_/alpine](https://hub.docker.com/_/alpine)
- [dockerignore](https://stackoverflow.com/a/25748464)
