```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-03 15:28:51
   Modified by: Gentleman.Hu
   Modified time: 2020-10-07 16:11:55
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description:
 ```

## JDBC与连接池
> [QuickGuide](https://www.tutorialspoint.com/jdbc/jdbc-quick-guide.htm)
> Java DataBase COnnectivity

### JDBC与基本CRUD

#### 基本

- 基本步骤
  - 注册驱动
  - 建立连接
  - 获取数据库连接对象(Connection)
  - 定义sql语句
  - 获取sql执行对象(Statement)
  - 执行sql,获取结果
  - 处理结果
  - 关闭连接,释放资源

- OnAction
  1. 引入包`import java.sql.*;`
  2. 注册驱动`Class.forName("com.mysql.jdbc.Driver)`
  3. 建立连接
   ```java
   static final String USER = "username";
   static final String PASS = "password";
   System.out.println("Connecting to database...);
   conn = DriverManager.getConnection(DB_URL,USER,PASS);
   ```
  4. 执行sql
   ```java
   System.out.println("Creating statement ...);
   stmt = conn.createStatement();
   String sql;
   sql = "select * from one_table";
   ResultSet rs = stmt.executeQuery(sql);
   ```
  5. 处理结果
   ```java
   while(rs.next()){
         int id  = rs.getInt("id");
    int age = rs.getInt("age");
    String first = rs.getString("first");
    String last = rs.getString("last");

    //Display values
    System.out.print("ID: " + id);
    System.out.print(", Age: " + age);
    System.out.print(", First: " + first);
    System.out.println(", Last: " + last);
   }
   ```
  6. 关闭连接,释放资源
   ```java
   rs.close();
   stmt.close();
   conn.close();
   ```

- Full

```java
  
  //STEP 1. Import required packages
import java.sql.*;

public class FirstExample {
   // JDBC driver name and database URL
   static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
   static final String DB_URL = "jdbc:mysql://localhost/EMP";

   //  Database credentials
   static final String USER = "username";
   static final String PASS = "password";
   
   public static void main(String[] args) {
   Connection conn = null;
   Statement stmt = null;
   try{
      //STEP 2: Register JDBC driver
      Class.forName("com.mysql.jdbc.Driver");

      //STEP 3: Open a connection
      System.out.println("Connecting to database...");
      conn = DriverManager.getConnection(DB_URL,USER,PASS);

      //STEP 4: Execute a query
      System.out.println("Creating statement...");
      stmt = conn.createStatement();
      String sql;
      sql = "SELECT id, first, last, age FROM Employees";
      ResultSet rs = stmt.executeQuery(sql);

      //STEP 5: Extract data from result set
      while(rs.next()){
         //Retrieve by column name
         int id  = rs.getInt("id");
         int age = rs.getInt("age");
         String first = rs.getString("first");
         String last = rs.getString("last");

         //Display values
         System.out.print("ID: " + id);
         System.out.print(", Age: " + age);
         System.out.print(", First: " + first);
         System.out.println(", Last: " + last);
      }
      //STEP 6: Clean-up environment
      rs.close();
      stmt.close();
      conn.close();
   }catch(SQLException se){
      //Handle errors for JDBC
      se.printStackTrace();
   }catch(Exception e){
      //Handle errors for Class.forName
      e.printStackTrace();
   }finally{
      //finally block used to close resources
      try{
         if(stmt!=null)
            stmt.close();
      }catch(SQLException se2){
      }// nothing we can do
      try{
         if(conn!=null)
            conn.close();
      }catch(SQLException se){
         se.printStackTrace();
      }//end finally try
   }//end try
   System.out.println("Goodbye!");
}//end main
}//end FirstExample
```

- 相关Exception表一览
  
| Method                         | Description                                                                                                                                                                                                     |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| getErrorCode( )                | Gets the error number associated with the exception.                                                                                                                                                            |
| getMessage( )                  | Gets the JDBC driver's error message for an error handled by the driver or gets the Oracle error number and message for a database error.                                                                       |
| getSQLState( )                 | Gets the XOPEN SQLstate string. For a JDBC driver error, no useful information is returned from this method. For a database error, the five-digit XOPEN SQLstate code is returned. This method can return null. |
| getNextException( )            | Gets the next Exception object in the exception chain.                                                                                                                                                          |
| printStackTrace( )             | Prints the current exception, or throwable, and its backtrace to a standard error stream.                                                                                                                       |
| printStackTrace(PrintStream s) | Prints this throwable and its backtrace to the print stream you specify.                                                                                                                                        |
| printStackTrace(PrintWriter w) | Prints this throwable and its backtrace to the print writer you specify.                                                                                                                                        |
- 用try catch finally包裹

```java
try {
   // Your risky code goes between these curly braces!!!
}
catch(Exception ex) {
   // Your exception handling code goes between these 
   // curly braces, similar to the exception clause 
   // in a PL/SQL block.
}
finally {
   // Your must-always-be-executed code goes between these 
   // curly braces. Like closing database connection.
}
```

- JDBC 中Data 类型对应表
  
| SQL         | JDBC/Java            | setXXX        | updateXXX        |
| ----------- | -------------------- | ------------- | ---------------- |
| VARCHAR     | java.lang.String     | setString     | updateString     |
| CHAR        | java.lang.String     | setString     | updateString     |
| LONGVARCHAR | java.lang.String     | setString     | updateString     |
| BIT         | boolean              | setBoolean    | updateBoolean    |
| NUMERIC     | java.math.BigDecimal | setBigDecimal | updateBigDecimal |
| TINYINT     | byte                 | setByte       | updateByte       |
| SMALLINT    | short                | setShort      | updateShort      |
| INTEGER     | int                  | setInt        | updateInt        |
| BIGINT      | long                 | setLong       | updateLong       |
| REAL        | float                | setFloat      | updateFloat      |
| FLOAT       | float                | setFloat      | updateFloat      |
| DOUBLE      | double               | setDouble     | updateDouble     |
| VARBINARY   | byte[ ]              | setBytes      | updateBytes      |
| BINARY      | byte[ ]              | setBytes      | updateBytes      |
| DATE        | java.sql.Date        | setDate       | updateDate       |
| TIME        | java.sql.Time        | setTime       | updateTime       |
| TIMESTAMP   | java.sql.Timestamp   | setTimestamp  | updateTimestamp  |
| CLOB        | java.sql.Clob        | setClob       | updateClob       |
| BLOB        | java.sql.Blob        | setBlob       | updateBlob       |
| ARRAY       | java.sql.Array       | setARRAY      | updateARRAY      |
| REF         | java.sql.Ref         | SetRef        | updateRef        |
| STRUCT      | java.sql.Struct      | SetStruct     | updateStruct     |

- 批处理 JDBC - Batch Processing

Batch Processing allows you to group related SQL statements into a batch and submit them with one call to the database.

When you send several SQL statements to the database at once, you reduce the amount of communication overhead, thereby improving performance.

- JDBC drivers are not required to support this feature. You should use the *DatabaseMetaData.supportsBatchUpdates()* method to determine if the target database supports batch update processing. The method returns true if your JDBC driver supports this feature.
- The **addBatch()** method of *Statement, PreparedStatement,* and *CallableStatement* is used to add individual statements to the batch. The **executeBatch()** is used to start the execution of all the statements grouped together.
- The **executeBatch()** returns an array of integers, and each element of the array represents the update count for the respective update statement.
- Just as you can add statements to a batch for processing, you can remove them with the **clearBatch()** method. This method removes all the statements you added with the addBatch() method. However, you cannot selectively choose which statement to remove.

- Streaming Data(流):

A PreparedStatement object has the ability to use input and output streams to supply parameter data. This enables you to place entire files into database columns that can hold large values, such as CLOB and BLOB data types.

There are following methods which can be used to stream data:

- **setAsciiStream():** This method is used to supply large ASCII values.
- **setCharacterStream():** This method is used to supply large UNICODE values.
- **setBinaryStream():** This method is used to supply large binary values.

The setXXXStream() method requires an extra parameter, the file size, besides the parameter placeholder. This parameter informs the driver how much data should be sent to the database using the stream.

#### 事务

> 事务：一个包含多个步骤的业务操作。如果这个业务操作被事务管理，则这多个步骤要么同时成功，要么同时失败。

使用Connection对象来管理事务

* 开启事务：setAutoCommit(boolean autoCommit) ：调用该方法设置参数为false，即开启事务
* 在执行sql之前开启事务
* 提交事务：commit() 
* 当所有sql都执行完提交事务
* 回滚事务：rollback() 
* 在catch中回滚事务

- 简单demo
```java
	public class JDBCDemo10 {

	    public static void main(String[] args) {
	        Connection conn = null;
	        PreparedStatement pstmt1 = null;
	        PreparedStatement pstmt2 = null;
	
	        try {
	            //1.获取连接
	            conn = JDBCUtils.getConnection();
	            //开启事务
	            conn.setAutoCommit(false);
	
	            //2.定义sql
	            //2.1 张三 - 500
	            String sql1 = "update account set balance = balance - ? where id = ?";
	            //2.2 李四 + 500
	            String sql2 = "update account set balance = balance + ? where id = ?";
	            //3.获取执行sql对象
	            pstmt1 = conn.prepareStatement(sql1);
	            pstmt2 = conn.prepareStatement(sql2);
	            //4. 设置参数
	            pstmt1.setDouble(1,500);
	            pstmt1.setInt(2,1);
	
	            pstmt2.setDouble(1,500);
	            pstmt2.setInt(2,2);
	            //5.执行sql
	            pstmt1.executeUpdate();
	            // 手动制造异常
	            int i = 3/0;
	
	            pstmt2.executeUpdate();
	            //提交事务
	            conn.commit();
	        } catch (Exception e) {
	            //事务回滚
	            try {
	                if(conn != null) {
	                    conn.rollback();
	                }
	            } catch (SQLException e1) {
	                e1.printStackTrace();
	            }
	            e.printStackTrace();
	        }finally {
	            JDBCUtils.close(pstmt1,conn);
	            JDBCUtils.close(pstmt2,null);
	        }
```

### 数据库连接池与JDBC Template

> [jdbc-jdbc-connection-pooling](https://www.progress.com/tutorials/jdbc/jdbc-jdbc-connection-pooling)

![](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20201007145250.png)

#### 基础连接池

> 一个容器(集合)，存放数据库连接的容器。
  当系统初始化好后，容器被创建，容器中会申请一些连接对象，当用户来访问数据库时，从容器中获取连接对象，用户访问完之后，会将连接对象归还给容器。

2. 好处：
	1. 节约资源
	2. 用户访问高效

3. 实现：
	 标准接口：DataSource   javax.sql包下的
4. 方法：
   * 获取连接：getConnection()
   * 归还连接：Connection.close()。如果连接对象Connection是从连接池中获取的，那么调用Connection.close()方法，则不会再关闭连接了。而是释放连接

5. 几个常见厂商实现的数据库连接池
   1. C3P0：数据库连接池技术
   2. Druid：数据库连接池实现技术，由阿里巴巴提供的
   
- c3p0配置文件
  - `c3p0.properties`或者`c3p0-config.xml`
  - 直接放置在`src`目录即可

- c3p0创建过程
  - ComboPooledDataSource
  - getConnection
  
  ```java
  DataSource ds = new ComboPooleddataSource();
  Connection conn = ds.getConnection();
  ```

- Druid:
  - 配置文件
    - 可以properties
    - 可以任意名称,任意位置
  - 过程
    - 加载配置文件.Properties
    - 通过工厂获取连接池对象.`DruidDataSourceFactory`
    - 获取连接:`getConnection`
  
  ```java
  Properties pro = new Properties();
  InputStream is = DruidDemo.class.getClassLoader().getResourceAsStream("druid.properties");
  pro.load(is);

  DataSource ds = DruidDataSourceFactory.createDataSource(pro);

  Connection conn = ds.getConnection();
  ```

  - Full in util class
  
  ```java
  public class JDBCUtils {

		    //1.定义成员变量 DataSource
		    private static DataSource ds ;
		
		    static{
		        try {
		            //1.加载配置文件
		            Properties pro = new Properties();
		            pro.load(JDBCUtils.class.getClassLoader().getResourceAsStream("druid.properties"));
		            //2.获取DataSource
		            ds = DruidDataSourceFactory.createDataSource(pro);
		        } catch (IOException e) {
		            e.printStackTrace();
		        } catch (Exception e) {
		            e.printStackTrace();
		        }
		    }
		
		    /**
		     * 获取连接
		     */
		    public static Connection getConnection() throws SQLException {
		        return ds.getConnection();
		    }
		
		    /**
		     * 释放资源
		     */
		    public static void close(Statement stmt,Connection conn){
		       /* if(stmt != null){
		            try {
		                stmt.close();
		            } catch (SQLException e) {
		                e.printStackTrace();
		            }
		        }
		
		        if(conn != null){
		            try {
		                conn.close();//归还连接
		            } catch (SQLException e) {
		                e.printStackTrace();
		            }
		        }*/
		
		       close(null,stmt,conn);
		    }
            public static void close(ResultSet rs , Statement stmt, Connection conn){
                if(rs != null){
                  try {
                      rs.close();
                  } catch (SQLException e) {
                      e.printStackTrace();
                  }
              }
              
                     if(stmt != null){
		            try {
		                stmt.close();
		            } catch (SQLException e) {
		                e.printStackTrace();
		            }
		        }
		
		        if(conn != null){
		            try {
		                conn.close();//归还连接
		            } catch (SQLException e) {
		                e.printStackTrace();
		            }
		        }
		    }
		
		    /**
		     * 获取连接池方法
		     */
		
		    public static DataSource getDataSource(){
		        return  ds;
		    }
		
		}
    ```

#### Spring JDBC

> [Spring_Guide](https://spring.io/guides/gs/relational-data-access/)
> [JavaPointTutorial](https://www.javatpoint.com/spring-JdbcTemplate-tutorial)

- Spring JDBCTemplate class method table

| No.  | Method                                                       | Description                                                  |
| :--- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 1)   | public int update(String query)                              | is used to insert, update and delete records.                |
| 2)   | public int update(String query,Object... args)               | is used to insert, update and delete records using PreparedStatement using given arguments. |
| 3)   | public void execute(String query)                            | is used to execute DDL query.                                |
| 4)   | public T execute(String sql, PreparedStatementCallback action) | executes the query by using PreparedStatement callback.      |
| 5)   | public T query(String sql, ResultSetExtractor rse)           | is used to fetch records using ResultSetExtractor.           |
| 6)   | public List query(String sql, RowMapper rse)                 | is used to fetch records using RowMapper.                    |

- Employee.java

```java
public class Employee {  
private int id;  
private String name;  
private float salary;  
//no-arg and parameterized constructors  
//getters and setters  
}  
```

- EmployeeDao.java

```java
import org.springframework.jdbc.core.JdbcTemplate;  
  
public class EmployeeDao {  
private JdbcTemplate jdbcTemplate;  
  
public void setJdbcTemplate(JdbcTemplate jdbcTemplate) {  
    this.jdbcTemplate = jdbcTemplate;  
}  
  
public int saveEmployee(Employee e){  
    String query="insert into employee values(  
    '"+e.getId()+"','"+e.getName()+"','"+e.getSalary()+"')";  
    return jdbcTemplate.update(query);  
}  
public int updateEmployee(Employee e){  
    String query="update employee set   
    name='"+e.getName()+"',salary='"+e.getSalary()+"' where id='"+e.getId()+"' ";  
    return jdbcTemplate.update(query);  
}  
public int deleteEmployee(Employee e){  
    String query="delete from employee where id='"+e.getId()+"' ";  
    return jdbcTemplate.update(query);  
}  
  
}  

```

- applicationContext.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>  
<beans  
    xmlns="http://www.springframework.org/schema/beans"  
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  
    xmlns:p="http://www.springframework.org/schema/p"  
    xsi:schemaLocation="http://www.springframework.org/schema/beans   
http://www.springframework.org/schema/beans/spring-beans-3.0.xsd">  
  
<bean id="ds" class="org.springframework.jdbc.datasource.DriverManagerDataSource">  
<property name="driverClassName" value="oracle.jdbc.driver.OracleDriver" />  
<property name="url" value="jdbc:oracle:thin:@localhost:1521:xe" />  
<property name="username" value="system" />  
<property name="password" value="oracle" />  
</bean>  
  
<bean id="jdbcTemplate" class="org.springframework.jdbc.core.JdbcTemplate">  
<property name="dataSource" ref="ds"></property>  
</bean>  
  
<bean id="edao" class="com.javatpoint.EmployeeDao">  
<property name="jdbcTemplate" ref="jdbcTemplate"></property>  
</bean>  
  
</beans>  
```

- Test.java

```java
import org.springframework.context.ApplicationContext;  
import org.springframework.context.support.ClassPathXmlApplicationContext;  
public class Test {  
  
public static void main(String[] args) {  
    ApplicationContext ctx=new ClassPathXmlApplicationContext("applicationContext.xml");  
      
    EmployeeDao dao=(EmployeeDao)ctx.getBean("edao");  
    int status=dao.saveEmployee(new Employee(102,"Amit",35000));  
    System.out.println(status);  
          
    /*int status=dao.updateEmployee(new Employee(102,"Sonoo",15000)); 
    System.out.println(status); 
    */  
          
    /*Employee e=new Employee(); 
    e.setId(102); 
    int status=dao.deleteEmployee(e); 
    System.out.println(status);*/  
      
}  
  
}  
```

#### Another(Not written by Gentleman.Hu)

* Spring框架对JDBC的简单封装。提供了一个JDBCTemplate对象简化JDBC的开发
* 步骤：
1. 导入jar包
2. 创建JdbcTemplate对象。依赖于数据源DataSource
	* JdbcTemplate template = new JdbcTemplate(ds);

3. 调用JdbcTemplate的方法来完成CRUD的操作
	* update():执行DML语句。增、删、改语句
	* queryForMap():查询结果将结果集封装为map集合，将列名作为key，将值作为value 将这条记录封装为一个map集合
		* 注意：这个方法查询的结果集长度只能是1
	* queryForList():查询结果将结果集封装为list集合
		* 注意：将每一条记录封装为一个Map集合，再将Map集合装载到List集合中
	* query():查询结果，将结果封装为JavaBean对象
		* query的参数：RowMapper
			* 一般我们使用BeanPropertyRowMapper实现类。可以完成数据到JavaBean的自动封装
			* new BeanPropertyRowMapper<类型>(类型.class)
	* queryForObject：查询结果，将结果封装为对象
		* 一般用于聚合函数的查询

4. 练习：
	* 需求：
		1. 修改1号数据的 salary 为 10000
		2. 添加一条记录
		3. 删除刚才添加的记录
		4. 查询id为1的记录，将其封装为Map集合
		5. 查询所有记录，将其封装为List
		6. 查询所有记录，将其封装为Emp对象的List集合
		7. 查询总记录数

	* 代码：
```java
import cn.itcast.domain.Emp;
import cn.itcast.utils.JDBCUtils;
import org.junit.Test;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;

import java.sql.Date;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;
import java.util.Map;

public class JdbcTemplateDemo2 {

    //Junit单元测试，可以让方法独立执行


​				
    //1. 获取JDBCTemplate对象
    private JdbcTemplate template = new JdbcTemplate(JDBCUtils.getDataSource());
    /**
      * 1. 修改1号数据的 salary 为 10000
      */
    @Test
    public void test1(){

        //2. 定义sql
        String sql = "update emp set salary = 10000 where id = 1001";
        //3. 执行sql
        int count = template.update(sql);
        System.out.println(count);
    }

    /**
      * 2. 添加一条记录
      */
    @Test
    public void test2(){
        String sql = "insert into emp(id,ename,dept_id) values(?,?,?)";
        int count = template.update(sql, 1015, "郭靖", 10);
        System.out.println(count);

    }

    /**
      * 3.删除刚才添加的记录
      */
    @Test
    public void test3(){
        String sql = "delete from emp where id = ?";
        int count = template.update(sql, 1015);
        System.out.println(count);
    }

    /**
      * 4.查询id为1001的记录，将其封装为Map集合
      * 注意：这个方法查询的结果集长度只能是1
      */
    @Test
    public void test4(){
        String sql = "select * from emp where id = ? or id = ?";
        Map<String, Object> map = template.queryForMap(sql, 1001,1002);
        System.out.println(map);
        //{id=1001, ename=孙悟空, job_id=4, mgr=1004, joindate=2000-12-17, salary=10000.00, bonus=null, dept_id=20}

    }

    /**
      * 5. 查询所有记录，将其封装为List
      */
    @Test
    public void test5(){
        String sql = "select * from emp";
        List<Map<String, Object>> list = template.queryForList(sql);

        for (Map<String, Object> stringObjectMap : list) {
            System.out.println(stringObjectMap);
        }
    }

    /**
      * 6. 查询所有记录，将其封装为Emp对象的List集合
      */

    @Test
    public void test6(){
        String sql = "select * from emp";
        List<Emp> list = template.query(sql, new RowMapper<Emp>() {

            @Override
            public Emp mapRow(ResultSet rs, int i) throws SQLException {
                Emp emp = new Emp();
                int id = rs.getInt("id");
                String ename = rs.getString("ename");
                int job_id = rs.getInt("job_id");
                int mgr = rs.getInt("mgr");
                Date joindate = rs.getDate("joindate");
                double salary = rs.getDouble("salary");
                double bonus = rs.getDouble("bonus");
                int dept_id = rs.getInt("dept_id");

                emp.setId(id);
                emp.setEname(ename);
                emp.setJob_id(job_id);
                emp.setMgr(mgr);
                emp.setJoindate(joindate);
                emp.setSalary(salary);
                emp.setBonus(bonus);
                emp.setDept_id(dept_id);

                return emp;
            }
        });


​				
        for (Emp emp : list) {
            System.out.println(emp);
        }
    }

    /**
      * 6. 查询所有记录，将其封装为Emp对象的List集合
      */

    @Test
    public void test6_2(){
        String sql = "select * from emp";
        List<Emp> list = template.query(sql, new BeanPropertyRowMapper<Emp>(Emp.class));
        for (Emp emp : list) {
            System.out.println(emp);
        }
    }

    /**
      * 7. 查询总记录数
      */

    @Test
    public void test7(){
        String sql = "select count(id) from emp";
        Long total = template.queryForObject(sql, Long.class);
        System.out.println(total);
    }

}
```