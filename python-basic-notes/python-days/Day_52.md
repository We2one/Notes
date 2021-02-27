#### Xpath 语法

#### XML 简介

+ Xpath 处理 HTML 文档
  1. 将 HTML 转换成 XML 文档
  2. 使用 XPath 查找 HTML 节点或元素

##### XML 介绍

+ XML 描述
  1. XML : 可拓展标记语言 (EXtensible Markup Language)
  2. XML 是一种标记性语言,类似 HTML
  3. XML 的设计宗旨是传输数据,而不是显示页面
  4. XML 的标签需要我们自行定义
  5. XML 的设计行为具有自我描述性
  6. XML 是 W3C 的推荐标准

##### XML 与 HTML 区别

+ XML 与 HTML 都是用于操作数据或结构数据的,结构上大致相同

+ 本质不同

  | 数据格式 | 描述                                                    | 设计目标                                                     |
  | -------- | ------------------------------------------------------- | ------------------------------------------------------------ |
  | XML      | Extensible Markup Language (可拓展标记语言)             | 传输和存储数据,其焦点是数据的内容                            |
  | HTML     | HyperText Markup Language (超文本标记语言)              | 显示数据以及如何更好显示数据                                 |
  | HTML DOM | Document Object Model for HTML (超文本标记文档对象模型) | 通过 HTML DOM 访问所有 HTML 元素,以及所包含的文本属性<br>可以对其中的内容进行修改和删除,同时也可以创造新的元素 |

  

##### XML 的节点关系

1. **父 (Parent)** : 每个元素及其属性都有一个 父节点.
2. **子 (Children)** : 元素节点可以有零个、一个或多个 子节点
3. **同胞 (Sibling)** : 拥有相同的父节点的同级节点
4. **先辈 (Ancestor)** : 某节点的父节点、父节点的父节点等
5. **后代 (Descenderant)** : 某个节点的子节点、子结点的子结点等

#### XPATH

##### XPATH 介绍 

+ XPath (XML Path Language) : 是在 XML 文档中查找信息的语言,可以用在 XML 文档中对元素和属性进行遍历

##### 选取节点

+ XPath 使用路径表达式来选取 XML 文档中的节点或者节点集.

+ 最常用的路径表达式

  | 表达式     | 描述                                                    |
  | ---------- | ------------------------------------------------------- |
  | `text()`   | 选取标签中内容                                          |
  | `nodename` | 选取此结点的所有子结点                                  |
  | `/`        | 从节点选取                                              |
  | `//`       | 从匹配选择的当前节点选择文档中的节点,而不考虑它们的位置 |
  | `.`        | 选取当前节点                                            |
  | `..`       | 选取当前节点的父节点                                    |
  | `@`        | 选取属性                                                |

  

##### 谓语 (Predicates)

+ 谓语用来查找某个特定的节点或者包含某个指定的值的节点,被嵌在方括号内

+ 谓语表达式及表达结果

  | 路径表达式                           | 结果                                                         |
  | ------------------------------------ | ------------------------------------------------------------ |
  | `/bookstore/book[1]`                 | 选取属于 bookstore 子元素的第一个 book 元素                  |
  | `/bookstore/book[last()]`            | 选取属于 bookstore 子元素的最后一个 book 元素                |
  | `/bookstore/book[last()-1]`          | 选取属于 bookstore 子元素的倒数第二个个 book 元素            |
  | `/bookstore/book[position()<3]`      | 选最前面两个属于 bookstore 元素的子元素 的 book 元素         |
  | `//title[@lang]`                     | 选取所有属性名为 lang 的属性的 title 元素                    |
  | `//title[@lang='eng']`               | 选取所有 title 元素,且这些元素有属性值为 eng 的 lang 属性    |
  | `/bookstore/book[price>35.00]`       | 选取 bookstore 元素的所有 book 元素,且其中的 price 元素的值需大于 35 |
  | `/bookstore/book[price>35.00]/title` | 选取 bookstore 元素的所有 book 元素 的所有 title 元素,且其中的 price 元素的值需大于 35 |

  

##### 选取未知节点

+ XPath 通过通配符选取未知的 XML 元素

  | 通配符   | 描述             | 举例                                                         |
  | -------- | ---------------- | ------------------------------------------------------------ |
  | `*`      | 匹配任何节点元素 | `/bookstore/*` : 选取 bookstore 元素的所有子元素 <br>`//*` : 选取文档的所有元素 |
  | `@*`     | 匹配任何属性节点 | `//title[@*]` : 选取所有带有属性的 title 元素                |
  | `node()` | 匹配任何类型节点 |                                                              |

  

##### 选取若干路径

+ `|` 运算符 : 可以选取若干个路径

+ 实例

   

  | 路径表达式                     | 结果                                     |
  | ------------------------------ | ---------------------------------------- |
  | **//book/title\|//book/price** | 选取 book 元素的所有 title 和 price 元素 |
  | **//title\|//price**           | 选取文档所有 title 和 price 元素         |

  

#### lxml 模块

##### lxml 简介与安装

+ lxml 是 python 的一个 HTML/XML 解析器
+ lxml 主要功能 : 解析提取 HTML/XML 数据,使用 XPath 语法快速定位特定元素以及节点信息
+ `pip install lxml`

##### lxml 初步使用

+ **解析 HTML 字符串** : lxml 可以自动修正 html 代码

  ```python
  # 导入 lxml
  from lxml import etree
  
  html_text = """
  xxxxx
  """
  # 初始化 xpath 解析对象
  html = etree.HTML(html_text)
  # 解析对象输出代码,代码类型为 bytes
  result = etree.tostring(html, encoding="utf-8")
  
  ```

  

+ **lxml 文件读取** : lxml 可以从文件中读取内容,使用 `etree.parse()`, 文件内容必须符合 xml 格式,如果标签缺失

  ```python
  # 带导入 lxml
  from lxml import etree
  
  # lxml 读取外部文件
  html = etree.parse('test.html')
  
  # 解析对象
  result = etree.string(html, pretty_print=True).decode("utf-8")
  ```

  

