# 安装Pyganme时出现的问题

**前提：**

我的python版本是3.9.6

在CMD中直接用命令

```
pip install pygame
```

安装pygame

安装后在Pycharm中开始写代码，直接报错ModuleNotFoundError: No module named 'pygame' 

解决办法：

打开Pycharm，File——Settings——Project:WorkSpace——Python Interpreter

点击右侧加号，在其中搜索Pygame，再点击Install即可（PS：这里可能需要点时间加载，耐心等待）

之后再运行代码就不报之前的错了。

但是出现了新的错误。

代码如下：

```python
import sys
import pygame

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.dispaly.set_caption("Alien Invasion")
	bg_color = (230,230,230)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.fill(bg_color)
		pygame.dispaly.flip()

run_game()
```

一段简单代码。

报错说pygame没有dispaly属性。

```
D:\Dev\Python\WorkSpace\venv\Scripts\python.exe D:/Dev/Python/WorkSpace/Alienandspace/alien_invasion.py
pygame 2.0.1 (SDL 2.0.14, Python 3.9.6)
Hello from the pygame community. https://www.pygame.org/contribute.html
Traceback (most recent call last):
  File "D:\Dev\Python\WorkSpace\Alienandspace\alien_invasion.py", line 16, in <module>
    run_game()
  File "D:\Dev\Python\WorkSpace\Alienandspace\alien_invasion.py", line 7, in run_game
    pygame.dispaly.set_caption("Alien Invasion")
AttributeError: module 'pygame' has no attribute 'dispaly'

Process finished with exit code 1

```

没错，粗心的我把display拼写错误了。而且最离谱的是，找了很久竟然没找出来，就在刚刚编写文档的时候才发现拼写错误。

**总结**

1、通过pip安装pygame后，如果想在pycharm中使用，则需要在pycharm中再安装一遍。

2、敲代码要仔细，尤其是某些预设函数、属性，错一点找一天。养成一个好的代码书写习惯是省时省力的第一步。

———————————————2021.7.6—————————————————————————

每天学一点，祝成功！！
