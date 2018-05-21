# Elasticsearch的学习

time: 2018.4.12
---
---

学习资料: 官网文档 - [elasticsearch权威指南](https://www.elastic.co/guide/cn/elasticsearch/guide/current/index.html)

几个问题:
- es存什么数据?
- es如何存数据?
- es如何取数据?
- es如何查数据?
- es如何分析数据?

### es存什么样的数据
首先搞清楚为什么用es. 
1. es不是关系型数据库, 
2. 对象数据不是简单的key-value对,用关系型数据库来存势必要将数据进行扁平化处理,而取出时又需要做还原.
3. es是面向文档的,直接存整个对象(文档),
4. es可以存文档,也可以索引文档

### es如何存数据
es中存储数据叫Index.
要保证所有属性能够被搜索到,es使用倒排索引.
 - Index 与 分片
es的Index实际上是指向一个或者多个物理 分片 的 逻辑命名空间.
一个 分片 是一个底层的 工作单元 ，它仅保存了 全部数据中的一部分。一个分片是一个 Lucene 的实例，它本身就是一个完整的搜索引擎。 
文档被存储和索引到分片内，但是应用程序是直接与Index而不是与分片进行交互。一个分片可以是 主 分片或者 副本 分片。 
索引内任意一个文档都归属于一个主分片，所以主分片的数目决定着索引能够保存的最大数据量。一个副本分片只是一个主分片的拷贝。 副本分片作为硬件故障时保护数据不丢失的冗余备份，并为搜索和返回文档等读操作提供服务。

在索引建立的时候就已经确定了主分片数，但是副本分片数可以随时修改。

- 倒排索引

1.The quick brown fox jumped over the lazy dog
2.Quick brown foxes leap over lazy dogs in summer

Term      Doc_1  Doc_2
-------------------------
Quick   |       |  X
The     |   X   |
brown   |   X   |  X
dog     |   X   |
dogs    |       |  X
fox     |   X   |
foxes   |       |  X
in      |       |  X
jumped  |   X   |
lazy    |   X   |  X
leap    |       |  X
over    |   X   |  X
quick   |   X   |
summer  |       |  X
the     |   X   |
------------------------