Here are the digest collected by fix es-perfermance issues:

1.每个Elasticsearch节点内部都维护着多个线程池，如index、search、get、bulk等，用户可以修改线程池的类型和大小，线程池默认大小跟CPU逻辑一致.
查看当前线程组状态:
    curl -XGET 'http://localhost:9200/_nodes/stats?pretty'  

"thread_pool" : {  
    "bulk" : {  
      "threads" : 32,  
      "queue" : 0,  
      "active" : 0,  
      "rejected" : 0,  
      "largest" : 32,  
      "completed" : 659997  
    },  
"index" : {  
      "threads" : 2,  
      "queue" : 0,  
      "active" : 0,  
      "rejected" : 0,  
      "largest" : 2,  
      "completed" : 2  
    }  

最需要关注的是rejected。当某个线程池active==threads时，表示所有线程都在忙，那么后续新的请求就会进入queue中，即queue>0，一旦queue大小超出限制，如bulk的queue默认50，那么elasticsearch进程将拒绝请求（碰到bulk HTTP状态码429），相应的拒绝次数就会累加到rejected中。
解决方法是
1、记录失败的请求并重发
2、减少并发写的进程个数，同时加大每次bulk请求的size

核心线程池
generic：通用操作，如node discovery。它的类型默认为cached。
index：此线程池用于索引和删除操作。它的类型默认为fixed，size默认为可用处理器的数量，队列的size默认为200。
search：此线程池用于搜索和计数请求。它的类型默认为fixed，size默认为(可用处理器的数量* 3) / 2) + 1，队列的size默认为1000。
suggest：此线程池用于建议器请求。它的类型默认为fixed，size默认为可用处理器的数量，队列的size默认为1000。
get：此线程池用于实时的GET请求。它的类型默认为fixed，size默认为可用处理器的数量，队列的size默认为1000。
bulk：此线程池用于批量操作。它的类型默认为fixed，size默认为可用处理器的数量，队列的size默认为50。
percolate：此线程池用于预匹配器操作。它的类型默认为fixed，size默认为可用处理器的数量，队列的size默认为1000。


``线程池类型
1. cached
无限制的线程池，为每个请求创建一个线程。这种线程池是为了防止请求被阻塞或者拒绝，其中的每个线程都有一个超时时间(keep_alive)，默认5分钟，一旦超时就会回收/终止。elasticsearch的generic线程池就是用该类型。最近发现5.0.0-alpha2版本中去掉了该类型的线程池。

2. fixed
有着固定大小的线程池，大小由size属性指定，默认是5*cores数，允许你指定一个队列（使用queue_size属性指定，默认是-1，即无限制）用来保存请求，直到有一个空闲的线程来执行请求。如果Elasticsearch无法把请求放到队列中（队列满了），该请求将被拒绝。

3. scaling
可变大小的pool，大小根据负载在1到size间，同样keep_alive参数指定了闲置线程被回收的时间。


错误处理
out of memory错误
因为默认情况下es对字段数据缓存（Field Data Cache）大小是无限制的，查询时会把字段值放到内存，特别是facet查询，对内存要求非常高，它会把结果都放在内存，然后进行排序等操作，一直使用内存，直到内存用完，当内存不够用时就有可能出现out of memory错误。
解决方法：
（1）设置es的缓存类型为Soft Reference，它的主要特点是据有较强的引用功能。只有当内存不够的时候，才进行回收这类内存，因此在内存足够的时候，它们通常不被回收。另外，这些引 用对象还能保证在Java抛出OutOfMemory 异常之前，被设置为null。它可以用于实现一些常用图片的缓存，实现Cache的功能，保证最大限度的使用内存而不引起OutOfMemory。在es的配置文件加上index.cache.field.type: soft即可。
（2）设置es最大缓存数据条数和缓存失效时间，通过设置index.cache.field.max_size: 50000来把缓存field的最大值设置为50000，设置index.cache.field.expire: 10m把过期时间设置成10分钟。