最近客户机房因为供电局突然断电，导致服务启动出问题。远程过去看后发现挂进去的磁盘/dev/sdb1报错：
```
EXT4-fs (/dev/sdb1):error:ext2_lookup deleted inode referenced 255443
```
很明显：磁盘文件系统错误。
该如何解决呢？
服务是运行在VirtualBox中虚拟机（ubuntu）中的docker， sdb1是从ubuntu中挂进docker的磁盘，存储数据，这样即便Docker服务重新部署或删除，用户的数据可以依然保留。
既然磁盘文件错误，那就尝试修复一下呗。
使用linux下的fsck工具。命令行执行：
```
# fsck -y /dev/sdb1
```
结果报错：
```
/dev/sdb1 is in use, 
cannot continue, aborting.
```
因为程序运行，磁盘内文件正在使用，因此需要首先关闭运行的程序，并且需要经磁盘umount，运行如下命令：
```
# fuser -mk /dev/sdb1   //查找目录文件占用的进程并关闭
# umount -l /dev/sdb1
# fsck -y /dev/sdb1
```
程序会检测并修复磁盘文件。
然后重启机器，问题解决。
