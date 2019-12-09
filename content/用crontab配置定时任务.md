Title: 用crontab配置定时任务
Date: 2018-08-07 06:09
Author: PwnForWhat
Category: linux
Slug: 用crontab配置定时任务
Status: published

前段时间需要定期把一个服务器上的日志以邮件的形式发送到我的邮箱，于是了解了一下linux下定时任务的实现。

（本文假定阅读者有基本的linux操作能力）

linux下一般用crontab配置定时任务，本人用的是centos。

安装命令如下：

    yum install vixie-cron #cron主程序
    yum install crontab #crontab主体
    chkconfig -level 345 crond on #设置开机自启动

安装成功后打开crontab 配置

    vi /etc/crontab

然后 该文件布局如下（ **注意，以编辑crontab的方式运行定时任务不能省略用户名**）：

    m h d m weekday user  command

对应的分别是：

分钟 小时 日期 月份 星期 用户 命令

每个值的范围（不过不限制则为\*）

    0-59 0-23 1-31 1-12 0-6(0 = sunday) username command

下面举例：

比如我想要在每天0：00以root用户执行一个名为test.sh的脚本：

    0 0 * * * root ./root/test.sh #假设先前已经给了执行权限

再比如每周六和周日以root用户执行一个名为img\_crawl.py的爬虫：

    * * * * 0,6 root python /root/img_crawl.py

或者你想要每天10：50开始 每十分钟以root用户执行clear\_ram.sh脚本：

    50,0 10 * * * root ./root/clear_ram.sh
    0-59/10 * * * * root  ./root/clear_ram.sh

以上就是玩了三天crontab的总结啦\~
