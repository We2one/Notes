### Pandas

#### 数据处理

##### 数据集成 (合并)

+ 合并数据

  + `pd.concat(objs: Union[Iterable[FrameOrSeries], Mapping[Label, FrameOrSeries]], axis=0, join="outer", ignore_index: bool = False, keys=None, levels=None, names=None, verify_integrity: bool = False, sort: bool = False, copy: bool = True,)`

    + 参数

      | 参数                 | 描述                                                         |
      | -------------------- | ------------------------------------------------------------ |
      | **objs**             | series，dataframe或者是panel构成的序列lsit,用来传入多个连接的对象 |
      | **axis**             | 需要合并链接的轴，0是行，1是列 **{0/'index', 1/'columns'}, default 0** |
      | **join**             | 连接的方式 inner(内连接)，或者outer(外连接)                  |
      | **ignore_index**     | bool,默认 False,如果为True，则不要沿连接轴使用索引值         |
      | **keys**             | 可迭代序列,如果需要保留来源信息，就可以通过keys参数进行设置  |
      | **levels**           | 列表或序列,用于构造多重索引的特定级别（唯一值）。否则将从键中推断出它们。 |
      | **names**            | 给拼接后形成的数据结构添加名字                               |
      | **verify_integrity** | bool,默认 False,检查新的连接轴是否包含重复项                 |
      | **sort**             | bool,默认 False,“join”为“outer”时，如果非连接轴尚未对齐，请对其排序。 |
      | **copy**             | bool,默认 True,                                              |

    + 横向合并 **axis=1** (左右合并)

      + 使用场景 : 
      + **合并与连接**
        + 在列的方向上直接合并 (直接堆叠), 存在重复列名并不进行删除
        + 在行的方向上 根据连接方式 **join** 对行索引进行合并
          + 如果连接方式是外连接**outer** ---> 行索引并集
          + 如果连接方式是内连接**inner** ---> 行索引交集
          + 如果两个 DataFrame 的行索引一致，内连接外连接结果一致

    + 纵向合并 **axis=0** (上下合并)

      + 使用场景
      + **合并与连接**
        + 在列的方向上 根据连接方式 **join** 对行索引进行合并
          + 如果连接方式是外连接**outer** ---> 列索引并集
          + 如果连接方式是内连接**inner** ---> 列索引交集

  + `DF_name.append(self, other, ignore_index=False, verify_integrity=False, sort=False)` : 只可以上下合并

    + 应用场景 : 适用于列索引一致的情况 `df1.append(df2)`

    + 参数

      | 参数                 | 描述                                                         |
      | -------------------- | ------------------------------------------------------------ |
      | **other**            | DataFrame、series、dict、list这样的数据结构                  |
      | **ignore_index**     | 默认值为False，如果为True则不使用index标签                   |
      | **verify_integrity** | 默认值为False，如果为True当创建相同的index时会抛出ValueError的异常 |
      | **sort**             | boolean，默认是None                                          |

  + `pd.merge(left, right, how: str = "inner", on=None, left_on=None, right_on=None, left_index: bool = False, right_index: bool = False, sort: bool = False, suffixes=("_x", "_y"), copy: bool = True, indicator: bool = False, validate=None,)` :主键合并, 只能**左右合并** (默认内连接)

    + 参数

      | 参数            | 描述                                                         |
      | --------------- | ------------------------------------------------------------ |
      | **left**        | 拼接的左侧DataFrame对象                                      |
      | **right**       | 拼接的右侧DataFrame对象                                      |
      | **how**         | **{‘left’, ‘right’, ‘outer’, ‘inner’}**. 默认inner。<br>&emsp;**inner**内连接, 取交集，<br>&emsp;**outer**外连接,取并集。<br>&emsp;**left** 左连接,以左表为主<br>&emsp;**right** 右连接,以右表为主<br>&emsp;比如left：[‘A’,‘B’,‘C’];right[’'A,‘C’,‘D’]；inner取交集的话，left中出现的A会和right中出现的一个A进行匹配拼接，如果没有是B，在right中没有匹配到，则会丢失。'outer’取并集，出现的A会进行一一匹配，没有同时出现的会将缺失的部分添加缺失值 |
      | **on**          | 要加入的列或索引级别名称。 必须在左侧和右侧DataFrame对象中找到。 如果未传递且left_index和right_index为False，则DataFrame中的列的交集将被推断为连接键。 |
      | **left_on**     | 左侧DataFrame中的列或索引级别用作键 (主键)。 可以是列名，索引级名称，也可以是长度等于DataFrame长度的数组 |
      | **right_on**    | 右侧DataFrame中的列或索引级别用作键 (主键)。 可以是列名，索引级名称，也可以是长度等于DataFrame长度的数组。 |
      | **left_index**  | 如果为True，则使用左侧DataFrame中的索引（行标签）作为其连接键。 对于具有MultiIndex（分层）的DataFrame，级别数必须与右侧DataFrame中的连接键数相匹配。 |
      | **right_index** | 与left_index功能相似。                                       |
      | **sort**        | 按字典顺序通过连接键对结果DataFrame进行排序。 默认为True，设置为False将在很多情况下显着提高性能。 |
      | **suffixes**    | 用于重叠列 (重名列) 的字符串后缀元组。 默认为（‘* x’，’* y’）。 |
      | **copy**        | 始终从传递的DataFrame对象复制数据（默认为True），即使不需要重建索引也是如此 |
      | **indicator**   | 将一列添加到名为_merge的输出DataFrame，其中包含有关每行源的信息。 _merge是分类类型，并且对于其合并键仅出现在“左”DataFrame中的观察值，取得值为left_only，对于其合并键仅出现在“右”DataFrame中的观察值为right_only，并且如果在两者中都找到观察点的合并键，则为left_only |

    + `DF_name1.combine_first(DF_name2)` : 重叠合并 (将两个不完整的 DF [列索引相同] 进行合并
    
      + 主表中空值的位置 使用第二个表中的非空值进行填充
      + 选择空值较少的作为主表
  