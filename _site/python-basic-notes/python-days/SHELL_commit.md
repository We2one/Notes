### SHELL 脚本 (shell编程就是通过终端编写的脚本程序,辅助开发人员完成命令的工程自动化操作, 解释器使用 bash 或 sh)

+ #### SHELL 脚本基本语法
    
    1. 脚本编写规范 (shell脚本程序是linux系统中的一种特殊的文件,一定要妥善的整理和管理)
        + 属于用户的脚本程序,全部放在指定的路径的scripts目录下
        + 脚本程序后缀名统一使用.sh(约定俗称)
        + 脚本程序的第一行: #!/bin/sh  或者 #!/bin/bash 指定程序的执行者
    
    2. SHELL 脚本输入输出
        
        + echo 输出信息  (-n : 不换行输出)
        
        + read 标准输出 (读取用户从键盘输出信息)
            
            + read 变量名  : 不带提示信息传入变量
            
            + read -p "提示信息" 变量名 : 带提示信息传入变量
            
            + read -s -p "提示信息" 变量名 : 带提示信息传入变量,输入信息不回显
            
        + 运行 shell 脚本两种方式
            1. 对当前目录下的file.sh文件的所有者增加可执行权限
                ```
               chmod u+x file.sh
               # u : 文件所有者
               # x : 执行权限
               # + : 增加权限
               # 直接运行 shell 脚本
               ./file.sh
               ```
            
            2. 使用命令方式执行
                ```
               sh ./file.sh
               ```
       
        + 变量 (一个有特殊意义的符号,由数字,字母,下划线组成,数字不能开头)
            
            + 先声明，后使用, 变量名中不要使用特殊符号,不要以$开头,不能以关键字命名
            
            + 声明变量的格式 : 变量名=值
            
            + 使用变量 : ${变量名}
            
    3. SHELL 程序控制结构 (控制程序的运行流程 : 顺序结构,选择结构,循环结构)
        
        1. 选择结构 if
            1. 语法
                + 单分支语法
                    ```
                  if 条件
                  then
                    条件如果为真执行代码
                  fi
                  ```
                + 双分支语法
                    ```
                  if 条件1;then
                    条件1 为真执行代码
                  else
                    条件1 为假执行代码
                  fi
                  ```
                + 多分支语法
                    ```
                  if 条件1;then
                    条件1 为真执行代码
                  elif 条件2;then
                    条件2 为真执行代码
                  else
                    条件1,2 为假执行代码
                  fi
                    ```
            
            2. 文件判断
                 
                命令 | 命令意义
                :---: | :---:
                if[ -e 文件路径 ] | 判断文件是否存在
                if[ -d 文件路径 ] | 判断是否是文件夹
                if[ -f 文件路径 ] | 判断是否文件
                if[ -r 文件路径 ] | 判断文件是否可读
                if[ -w 文件路径 ] | 判断文件是否可写
                if[ -x 文件路径 ] | 判断文件是否可执行
                
            3. 字符串的判断
                
                命令 | 命令意义
                :---: | :---:
                =/==  | 判断两个字符是否相等 [ $a=$b ]
                !=    | 判断两个字符是否不等 [ $a!=$b ] 
                -z    | 判断字符串长度是否为0  如果为0返回true [ -z $变量 ]
                -n    | 判断字符串是否不为空 不为空返回true [ -n “$变量” ]
                
            4. 数值比较
                
                命令 | 命令意义
                :---: | :---:
                -eq   | = 相等 [ $a -eq $2 ]
                -gt   | > 大于  
                -it   | < 小于
                -ge   | >= 大于等于
                -le   | <= 小于等于
                -ne   | != 不等
                
            5. 逻辑判断
                
                命令 | 命令意义
                :---: | :---:
                &&    | 并且/与 and
                ||    | 或者 or
                -o    | 或者 or
                !     | 取反
        
        2. case 分支语句 (等值匹配)
            
            + 语法 
                ```
              case 变量 in
              值 1)
                执行代码
              ;;
              值 2)
                执行代码
              ;;
              *)
                上述条件都不成立时执行
              esac
              ```
                + 例子
                    ```
                    [angleliuliu@localhost 桌面]$ cat -n case.sh 
                     1  #!/bin/sh
                     2
                     3  read -p "请输入你要进行的操作1)登录,2)退出" num
                     4
                     5  case $num in
                     6  1|login )
                     7      echo "登录"
                     8      ;;
                     9  2|exit )
                    10      echo "退出"
                    11      ;;
                    12  * )
                    13      echo "输入错误"
                    14  esac
                  ```
      
        3. for 循环
            ```
           for 临时变量 in 可迭代数据传
           do 
            循环中代码
           done
           ```
            + 例子
                ```
                [angleliuliu@localhost 桌面]$ cat for.sh 
                #!/bin/sh
                
                num="1 2 3 4 5"
                
                for i in $num
                do
                    echo $i
                    sleep 1
                done
                [angleliuliu@localhost 桌面]$ sh for.sh 
                1
                2
                3
                4
                5
              ```
           
        4. while 循环
            ```
           while 条件
           do
            循环执行代码
           done
           ```
            + 例子
                ```
                [angleliuliu@localhost 桌面]$ cat -n while.sh 
                1  #!/bin/sh
                2
                3  i=1
                4  while (($i <= 10))
                5  do
                6      echo $i
                7      let i++
                8  done
                9
                10
                11  j=1
                12  sum=0
                13  while [ $j -le 100 ]
                14  do
                15      sum=`expr $sum + $j`
                16      let j++
                17  done
                18  echo $sum
                [angleliuliu@localhost 桌面]$ sh while.sh 
                1
                2
                3
                4
                5
                6
                7
                8
                9
                10
                5050
              ```
        
        5. 数值运算三种方式
            
            1. expr 运算表达式 :
                 ```
                 sum=`expr 1+1`
               ```
            
            2. $(()) 运算符号
                ```
               res=$((1+2))
               ```
           
            3. $[] 运算符号
                ```
               res=$[1+2]
               ```
        
        6. 数组
            + 数组语法
                ```
              names=("a" "b" "c")
                <==>
              names="a b c"
              ```
          
            + 数组取用
                
                + echo names : 返回第一个元素
                + echo ${names[@]}  : 获取所有的
                + echo ${names[*]}  : 获取所有的,作为一个完整字符串
                + echo ${names[1]}  : 通过索引获取指定值
                + echo ${#names[@]} : 获取指定数组长度
                + names[1]=""   : 动态存入数据至数组
                 
             + 例子
                ```
                 angleliuliu@localhost 桌面]$ cat -n arr.sh 
                 1  #!/bin/sh
                 2
                 3  arr=("1" "2" "3")
                 4
                 5  echo arr
                 6  echo ${arr[@]}
                 7  echo ${arr[*]}
                 8  echo ${arr[1]}
                 9  echo ${#arr[@]}
                [angleliuliu@localhost 桌面]$ sh arr.sh 
                arr
                1 2 3
                1 2 3
                2
                3
               ```
             
    4. SHELL 函数
        
        + 函数格式
            ```
          # 声明函数
          function 函数名(){
            代码段
          }
          
          # 也可以
          函数名(){
            代码段
          }
          函数的调用
          函数名
          ```
          
        + 函数的传参
          + 函数的传参 `函数名 参数1 参数2 ...`
          + 接收参数
              + $0  接受当前文件的名称
              + $1  接受到的第一个参数
              + $2  接受到的第二个参数
              + ${10}  10以上的参数需要加{}
              + $@ 表示接受到的所有参数
              + $*  接受到的所有参数
              + $#  表示接受的参数个数
              + $?  表示检测上一条命令是否执行成果 (执行成果 返回 0)
          ```
          [angleliuliu@localhost 桌面]$ sh func.sh 
          test1
          test2
          a
          b
          a b c d e f g 1 2 3
          10
          a b c d e f g 1 2 3
          3
          [angleliuliu@localhost 桌面]$ cat func.sh 
          #!/bin/sh
            
          function test1(){
              echo "test1"
          }
            
          test2(){
              echo "test2"
              echo $1
              echo $2
              echo $@
              echo $#
              echo $*
              echo ${10}
          }
            
          # 调用函数
          test1
          ```
          