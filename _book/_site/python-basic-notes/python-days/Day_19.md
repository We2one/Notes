### unittest : 单元测试模块

+ #### 单元测试 : 用来对一个模块/一个函数/一个类来进行正确性检验的测试工作

    + ##### 核心四个概念
        1. test case : (测试用例)
            + 一个 test case 的实例就是一个测试用例。测试前准备环境的搭建 (setUp), 执行测试代码 (run), 测试后环境的还原 (tearDown)
        
        2. test suite : (测试套件)
            + 多个测试用例的结合
        
        3. test runner : (测试运行器)
            + test loader : 用来加载 test case 到 test suite 里
            + 测试执行, 其中 run(test) 会执行 test suite /test case 中的 run(result) 方法
            
        4. test fixture : (测试环境数据准备和数据清理或者测试脚手架)
            + 测试用例环境的搭建和销毁
            + setUp 加载初始数据
            + tearDown 释放数据
    
    + ##### unittest 的使用
    
        1. 步骤
           
            1. 导入 unittest 模块, 被检测文件或者其中的类
            
            2. 创建一个测试类, 被继承 unittest.TestCase
            
            3. 重写 setUp 和 tearDown 方法 (如果有初始化条件和结束条件)
            
            4. 定义测试函数,函数名以test_开头,测试用例
            
            5. 在函数体中使用断言来测试测试结果是否符合预期结果
            
            6. 调用 unittest.main() 方法运行测试用例,无此方法也可运行
            
        2. 设置 setUp 和 tearDown : 每次用例执行前都会执行初始化条件和结束条件
        
        3. 设置 setupClass 和 teardownClass : 执行所有测试用例, 仅执行一次初始化条件和结束条件
        
        4. 断言 Assert ---- 结果对比的函数 (当一条测试用例执行失败,不会影响其他测试用例的执行)
            + 也可以直接用 >= / = / <= 判断
            
            方法 | 判断
            :---: | :---:
            assertEqual(a, b) : 相等 | a == b
            assertNotEqual(a, b) | a != b
            assertTrue(x) | bool(x) is True
            assertFalse(x) | bool(x) is False
            assertls(a, b) | a is b : 判断是否是同一对象 [id(a), 从存储地址上] 
            assertNottls(a, b) | a is not b  [id(a), 从存储地址上] 
            assertlsNone(x) | x is None
            assertlsNotNone | x is not None
            assertin(a, b) | a in b : 判断 a 是否在 b 中
            assertNotin(a, b) | a not in b
            assertlsInstance(a, b) | isInstance(a, b) : 实例对象
            assertNotlsInstance(a, b) | not isInstance(a, b) 
        
        ````
        """
        基本测试流程语法
        """
        import unittest

        # 创建类,继承unittest.TestCase
        class MyTest(unittest.TestCase):
        
            # 初始化测试数据, 类似于 __init__
            def setUp(self) -> None:
                print("开始初始化")
        
            # 释放数据
            def tearDown(self) -> None:
                print("释放数据")
        
            # 测试功能
            def test_add(self):
                a = 1
                b = 2
                res = 4
                # 测试目的 : 测试 a + b 是否为 res
                self.assertEqual(a+b, res)
        
            def test_sum(self):
                a = 1
                b = 2
                res = 3
                self.assertEqual(a+b, res)

        if __name__ == '__main__':
            # 调用测试用例,main自动执行test_开头的方法
            unittest.main()
      ````

### Python2 / Python3区别

1. #### print
    + Python2 : print 为 class
    
    + Python3 : print 为一个函数
    
2. #### range 与 xrange
    + Python2 : range() 得到为 列表; xrange() 得到为 range 生成器
    
    + Python3 : 得到一个 range 生成器
    
3. #### 字符串
    + Python2 : 存储字符串使用 **bit串** 存储方式,底层使用 ascii 编码方式,所以字符串有两种格式 str 和 unicode
    
    + Python3 : 存储字符串使用的是 bit unicode 字符串变长存储方式
    
4. #### 异常处理
    + Python2 

        ```
      try:
        ...
      except Exception, e:
        ...
      ```
    
    + Python3

        ```
      try:
        ...
      except Except as e:
        ...
      ```
  
5. #### 打开文件
    + Python2 : 打开文件有多种方式
        + f = file(...)
        + f = open(...)
    
    + Python3 : 打开文件只有一种方式
        + f = open(...)
    
6. #### 标准输入
    + Python2 : 两种标准输入
        + info = raw_input("提示消息")
        + ch = input("输入整数: ")
        
    + Python3 : 一种标准输入
        + info = input("提示消息")
    
7. #### 除法运算 : /
    + Python2 : 
        + / : 表示整除
        + 加上浮点数就是真实除法
    
    + Python3 : 
        + / : 真实除法
        + // : 整除
    
8. #### 自定义类型
    + Python2 : 保留原始类型继承关系的经典类,同时也支持继承 object 而衍生的新式类,所以在多继承操作过程中会出现两种不同的数据检索方式,对大型项目不友好，开发更加混乱
    
    + Python3 : 废弃经典类,只保留新式类 (自定义类), 或者直接继承 object

### Linux 系统

+ #### linu目录:
    + /:  根目录  所有文件的根
    + home:  一般存储的是 普通用户的用户目录
    + bin:  可执行的命令
    + etc:   配置信息
    + root:  管理员的用户目录
    + var:   一般存储日志文件
    + usr:   软件的默认安装目录
    + sbin:   只有管理员可以运行的命令  一般在此目录下 
    + opt:  系统给用户预留目录,或者自定安装一些软件一般选择安装在此目录


+ #### Linux 操作系统特性
  
    + 完全免费
    + 多用户、多任务
    + 良好的界面(相对而言)
    + 支持多种硬件平台
    + 安全性和稳定性高
    
+ #### 发行版本 (李纳斯.托瓦兹开发的Linux只是一个内核)
    + 商业公司维护的发行版本 : Red Hat 为代表
    + 社区组织维护的发行版本 : 以 Debian 为代表
    
+ #### linux 内核版本号 : 6.12.13
    + 主版本号 6 : 第六大版本
    + 次版本号 12 : 奇数表示开发版测试版,偶数表示稳定版
    + 末版本号 13 : 修改版本号，做过多少次修改
    
+ #### 防火墙

    + CentOS 6 关闭防火墙 [老版防火墙 : iptables，新版防火墙 : firewalld]
        + 关闭防火墙 : 
            + service stop firewalld
            + service iptables stop
        + 关闭开机启动
            + chkconfig firewalld off
            + chkconfig iptables off
        
    + CentOS 7 关闭防火墙
        + 关闭防火墙
            + systemctl stop firewalld
        + 关闭开机启动
            + systemctl disabled firewalld
        + 查看关闭状态
            + systemctl status firewalld
    
+ #### 命令操作 (命令基本格式 : 命令 [-选项] [参数] 可选)
    1. 帮助使用命令
        + 快捷键:  清屏  ctrl+l   /  clear
        + -h 或者 --help : 查看指定命令的帮助信息
            + 格式
                ```
              ls --help
              ```
        + which : 查看指定命令在文件系统环境变量中的位置
            + 格式 
                ```
              which 命令
              ```
        + whereis : 查看指定命令在文件系统的位置
            + 格式
                ```
              whereis 命令
              ```
    2. 系统常见命令
    
        + ls : 查看指定路径中的文件
            + `ls path` : 查看指定路径 path 下的文件列表
            + -a : 查看路径下所有文件,包含隐藏文件
            + -l : 列表形式查看文件信息, 包含文件权限、所属用户/组、文件大小、文件名称等
            + -R : 递归方式查看当前文件夹下所有的子文件、子文件中的子文件
        
        + cd : 改变当前工作路径
            + `cd path ` : 在命令行切换不同的路径
            + cd / : 进入系统根目录
            + cd ~ : 进入系统当前用户目录
            + cd . : 一个符号 . 表示当前路径
            + cd .. : 两个符号 .. 表示上级/父级路径
        
        + pwd : 查看当前工作路径
        
        + ifconfig : 查看当前网络配置信息 (linux  系统中查看网卡网络信息的命令)
        
        + poweroff : 关闭计算机 (CentOS 中关机)
        
        + shutdown : 关闭计算机 (执行命令后会延时关机) 
            + `shutdown -r now` : 立刻重启计算机
            + `shutdown -r 10` : 10 分钟后重启系统
            + `shutdown -r 20:35` : 指定时间重启系统
            + `shutdown -h now` : 立刻关闭计算机
            + `shutdown -h 10` : 10 分钟后关闭计算机
            + `shutdown -c` : 取消 shutdown 命令执行的操作
        
        + reboot : 重启计算机
        
        + grep : 数据检索命令 (用于过滤/搜索特定字符 (串)，常配合管道命令使用)
            + `grep 需要搜索的字符串/要被搜索的文件`
            + -i | -ignore-case : 忽略字符大小写
        
        + | : 管道符号, 连接多个命令 (将第一个命令的输出结果，作为第二个命令的输入)
            
        + 基本语法 : `$ 命令1 | 命令2 | 命令3`
            
        + find : 文件检索命令
            + 语法格式 : `$ find path -option [-print] [-exec -ok command] {} \`
                + path : 命令所查找的目录路径
                + -print : 命令将匹配的文件输出到标准输出
                + -exec : 命令对匹配的文件执行该参数所给出的 shell 命令, 相应命令的形式为 ' command' {} \
                + -ok : 和 -exec 的作用相同,只不过以一种更为安全的模式来执行该参数所给出的 shell 命令, 在执行每一个命令时，都会给出提示
                + -name filename : 查找名为 filename 的文件
                + -type b/d/c/p/l/f : 按照文件类型查询指定的文件
                + -size n[c] : 按照文件大小查询指定的文件
                    ```
                  find /home -size +512k  # 查找 /home 目录下大于 512k 的文件
                  find /home -size -512k  # 查找 /home 目录下小于 512k 的文件
                  ```
                + -perm : 按照文件权限查询指定的文件
                    ```
                  find /home -perm 0700  # 查权限为 700 的文件或目录
                  ```
                + -user username : 查询文件用户是 username 的文件
                + -group groupname : 查询文件所属组 groupname 的文件
                + -mtime -n +n : 查询修改时间: ① +n : n 天前 ② -n : n天后的文件
                + -amin : 查询修改时间: ① +n : n 分钟前 ② -n : n分钟后的文件
                + -atime -n +n : 查询访问时间: ① +n : n 天前 ② -n : n天后的文件
                + -ctime -n +n : 查询创建时间: ① +n : n 天前 ② -n : n天后的文件
                + -newer f1 !f2 : 查询更改时间比 f1 新但是比 f2 旧的文件
                + -depth : 查询的递归子目录深度, 默认全部递归查询
                + -links n[c]: 按照 文件硬连接数 查询文件
                    ```
                  find /home -links +2  # 查硬连接数大于 2 的文件或目录
                  find / -empty  # 查找系统中为空的文件或文件夹
                  find / -nouser    # 查找在系统中属于作废用户的文件
                  find / -amin -10  # 查找在系统中最后 10 分钟访问的文件夹
                  ```