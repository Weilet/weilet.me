Title: Windows Terminal折腾指南
Date: 2020-02-14 22:25
Author: Weilet
Category: Tech
Tags: Windows,Terminal
Slug: Windows Terminal折腾指南
Status: published



> 终端是程序员的浪漫

俺从2017年年底开始接触终端这个概念，那时候俺对它一知半解，是个被GUI宠坏的巨婴。

直到后来，俺碰见了[Hyper](https://hyper.is/)，它的高颜值和高度定制使俺沉迷。然而渐渐地俺觉得它的速度比起原生的慢太多了。而且有些时候俺需要切换PowerShell和WSL，它并不支持。

能够打败原生的，只有原生。某天俺在Django交流群里了解到[Windows Terminal](https://github.com/microsoft/terminal)（下称Terminal），一番折腾，流畅的同时还能够多个shell切换，值得安利！

`注意：Windows Terminal需要Windows 10 1903或更高版本`

### 预备

俺假设你是使用WSL的：

首先，开启WSL功能（Cortana里搜索功能，一溜儿找下来）

然后，在Microsoft Store找到你喜欢的发行版（比如俺就喜欢Ubuntu）安装

### 安装

#### Microsoft Store

最简单的方法，目前使用下来没有任何问题。

#### 自行编译

[官方文档](https://github.com/microsoft/terminal#manually-installing-builds-from-this-repository)请。大哥都选择自行编译了，看看文档肯定会。

####  Chocolatey 

`choco install microsoft-windows-terminal`

(Chocolatey的下载速度超级慢的说)

### 配置

打开Terminal，找到setting位置。

你可以在[这里](https://github.com/microsoft/terminal/blob/master/doc/cascadia/SettingsSchema.md#globals)查看全局设置

你可以在[这里](https://github.com/microsoft/terminal/blob/master/doc/cascadia/SettingsSchema.md#profiles)查看单独设置

你可以在[这里](https://github.com/microsoft/terminal/blob/master/doc/cascadia/SettingsSchema.md#implemented-commands-and-actions)查看快捷键配置

一番配置后，你的Terminal的雏形就完成了。

### WSL优化

#### 安装zsh

`sudo apt-get install zsh`

#### 设置zsh为默认bash

`sed -i '1i bash -c zsh' ~/.bashrc` 

#### 安装oh-my-zsh

`sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`

#### 安装插件

- [zsh语法高亮](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md#oh-my-zsh) 

- [zsh历史记录](https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md#oh-my-zsh)
- ……

在zshrc中配置：

**注意☠**：插件之间是以空格分隔的

`plugins=(git sublime zsh-syntax-highlighting zsh-autosuggestions)`



### PowerShell优化

**注意☠**：以管理员身份单独运行PowerShell

#### 安装posh-git 

`Install-Module posh-git -Scope CurrentUser`

#### 安装oh-my-posh

`Install-Module oh-my-posh -Scope CurrentUser`

#### 选择主题

`notepad $profile`

在弹出的文本编辑器中输入以下内容

```powershell
Import-Module oh-my-posh
set-Theme robbyrussell
```

随后你可以在posh中输入`set-Theme lily-is-cool` 来获取所有主题的名字并以上述方法修改主题。

### 字体优化

#### 安装powerline字体

`git clone https://github.com/powerline/fonts.git`

在克隆的目录中找到`install.ps1`，双击它即可自动安装字体。

#### 配置到Terminal

找到这个字段：“fontFace”，把它们的值都改为：“Meslo LG M for powerLine”



### One More Thing

甚是怀念PowerShell的“从此打开PowerShell”的右键菜单，于是为Terminal配置之

```
Windows Registry Editor Version 5.00
 
[HKEY_CLASSES_ROOT\Directory\Background\shell\wt]
@="{右键菜单文字}"
"Icon"="{icon的绝对路径}"

 
[HKEY_CLASSES_ROOT\Directory\Background\shell\wt\command]
@="{Terminal的可执行文件的绝对路径，名称为wt.exe} -d ."
```

将上面的文本另存为注册表项(后缀为.reg)，点击添加即可

另外，在配置文件中的“startingDirectory”决定了你**新增**Tab的路径，你可以将它的值设置为“.”以保证新增的Tab的路径也是当前工作路径。