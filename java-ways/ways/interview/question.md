```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-20 18:03:17
   Modified by: Gentleman.Hu
   Modified time: 2020-10-20 22:26:55
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description:
 ```

## 面试题

- SOAP,WSDL,UDDI了解?
  - [csdn](https://blog.csdn.net/fupengyao/article/details/51612069)
  ```md
  1、SOAP 即 Simple Object AccessProtocol 也就是简单对象访问协议。 SOAP 是用于在应用程序之间进行通信的一种通信协议。SOAP 基于XML 和 HTTP ，其通过XML 来实现消息描述，然后再通过 HTTP 实现消息传输。 SOAP 协议的一个重要特点是它独立于底层传输机制，Web 服务应用程序可以根据需要选择自己的数据传输协议， 可以在发送消息时来确定相应传输机制。 2、WSDL 即Web Services Description Language也就是 Web 服务描述语言。 服务提供者通过服务描述将所有用于访问 Web服务的规范传送给服务请求者，通过服务描述便可以不必了解对方的底层平台，编程语言等。（服务所提供的操作、如何访问服务、服务位于何处） 3、UDDI 即 Universal Description，Discovery and Integration，也就是通用的描述，发现以及整合。 WSDL 呢，用来描述了访问特定的 Web 服务的一些相关的信息，可以在互联网上，或者是在企业的不同部门之间。 UDDI的话，是一个跨产业，跨平台的开放性架构，可以帮助 Web 服务提供商在互联网上发布 Web 服务的信息。 UDDI 呢是一种目录服务，企业可以通过 UDDI 来注册和搜索 Web 服务。 简单来时候话，UDDI 就是一个目录，只不过在这个目录中存放的是一些关于 Web 服务的信息而已。
  ```
  
- JDO(JAVA Data Object)
- 谈谈Java规范中和WebService相关的规范有哪些？
  - [csdn](https://blog.csdn.net/troubleshooter/article/details/78455036)
  ```md
  JAVA ***同拥有三种WebService 规范，各自是JAXM&SAAJ、JAX-WS（JAX-RPC）、JAX-RS。
- JAX-WS(JSR 224)：这个规范是早期的基于SOAP的Web Service规范JAX-RPC的替代版本，它并不提供向下兼容性，因为RPC样式的WSDL以及相关的API已经在Java EE5中被移除了。WS-MetaData是JAX-WS的依赖规范，提供了基于注解配置Web Service和SOAP消息的相关API。
- JAXM(JSR 67)：定义了发送和接收消息所需的API,相当于Web Service的服务器端。
- JAX-RS(JSR 311 & JSR 339 & JSR 370)：是Java针对REST（Representation State Transfer）架构风格制定的一套Web Service规范。REST是一种软件架构模式，是一种风格，它不像SOAP那样本身承载着一种消息协议， (两种风格的Web Service均采用了HTTP做传输协议，因为HTTP协议能穿越防火墙，Java的远程方法调用（RMI）等是重量级协议，通常不能穿越防火墙），因此可以将REST视为基于HTTP协议的软件架构。REST中最重要的两个概念是资源定位和资源操作，而HTTP协议恰好完整的提供了这两个点。HTTP协议中的URI可以完成资源定位，而GET、POST、OPTION、DELETE方法可以完成资源操作。因此REST完全依赖HTTP协议就可以完成Web Service，而不像SOAP协议那样只利用了HTTP的传输特性，定位和操作都是由SOAP协议自身完成的，也正是由于SOAP消息的存在使得基于SOAP的Web Service显得笨重而逐渐被淘汰。
	```

- 操作系统里的内存碎片你怎么理解，有什么解决办法？

- 怎么杀死进程？