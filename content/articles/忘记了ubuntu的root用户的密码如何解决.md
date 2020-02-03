Title: 忘记root的密码如何解决
Date: 2018-08-05 22:47
Author: PwnForWhat
Category: Daily
Tags:Linux
Slug: 忘记了ubuntu的root用户的密码如何解决
Status: published

> 昨天教同学使用Ubuntu，他居然把密码给忘记了。于是便顺便了解了一下这方面的知识。

首先是在开机3秒内按下ESC键

然后就会出现一个菜单，选择进入恢复模式 （recovery mode）

进入恢复模式以后，启用root shell

将目录改为可写  
`mount -o rw,remount `

查看home下的用户  
`ls /home`

修改密码  
`passwd`

输入两次密码（一次是确认）即修改完成

重启