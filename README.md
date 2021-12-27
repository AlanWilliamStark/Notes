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

   