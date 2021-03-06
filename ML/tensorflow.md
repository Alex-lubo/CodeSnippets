# Tensorflow concepts

* Graph
  - node: operation
  - edge: tensor
    
    control dependencies
* Session

在单个硬件设备的情况下,计算图会按照依赖关系被顺序执行.当一个节点的所有上游依赖被执行完成时(依赖数为0), 这个节点会被加入ready-queue以等待执行,同时,它下游的依赖数减1.

当有多个硬件设备时, tensorflow有一套为节点分配设备的策略.这个策略的流程是:
1. 计算一个代价模型, 这个代价模型估算每一个节点的输入和输出tensor的大小,以及所需要计算的时间.

    计算方法
    * 人工经验制定的启发式规则
    * 对一小部分数据进行实际计算测量得到
2. 模拟执行计算整个计算图, 从起点开始,按照拓扑顺序执行.模拟执行一个节点时,会在所有能进行计算的设备上都测试一遍,这个测试所用的时间包括计算的时间和传送数据需要的通信时间,最后选择一个综合时间最短的设备作为这个节点的运算设备.
3. 内存的最高使用峰值也会被考虑进来
4. 允许用户对节点的分配设置限定条件.

设备节点间的数据通信
当节点分别设备的方案被确定,整个计算图会被划分为许多子图,使用同一个设备并且相邻的节点会被划分到同一个子图.然后计算图中从x-y的边会被发送端的发送节点到接收端的接收节点的边取代.