# Introduction

本仓库是一个学习记录，记录本人的各项学习历程。2021年12月28日建立，后期将不断更新各种学习笔记。

# 目录



## Tips

**如何将本地普通文件夹设置成Git仓库**

在文件夹中右键 Git bush here

git init (会得到一个.git文件夹)

此时仓库已经建好，添加好内容后

git add . 

git commit -m "提交说明"

git branch -M surface #新建一个分支名叫surface



**如何将本地仓库上传至GitHub**

1. 在GitHub上新建一个仓库
2. 将新建的仓库克隆到本地, 或直接打开本地已存在的仓库
3. 对仓库内容进行编辑，更新
4. 进入该仓库，右键选择git bush here（未安装git的请先安装）
5. 添加所有内容至缓存，git add .
6. 添加提交说明：git commit -m "提交说明"
7. 将本地更新推送到远程：git push origin surface   ##这里的surface是分支名
8. 完成

**遇到的问题**

error: remote origin already exists.

1、先删除远程 Git 仓库

> $ git remote rm origin

2、再添加远程 Git 仓库

> $ git remote add origin https://github.com/AlanWilliamStark/Alan_Notes.git

**常用指令**

1.cd : 切换到哪个目录下， 如 cd e:\fff 切换 E 盘下面的fff 目录。
　　当我们用cd 进入文件夹时,我们可以使用 通配符*, cd f*, 如果E盘下只有一个f开头的文件夹,它就会进入到这个文件夹.
2.cd … 回退到上一个目录， 注意，cd 和两个点点…之间有一个空格。
3.pwd : 显示当前目录路径。
4.ls(ll): 都是列出当前目录中的所有文件，只不过ll(两个ll)列出的内容更为详细。
5.touch : 新建一个文件 如 touch index.js 就会在当前目录下新建一个index.js文件。
6.rm: 删除一个文件, rm index.js 就会把index.js文件删除.
7.mkdir: 新建一个目录,就是新建一个文件夹. 如mkdir src 新建src 文件夹.
8.rm -r : 删除一个文件夹, rm -r src 删除src目录， 好像不能用通配符。
9.mv 移动文件, mv index.html src index.html 是我们要移动的文件, src 是目标文件夹,当然, 这样写,必须保证文件和目标文件夹在同一目录下.
10.reset 清屏，把git bash命令窗口中的所有内容清空。