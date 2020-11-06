```yaml
   Author: Gentleman.Hu
   Create Time: 2020-11-06 16:17:19
   Modified by: Gentleman.Hu
   Modified time: 2020-11-06 17:21:24
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description: 一些vim进阶用法
 ```

## 基础

符号 | 对应单词 | 含义
---------|----------|---------
 y | yank | 拷贝, 大写yank到行尾
 t | till | 直到
 c | change | 改
 g | not sure(namespace) | "go"
 a | append | 小写后插,大写前插
 o | not sure | 小写下行插,大写上行插
 d | delete | 小写跟数字,删除指定数量,大写从cursor删到行尾
 ~ | 改变大小写| 改变大小写 |
 p | put | 寄存器存的内容放在cursor后,大写放之前.前边跟数字,放置n遍
 e | end | 末尾
 $ | end | 末尾
 0 | start | 首
 % | not sure | 匹配到对应括号
 z | not sure | z. cursor居中屏幕;zt,top;zb,bottom
 * | mark/star | 快速标记

- 上表并不完整, 列举仅仅常用

## 用例实践

- 多行添加注释

![](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20201106165738.gif)

- gt+"字符",删除直到某个"字符"

![](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20201106170133.gif)

- 其他慢慢探索

## Macro用例实践

- 简单加引号

![](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20201106171938.gif)

- 其他用例可参照资源, 各种玩法, 等待探索

## Resources

- [油管_大神](https://www.youtube.com/watch?v=IiwGbcd8S7I)
- [vim_micros](https://spin.atomicobject.com/2014/11/23/record-vim-macros/)
- [stack_exchange_what_is_meaning_of_blabla_invim](https://vi.stackexchange.com/a/18745)
- [vim_CheatSheet](https://www.fprintf.net/vimCheatSheet.html)
- [dot_command_in_vim](https://stackoverflow.com/a/7325105)