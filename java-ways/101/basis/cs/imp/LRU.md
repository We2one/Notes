```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-19 17:35:22
   Modified by: Gentleman.Hu
   Modified time: 2020-10-20 15:01:46
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description: LRU算法实现
 ```

## LRU 算法实现

Least Recently Used

> [source_from_csdn](https://blog.csdn.net/elricboa/article/details/78847305) 

设计原则:如果一个`数据`在对近一段时间`没有被访问到`,那么在将来他被访问的可能性也很小.就是说,当限定的空间已存满数据时,应当把`最久没有被访问到`的`数据`淘汰.

- 实现方法
  1. 用一个数组存储数据,给每个数据项标记一个访问时间戳,每次插入新数据项的时候,先把数组中存在的数据项的时间戳自增,并将新数据项的时间戳置为0并插入到数组中.每次访问数组中的数据项的时候,将被访问的数据项的时间戳置为0.当数据空间已满时,将时间戳最大的数据项淘汰.
  2. 利用一个链表实现,每次新插入数据的时候将新数据插到链表的头部;每次缓存命中(数据被访问),则将数据移到链表头部;那么当链表满的时候,就将表尾部的数据丢弃.
  3. 利用链表和hashmap.当需要插入新得数据项的时候,如果新数据项在链表中存在(命中),则把该节点移动到链表头部,如果不存在,则新建节点,放在链表头部,若缓存满了,则把链表最后一个节点删除即可.在访问数据的时候,如果数据项在链表中存在,则把该节点移动到链表头部,否则返回-1.这样链表尾部节点就是最近最久未访问数据项.

- 评价
  1. 需要不停维护数据项访问时间戳,insert,delete和访问数据时间复杂度都是O(n).
  2. 链表在定位数据时候时间复杂度为O(n).

实际多采用第三种实现

- LRU算法对比

| 对比点 | 对比                     |
| ------ | ------------------------ |
| 命中率 | LRU-2 > MQ(2) > 2Q > LRU |
| 复杂度 | LRU-2 > MQ(2) > 2Q > LRU |
| 代价   | LRU-2 > MQ(2) > 2Q > LRU |

### 具体实现

1. LinkedHashMap实现

```java
public class LRU<K,V>{
  private static final float hashLoadFactory = 0.75f;
  private LinkedHashMap<K,V> map;
  private int cacheSize;

  public LRU(int cacheSize){
    this.cacheSize = cacheSize;
    // Math.ceil(double x) - 返回参数值的
    int capacity = (int)Math.ceil(cacheSize/hashLoadFactory)+1;
    map = new LinkedHashMap<K,V>(capacity,hashLoadFactory,true){
      private static final long serialVersionUID = 1L;
      
      @Override
      protected boolean removeEldestEntry(Map.Entry eldest){
        return size()>LRU.this.cacheSize;
      }
    };
  }

  public synchronized V get(K key){
    return map.get(key);
  }

  public synchronized void put(K key,V value){
    map.put(key,value);
  }

  public synchronized void clear(){
    map.clear();
  }
}
```

## References

- Math.ceil()和Math.floor()和Math.round()区别

这三个方法分别遵循下列舍入规则：

- Math.ceil()执行向上舍入，即它总是将数值向上舍入为最接近的整数；
- Math.floor()执行向下舍入，即它总是将数值向下舍入为最接近的整数；
- Math.round()执行标准舍入，即它总是将数值四舍五入为最接近的整数(这也是我们在数学课上学到的舍入规则)。