---
   Author: Gentleman.Hu
   Create Time: 2020-09-25 18:56:23
   Modified by: Gentleman.Hu
   Modified time: 2020-09-25 19:01:01
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description: Java中DateForamtt各种范例
 ---

## Java中DateFormat各种范例

1. DateFormat Example: Formatting the Date and Time using SHORT, MEDIUM and LONG Fields

```java
import java.text.DateFormat;  
import java.util.Date; 
class Example{
   public static void main(String args[]){
	   
       Date currentDate = new Date();  
       System.out.println("Current date is: "+currentDate); 
       
       String dateShort = DateFormat.getDateInstance(DateFormat.SHORT).format(currentDate);  
       System.out.println("Formatting the Date using DateFormat.SHORT: "+dateShort);  
 
       String dateMedium = DateFormat.getDateInstance(DateFormat.MEDIUM).format(currentDate);  
       System.out.println("Formatting the Date using DateFormat.MEDIUM: "+dateMedium);  
         
       String dateLong = DateFormat.getDateInstance(DateFormat.LONG).format(currentDate);  
       System.out.println("Formatting the Date using DateFormat.LONG: "+dateLong); 
       
       String timeShort = DateFormat.getTimeInstance(DateFormat.SHORT).format(currentDate);  
       System.out.println("Formatting the Time using DateFormat.SHORT: "+timeShort);  
 
       String timeMedium = DateFormat.getTimeInstance(DateFormat.MEDIUM).format(currentDate);  
       System.out.println("Formatting the Time using DateFormat.MEDIUM: "+timeMedium);  
         
       String timeLong = DateFormat.getTimeInstance(DateFormat.LONG).format(currentDate);  
       System.out.println("Formatting the Time using DateFormat.LONG: "+timeLong); 
   }
}
```
Output:

```yaml
Current date is: Thu Oct 19 20:54:44 IST 2017
Formatting the Date using DateFormat.SHORT: 19/10/17
Formatting the Date using DateFormat.MEDIUM: 19 Oct, 2017
Formatting the Date using DateFormat.LONG: 19 October, 2017
Formatting the Time using DateFormat.SHORT: 8:54 PM
Formatting the Time using DateFormat.MEDIUM: 8:54:44 PM
Formatting the Time using DateFormat.LONG: 8:54:44 PM IST
```
2. DateFormat Example: Converting the Date to String

```java
import java.text.DateFormat;  
import java.util.Date;  
public class Example {  
    public static void main(String[] args) {  
        Date date = new Date();  
        System.out.println("Date is: "+date);  
        String dateString = DateFormat.getDateInstance().format(date);  
        System.out.println("Converting Date to String: "+dateString);  
    }  
}
```
Output:
```yaml
Date is: Thu Oct 19 21:04:16 IST 2017
Converting Date to String: 19 Oct, 2017
```
3. DateFormat Example: String to Date conversion using parse() method

```java
import java.text.DateFormat;  
import java.util.Date;  
public class Example {  
    public static void main(String[] args)throws Exception {  
    	//Date in String format
    	String dateString = "11 Oct, 2017";
    	//Converting the String to date using DateFormat
        Date date = DateFormat.getDateInstance().parse(dateString); 
        //Displaying the Date
        System.out.println("Date: "+date);  
    }  
}
```
Output:
```yaml
Date: Wed Oct 11 00:00:00 IST 2017
```

## 相关链接

- [refer](https://beginnersbook.com/2013/04/java-date-format/)
