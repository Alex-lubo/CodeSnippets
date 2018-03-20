## the Object in javascript

javacript中的简单类型:
  - numbers
  - strings
  - booleans
  - null
  - undefind

其中number， string和boolean有些像对象因为他们也有方法，但是它们不是可以随意变化。除去这些基本数据类型，js中的其它的一切都是对象，数组是对象，函数是对象，正则表达式也是对象。
JS中的对象是可修改的的键值对标示的属性值的组合。属性名称可以时任意字符串，属性值可以为除undefined之外的任意值或对象。
对象标示：
```
var empty_object = {}
var object = {
  'a': '1',
  'b': 1
}
```

JS中的对象分两种。
 - 普通对象
 - 函数对象

其中普通对象即一般的对象。而函数对象是指通过构造函数（new）创造出来的对象.