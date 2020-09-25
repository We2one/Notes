## Java与Oracle数据库各种操作

### 链接数据库

```java
//step1 load the driver class  
Class.forName("oracle.jdbc.driver.OracleDriver");  
  
//step2 create  the connection object  
Connection con=DriverManager.getConnection(  
"jdbc:oracle:thin:@localhost:1521:xe","system","oracle");  
  
//step3 create the statement object  
Statement stmt=con.createStatement();  
  
//step4 execute query  
ResultSet rs=stmt.executeQuery("select * from emp");  
while(rs.next())  
System.out.println(rs.getInt(1)+"  "+rs.getString(2)+"  "+rs.getString(3));  
  
//step5 close the connection object  
con.close();  
```

1. 加载drive类
2. 建立连接
3. 通过Connection创建Statement对象
4. 建立ResultSet对象以接受Statement执行的query结果
5. 关闭连接

## 相关链接

- [Java Database Connectivity](https://www.javatpoint.com/example-to-connect-to-the-oracle-database)

- [Official Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e12137/getconn.htm#TDPJD127)