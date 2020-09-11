# Youtube离线下载

## 1.安装MediaDownloader

[MediaDownloader](https://github.com/Kallys/MediaDownloader)

## 2.配置rclone

## 3.配置inotify

- 监测mp3文件生成

    ```shell
    #!/bin/bash
    TARGET='/www/wwwroot/be.feelingyou.ml/MediaDownloader/public/downloads'
    downloadpath='/www/wwwroot/be.feelingyou.ml/MediaDownloader/public/downloads'

    inotifywait -m --exclude "[^m][^p][^3]$" $TARGET -e create -e moved_to | \
        while read path action file; do
                echo "The file '$file' appeared in directory '$TARGET' via '$action'"
            if [[ "$file" =~ .*temp.*$ ]]; then
                echo "这是临时文件不上传"
            elif [[ "$file" =~ .*mp3$ ]]; then
                /usr/bin/php /www/wwwroot/pan.i-love-you.ml/one.php upload:file "$TARGET/$file" /Youtube-dl/musics/
            fi
        done
    ```

- 监测mp4

  ```shell
  #!/bin/bash
  TARGET='/www/wwwroot/be.feelingyou.ml/MediaDownloader/public/downloads'
  downloadpath='/www/wwwroot/be.feelingyou.ml/MediaDownloader/public/downloads'
  
  inotifywait -m --exclude "[^m][^p][^4]$" $TARGET -e create -e moved_to | \
      while read path action file; do
             echo "The file '$file' appeared in directory '$TARGET' via '$action'"
  		if [[ "$file" =~ .*temp.*$ ]]; then
             echo "这是临时文件不上传"
  		elif [[ "$file" =~ .*mp4$ ]]; then
  			/usr/bin/php /www/wwwroot/pan.i-love-you.ml/one.php upload:file "$TARGET/$file" /Youtube-dl/videos/
  		fi
      done
  ```

- 监测webm

  ```shell
  #!/bin/bash
  TARGET='/www/wwwroot/be.feelingyou.ml/MediaDownloader/public/downloads'
  downloadpath='/www/wwwroot/be.feelingyou.ml/MediaDownloader/public/downloads'
  
  inotifywait -m --exclude "[^w][^e][^b][^m]$" $TARGET -e create -e moved_to | \
      while read path action file; do
              echo "The file '$file' appeared in directory '$TARGET' via '$action'"
  		if [[ "$file" =~ .*temp.*$ ]]; then
              echo "这是临时文件不上传"
  #		if [[ "$file" =~ .f*.webm$ ]]; then
  #            echo "这是初始文件不上传"
  		elif [[ "$file" =~ .*webm$ ]]; then
  			/usr/bin/php /www/wwwroot/pan.i-love-you.ml/one.php upload:file "$TARGET/$file" /Youtube-dl/videos/
  			rm -rf "$TARGET/$file"
  		fi
      done
  
  ```

- 监测mkv

  ```shell
  #!/bin/bash
  TARGET='/www/wwwroot/be.feelingyou.ml/MediaDownloader/public/downloads'
  downloadpath='/www/wwwroot/be.feelingyou.ml/MediaDownloader/public/downloads'
  
  inotifywait -m --exclude "[^m][^k][^v]$" $TARGET -e create -e moved_to | \
      while read path action file; do
             echo "The file '$file' appeared in directory '$TARGET' via '$action'"
  		if [[ "$file" =~ .*temp.*mkv$ ]]; then
             echo "这是临时文件不上传"
  		elif [[ "$file" =~ .f*.*mp4$ ]]; then
  			echo "这是初始文件不上传"
  		elif [[ "$file" =~ .*mkv$ ]]; then
  			/usr/bin/php /www/wwwroot/pan.i-love-you.ml/one.php upload:file "$TARGET/$file" /Youtube-dl/videos/
  			rm -rf "$TARGET/$file"
  		fi
      done
  #inotifywait -m -e create -e moved_to --format "%f" $TARGET
  #    while read FILENAME; do
  #        #if [[ "$FILENAME" =~ .*mkv$ || "$FILENAME" =~ .*webm$ ]]; then
  #				#echo "mkv file"
  #            #filepath=$FILENAME
  #                #/usr/bin/php /www/wwwroot/pan.i-love-you.ml/one.php upload:file "$filepath" /Youtube-dl/videos/
  #                #rm -rf "$filepath"
  #                #exit 0
  #        #fi
  #   done
  
  # if [ $2 -eq 0 ]; then
  #     exit 0
  # fi
  # while true; do
  #     filepath=$path
  #     path=${path%/*}
  #     if [ "$path" = "$downloadpath" ] && [ $2 -eq 1 ]; then
  #         /usr/bin/php /www/wwwroot/pan.i-love-you.ml/one.php upload:file "$filepath" /upload/
  #         rm -rf "$filepath"
  #         exit 0
  #     elif [ "$path" = "$downloadpath" ]; then
  #         /usr/bin/php /www/wwwroot/pan.i-love-you.ml/one.php upload:folder "$filepath"/ /upload/"${filepath##*/}"/
  #         rm -rf "$filepath"/
  #         exit 0
  #     fi
  # done
  
  ```

  > 可能某些还未监测

- 较完美监测

  ```shell
  #!/bin/bash
  TARGET='/root/tmp'
  downloadpath='/www/wwwroot/be.feelingyou.ml/MediaDownloader/public/downloads'
  
  inotifywait -m $TARGET -e create -e moved_to |
      while read path action file; do
          echo "The file '$file' appeared in directory '$TARGET' via '$action'"
          filename="${file##*/}"
          extension="${filename##*.}"
          case $extension in
          mp3)
              echo "$file"
              echo "$extension"
              ;;
          *)
              echo "$file"
              echo "$extension"
              ;;
          esac
      done
  
  ```

  

## 4.安装任意一款OneDrive的index

- cuteone
- oneindex
- Olxdex?
- pyone
- ...

## 其他待完善





