# 项目二：数据可视化

# 1 生成数据

## 1.1 安装matplotlib

```
python -m pip install matplotlib
```

```
Microsoft Windows [版本 10.0.19042.1110]
(c) Microsoft Corporation。保留所有权利。

C:\Users\Alan>pip --version
pip 21.1.3 from d:\dev\python\python3.9\lib\site-packages\pip (python 3.9)

C:\Users\Alan>python -m pip install matplotlib
WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ProtocolError('Connection aborted.', ConnectionResetError(10054, '远程主机强迫关闭了一个现有的连接。', None, 10054, None))': /simple/matplotlib/
Collecting matplotlib
  Downloading matplotlib-3.4.2-cp39-cp39-win_amd64.whl (7.1 MB)
     |████████████████████████████████| 7.1 MB 23 kB/s
Collecting pyparsing>=2.2.1
  Downloading pyparsing-2.4.7-py2.py3-none-any.whl (67 kB)
     |████████████████████████████████| 67 kB 12 kB/s
Collecting kiwisolver>=1.0.1
  Downloading kiwisolver-1.3.1-cp39-cp39-win_amd64.whl (51 kB)
     |████████████████████████████████| 51 kB 23 kB/s
Collecting cycler>=0.10
  Downloading cycler-0.10.0-py2.py3-none-any.whl (6.5 kB)
Collecting pillow>=6.2.0
  Downloading Pillow-8.3.1-1-cp39-cp39-win_amd64.whl (3.2 MB)
     |████████████████████████████████| 3.2 MB 17 kB/s
Collecting numpy>=1.16
  Downloading numpy-1.21.0-cp39-cp39-win_amd64.whl (14.0 MB)
     |████████████████████████████████| 14.0 MB 21 kB/s
WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ReadTimeoutError("HTTPSConnectionPool(host='pypi.org', port=443): Read timed out. (read timeout=15)")': /simple/python-dateutil/
WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ProtocolError('Connection aborted.', ConnectionResetError(10054, '远程主机强迫关闭了一个现有的连接。', None, 10054, None))': /simple/python-dateutil/
Collecting python-dateutil>=2.7
  Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
     |████████████████████████████████| 247 kB 46 kB/s
Collecting six
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six, python-dateutil, pyparsing, pillow, numpy, kiwisolver, cycler, matplotlib
Successfully installed cycler-0.10.0 kiwisolver-1.3.1 matplotlib-3.4.2 numpy-1.21.0 pillow-8.3.1 pyparsing-2.4.7 python-dateutil-2.8.2 six-1.16.0

C:\Users\Alan>
'''


```

**为了在Pycharm中正常使用matplotlib**

需要执行一下步骤：

打开Pycharm，File——Settings——Project:WorkSpace——Python Interpreter

点击右侧加号，在其中搜索matplotlib，再点击Install即可（PS：这里可能需要点时间加载，耐心等待）

## 1.2绘制简单的折线图

```python
#mpl_squares.py
import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
plt.plot(squares)
plt.show()#打开matplotlib查看器
```

Result：

![1](Matplotlib%E5%AE%9E%E6%88%98.assets/1-1640669030739.png)

### 1.2.1修改标签文字和线条粗细

```python
#mpl_squares.py
import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
plt.plot(squares,linewidth = 5)#设置线条粗细

plt.title("Square Numbers", fontsize = 24)#设置表标题
plt.xlabel("Value", fontsize = 14)#设置X轴标签
plt.ylabel("Square of Value", fontsize = 14)#设置Y轴标签
plt.tick_params(axis='both', labelsize = 14)#设置刻度标记大小

plt.show()
```

![2](Matplotlib%E5%AE%9E%E6%88%98.assets/2.png)

### 1.2.2校正图形

由图像可以看出明显错误，0的平方是1,4的平方是25，现在来进行修正

```python
#mpl_squares.py
import matplotlib.pyplot as plt

input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_value,squares,linewidth = 5)#设置线条粗细

plt.title("Square Numbers", fontsize = 24)#设置表标题
plt.xlabel("Value", fontsize = 14)#设置X轴标签
plt.ylabel("Square of Value", fontsize = 14)#设置Y轴标签
plt.tick_params(axis='both', labelsize = 14)#设置刻度标记大小

plt.show()
```

![3](Matplotlib%E5%AE%9E%E6%88%98.assets/3.png)

### 1.2.3使用scatter()绘制散点图并设置其样式

```python
import matplotlib.pyplot as plt

plt.scatter(2,4,s=200)

plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 24)
plt.ylabel('Square of Value',fontsize = 24)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize = 14)
plt.show()
```

![4](Matplotlib%E5%AE%9E%E6%88%98.assets/4.png)

### 1.2.4使用scatter()绘制一系列点

```python
import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

plt.scatter(x_values,y_values,s=100)

plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 24)
plt.ylabel('Square of Value',fontsize = 24)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize = 14)
plt.show()
```

![5](Matplotlib%E5%AE%9E%E6%88%98.assets/5.png)

### 1.2.5自动计算数据

```python
import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,s=40)

plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 24)
plt.ylabel('Square of Value',fontsize = 24)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize = 14)
#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])

plt.show()
```

![6](Matplotlib%E5%AE%9E%E6%88%98.assets/6.png)

### 1.2.6删除数据点的轮廓

```python
plt.scatter(x_values,y_values,edgecolors='none',s=40)
```

### 1.2.7自定义颜色

```python
plt.scatter(x_values,y_values,edgecolors='none',s=40,c='red')
plt.scatter(x_values,y_values,edgecolors='none',s=40,color=(0,0,0))
```

### 1.2.8使用颜色映射

```python
plt.scatter(x_values,y_values,edgecolors='none',s=40,c=y_values,cmap=plt.cm.Blues)
```

![7](Matplotlib%E5%AE%9E%E6%88%98.assets/7.png)

### 1.2.9自动保存图表

```python
#自动保存图标至文件
plt.savefig('squares_plot.png',bbox_inches = 'tight')
#第一个实参指定保存的文件名，第二个实参指定将图标多余的空白区域裁剪掉。
```

### 1.2.10练习

#### 练习一：

数字的三次方被称为其立方。请绘制一个图形，显示前5个整数的立方值，再绘制一个图形，显示前5000个整数的立方值。

```python
import matplotlib.pyplot as plt

x_value = list(range(1,6))
y_value = [x**3 for x in x_value]

plt.scatter(x_value,y_value)

plt.title('Cubic Number',fontsize = 24)
plt.xlabel('Value',fontsize = 14)
plt.ylabel('Cubic of Value',fontsize = 14)

plt.axis([0,6,0,150])

plt.show()
```

```python
import matplotlib.pyplot as plt

x_value = list(range(1,5001))
y_value = [x**3 for x in x_value]

plt.scatter(x_value,y_value)

plt.title('Cubic Number',fontsize = 24)
plt.xlabel('Value',fontsize = 14)
plt.ylabel('Cubic of Value',fontsize = 14)

plt.axis([0,5300,0,130000000000])

plt.show()
```

#### 练习二：

给前面绘制的立方图指定颜色映射

```python
import matplotlib.pyplot as plt

x_value = list(range(1,5001))
y_value = [x**3 for x in x_value]

plt.scatter(x_value,y_value,edgecolors='none',s=40,c=y_value,cmap=plt.cm.Blues)

plt.title('Cubic Number',fontsize = 24)
plt.xlabel('Value',fontsize = 14)
plt.ylabel('Cubic of Value',fontsize = 14)

plt.axis([0,5300,0,130000000000])

plt.show()
```



## 1.3随机漫步

### 1.3.1创建RandomWalk()类

```python
#random_walk.py
from random import choice
class RandomWalk():
    def __init__(self,num_points=5000):#设置总点数为5000
        self.num_points = num_points

        #创建两个用于存储x与y值的列表，并让每次的漫步都从（0,0）开始
        self.x_values = [0]
        self.y_values = [0]
```

### 1.3.2选择方向

```python
#randomwalk.py
def fill_walk(self):
        # 通过while循环来控制随机漫步的执行，直到达到指定长度
        while len(self.x_values)<self.num_points:

            #决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            #计算下一个点的X与Y值
            #令x_values和y_values两个列表的最后一个值分别于x_step与y_step相加
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            #将最新的值放入列表
            self.x_values.append(next_x)
            self.y_values.append(next_y)
```

### 1.3.3绘制随机漫步图

```python
#rw_visual.py
import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,s=15)
plt.show()
```

### 1.3.4模拟多次随机漫步

```python
import matplotlib.pyplot as plt
from random_walk import RandomWalk
x = 1
#while True:
for x in range(10):
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values,rw.y_values,s=15)
    plt.show()

    plt.savefig('RandomWalk{:.0f}.png'.format(x))
    # keep_running = input("Make another walk?(y/n):")
    # if keep_running == 'n':
    #     break
```

### 1.3.5设置随机漫步图的样式

```python
import matplotlib.pyplot as plt
from random_walk import RandomWalk
# x = 1
# for x in range(10):
while True:
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)
    plt.show()

    # plt.savefig('RandomWalk{:.0f}.png'.format(x))
    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
```

### 1.3.6重新绘制起点和终点

```python
import matplotlib.pyplot as plt
from random_walk import RandomWalk
# x = 1
# for x in range(10):
while True:
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)

    #突出起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    plt.show()
    # plt.savefig('RandomWalk{:.0f}.png'.format(x))
    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
```

![8](Matplotlib%E5%AE%9E%E6%88%98.assets/8.png)

### 1.3.7隐藏坐标轴

```python
#rw_visual.py
#隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
```



```python
	current_axes = plt.axes()
	current_axes.xaxis.set_visible(False)
	current_axes.yaxis.set_visible(False)
```



### 1.3.8增加点数

```python
import matplotlib.pyplot as plt
from random_walk import RandomWalk
# x = 1
# for x in range(10):
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)

    #突出起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    #隐藏坐标轴
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    # current_axes = plt.axes()
    # current_axes.xaxis.set_visible(False)
    # current_axes.yaxis.set_visible(False)

    plt.show()
    # plt.savefig('RandomWalk{:.0f}.png'.format(x))
    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
```

### 1.3.9调整尺寸以适合屏幕

```python
 plt.figure(dii = 128,figsize = (10,6))
```



### 1.3.10小结

```python
#random_walk.py
from random import choice
class RandomWalk():
    def __init__(self,num_points=5000):#设置总点数为5000
        self.num_points = num_points

        #创建两个用于存储x与y值的列表，并让每次的漫步都从（0,0）开始
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):
        # 通过while循环来控制随机漫步的执行，直到达到指定长度
        while len(self.x_values)<self.num_points:

            #决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            #计算下一个点的X与Y值
            #令x_values和y_values两个列表的最后一个值分别于x_step与y_step相加
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            #将最新的值放入列表
            self.x_values.append(next_x)
            self.y_values.append(next_y)
```

```python
#rw_visual.py
import matplotlib.pyplot as plt
from random_walk import RandomWalk
# x = 1
# for x in range(10):
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.figure(dii = 128,figsize = (10,6))

    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)

    #突出起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    #隐藏坐标轴
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    # current_axes = plt.axes()
    # current_axes.xaxis.set_visible(False)
    # current_axes.yaxis.set_visible(False)

    plt.show()
    # plt.savefig('RandomWalk{:.0f}.png'.format(x))
    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
```



### 1.3.11练习

#### 练习一：

修改rw_visual.py, 将其中的plt.scatter()替换为plt.plot()。为模拟花粉在水滴表面的运动路径，向plt.plot()传递rw.x_values和rw.y_values，并指定实参值linewidth。使用5000个点而不是50000个点。

```python
plt.plot(rw.x_values,rw.y_values,linewidth = 5)
```



#### 练习二：

在类RandomWalk中，x_step和y_step是根据相同的条件生成的：从列表[1,-1]中随机地选择方向，并从列表[0,1,2,3,4]中随机地选择距离。请修改这些列表中的值，看看对随机漫步路径有何影响。尝试使用更长的距离选择列表，如0~8；或者将-1从x或y方向列表中删除。



#### 练习三：



## 1.4使用Pygal模拟掷骰子

### 1.4.1安装Pygal

```
python -m install --user pygal==1.7
```

### 1.4.2创建Die类

```python
from random import randint
class Die():
    def __init__(self,num_sides = 6):
        self.num_sides = num_sides
    def roll(self):
        #randint()返回一个1和面数之间的随机数。包括1和面数。
        return randint(1,self.num_sides)
```

### 1.4.3掷骰子

```python
from die import Die
die = Die()
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)
print(results)
```

Result：

```python
[2, 5, 2, 4, 4, 4, 6, 5, 3, 5, 1, 6, 6, 4, 4, 4, 2, 4, 2, 5, 3, 2, 3, 1, 5, 1, 1, 6, 6, 5, 2, 5, 5, 1, 6, 2, 2, 6, 5, 5, 5, 6, 2, 2, 3, 6, 5, 3, 1, 3, 3, 6, 1, 1, 1, 5, 1, 1, 3, 1, 2, 2, 5, 4, 4, 3, 3, 1, 6, 2, 6, 6, 1, 1, 2, 3, 1, 2, 1, 2, 2, 5, 4, 1, 6, 2, 5, 6, 2, 2, 6, 1, 1, 5, 2, 6, 3, 3, 3, 4]
```

### 1.4.4分析结果

```python
from die import Die
die = Die()
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(results)
print(frequencies)
```

Result：

```python
[4, 5, 3, 5, 4, 4, 3, 6, 4, 1, 3, 3, 5, 1, 3, 2, 1, 6, 6, 6, 2, 2, 1, 6, 2, 1, 6, 4, 5, 3, 2, 1, 1, 2, 3, 5, 3, 2, 2, 6, 2, 5, 4, 4, 1, 1, 1, 5, 6, 2, 6, 4, 2, 3, 6, 5, 5, 2, 3, 6, 1, 1, 4, 5, 3, 6, 6, 3, 5, 5, 4, 5, 2, 3, 5, 3, 6, 3, 6, 4, 2, 5, 3, 4, 6, 3, 6, 5, 4, 3, 4, 1, 2, 5, 5, 2, 3, 1, 3, 4, 3, 1, 6, 4, 4, 1, 1, 5, 1, 1, 1, 3, 4, 3, 6, 3, 1, 2, 5, 5, 1, 3, 5, 4, 5, 5, 3, 3, 2, 2, 1, 3, 3, 1, 6, 4, 4, 2, 3, 4, 6, 1, 4, 4, 1, 2, 3, 5, 4, 3, 1, 6, 6, 1, 4, 4, 6, 6, 3, 1, 4, 3, 4, 2, 2, 4, 1, 4, 1, 4, 6, 1, 4, 1, 2, 5, 5, 6, 3, 3, 5, 4, 3, 4, 6, 2, 3, 5, 3, 5, 3, 4, 1, 2, 2, 3, 1, 4, 6, 4, 2, 5, 1, 3, 5, 5, 4, 6, 1, 5, 5, 4, 3, 2, 5, 6, 6, 5, 3, 2, 5, 5, 1, 5, 6, 4, 2, 1, 3, 2, 4, 5, 5, 4, 6, 2, 3, 2, 5, 5, 2, 2, 2, 1, 5, 2, 5, 2, 1, 5, 4, 4, 3, 2, 4, 1, 5, 3, 6, 3, 4, 3, 6, 4, 6, 3, 1, 5, 6, 2, 3, 3, 4, 3, 4, 2, 2, 4, 5, 1, 6, 5, 3, 1, 1, 5, 6, 1, 1, 1, 4, 3, 5, 1, 1, 2, 1, 6, 2, 3, 1, 3, 1, 3, 1, 2, 5, 3, 6, 5, 4, 6, 3, 3, 6, 4, 5, 5, 5, 1, 5, 2, 1, 5, 2, 5, 4, 1, 2, 2, 5, 2, 4, 3, 3, 1, 6, 1, 3, 4, 1, 6, 6, 2, 4, 4, 6, 5, 1, 6, 2, 3, 6, 3, 1, 4, 4, 4, 4, 2, 3, 3, 2, 4, 2, 4, 5, 4, 2, 6, 5, 2, 2, 2, 1, 2, 1, 3, 1, 2, 1, 3, 5, 6, 4, 3, 1, 3, 2, 6, 5, 1, 3, 4, 4, 2, 1, 4, 2, 6, 3, 1, 4, 1, 4, 3, 1, 2, 6, 6, 5, 3, 3, 4, 5, 4, 1, 4, 2, 3, 3, 6, 3, 6, 3, 6, 1, 4, 3, 3, 6, 4, 4, 2, 5, 1, 3, 3, 5, 5, 3, 3, 6, 3, 5, 5, 6, 5, 2, 2, 2, 5, 3, 4, 1, 3, 2, 6, 6, 6, 3, 2, 3, 5, 1, 2, 2, 6, 1, 4, 4, 4, 6, 5, 4, 5, 3, 1, 4, 2, 5, 1, 3, 5, 5, 1, 1, 3, 5, 3, 6, 6, 4, 1, 3, 5, 3, 5, 2, 5, 6, 4, 2, 2, 5, 4, 5, 6, 5, 6, 6, 2, 6, 4, 5, 2, 1, 1, 3, 5, 3, 5, 2, 1, 6, 6, 1, 1, 4, 2, 6, 2, 3, 6, 2, 1, 4, 5, 3, 2, 5, 1, 5, 2, 3, 1, 3, 3, 5, 2, 6, 6, 1, 4, 3, 6, 2, 3, 1, 1, 4, 6, 5, 3, 4, 1, 1, 6, 2, 4, 1, 6, 2, 4, 1, 2, 3, 4, 1, 4, 1, 6, 1, 3, 3, 3, 2, 4, 3, 2, 6, 6, 3, 2, 4, 5, 6, 3, 3, 1, 2, 3, 6, 4, 5, 6, 5, 1, 3, 6, 2, 4, 1, 5, 3, 5, 2, 5, 3, 1, 3, 2, 6, 3, 3, 4, 1, 6, 6, 1, 5, 4, 2, 4, 1, 5, 2, 3, 1, 1, 1, 4, 4, 2, 2, 1, 4, 5, 1, 1, 3, 1, 4, 5, 3, 5, 2, 2, 5, 3, 4, 4, 2, 3, 4, 5, 1, 1, 3, 6, 3, 1, 6, 1, 6, 1, 5, 5, 3, 4, 6, 6, 1, 6, 6, 1, 6, 3, 3, 2, 5, 3, 2, 4, 2, 2, 1, 4, 1, 5, 6, 6, 4, 2, 3, 1, 2, 2, 4, 3, 6, 3, 3, 3, 2, 2, 4, 3, 3, 5, 3, 5, 2, 5, 3, 4, 4, 2, 1, 2, 3, 5, 2, 4, 2, 2, 3, 1, 6, 5, 1, 6, 2, 4, 2, 5, 3, 2, 4, 6, 5, 1, 6, 3, 1, 2, 2, 4, 1, 5, 1, 6, 4, 3, 5, 4, 2, 5, 1, 1, 6, 2, 5, 5, 4, 5, 3, 1, 6, 6, 1, 2, 5, 6, 6, 3, 4, 5, 1, 3, 2, 6, 3, 6, 3, 2, 2, 4, 1, 1, 2, 6, 2, 3, 2, 6, 2, 2, 2, 2, 6, 3, 5, 5, 6, 4, 2, 5, 2, 4, 1, 2, 3, 2, 6, 1, 3, 2, 4, 1, 2, 1, 2, 4, 1, 6, 5, 6, 1, 6, 4, 6, 4, 3, 6, 4, 5, 3, 4, 4, 3, 5, 6, 2, 2, 6, 3, 4, 4, 6, 2, 6, 3, 4, 2, 3, 6, 4, 4, 4, 2, 2, 2, 4, 2, 3, 2, 6, 2, 2, 6, 1, 3, 6, 4, 2, 1, 1, 2, 2, 2, 5, 3, 4, 5, 4, 2, 2, 1, 4, 1, 1, 3, 4, 2, 4, 1, 6, 4, 2, 1, 2, 1, 2, 1, 1, 4, 5, 6, 3, 4, 5, 4, 2, 5, 6, 2, 6, 5, 4, 3, 3, 2, 3, 5, 3, 6, 6, 2, 3, 6, 5, 1, 5, 4, 1, 3, 3, 4, 5, 4, 3, 3, 3, 6, 6, 6, 5, 4, 5, 1, 1, 5, 4, 6, 3, 1, 4, 2, 5, 6, 5, 2, 1, 6, 6, 3, 5, 5, 4, 1, 2, 5, 2, 1, 4, 2, 3, 1, 3, 2, 4, 3, 3, 3, 5, 1, 6, 1, 2]
[168, 178, 186, 164, 154, 150]
```

### 1.4.5绘制直方图

```python
import pygal
from die import Die
die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')

print(results)
print(frequencies)
```

![9](Matplotlib%E5%AE%9E%E6%88%98.assets/9.png)

### 1.4.6同时掷两个D6骰子

```python
import pygal
from die import Die
die_1 = Die()
die_2 = Die()
results = []
for roll_num in range(1000):
    result = die_1.roll()+die_2.roll()
    results.append(result)
frequencies = []
max_result = die_1.num_sides+die_2.num_sides
for value in range(2,max_result):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6',frequencies)
hist.render_to_file('die_visual.svg')

print(results)
print(frequencies)
```

### 1.4.7同时掷两个面数不同的骰子

```python
import pygal
from die import Die
die_1 = Die()
die_2 = Die(10)
results = []
for roll_num in range(50000):
    result = die_1.roll()+die_2.roll()
    results.append(result)
frequencies = []
max_result = die_1.num_sides+die_2.num_sides
for value in range(2,max_result):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "Results of rolling D6 and D10 50,000 times."
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10',frequencies)
hist.render_to_file('die_visual.svg')

print(results)
print(frequencies)
```



# 2下载数据

## 2.1CSV文件

### 2.1.1分析CSV文件头

```python
import csv
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
```



### 2.1.2打印文件头及其位置

```python
import csv
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index,column_header in enumerate(header_row):
        print(index,column_header)
```



### 2.1.3提取并读取数据

```python
import csv
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = []
    for row in reader:
        highs.append(row[1])
    print(highs)
```

```python
import csv
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
    print(highs)
```

### 2.1.4绘制气温图表

```python
import csv
from matplotlib import pyplot as plt
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
    print(highs)

    fig = plt.figure(dpi = 128,figsize=(10,6))
    plt.plot(highs,c='red')
    plt.title("Daily high temperatures,July 2014",fontsize = 24)
    plt.xlabel('',fontsize = 16)
    plt.ylabel("Temperature(F)",fontsize = 16)
    plt.tick_params(axis='both',which='major',labelsize = 16)
    plt.show()
```

### 2.1.5在图表中添加日期

```python
import csv
import matplotlib.pyplot as plt
from datetime import datetime
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = []
    dates = []
    for row in reader:
        dates.append(datetime.strptime(row[0],'%Y-%m-%d'))
        highs.append(int(row[1]))

    print(highs)

    fig = plt.figure(dpi = 128,figsize = (10,6))
    plt.plot(dates,highs,c = 'red')
    plt.title("Daily high temperatures, July 2014",fontsize = 20)
    plt.xlabel("",fontsize = 16)
    fig.autofmt_xdate()
    plt.ylabel("Temperatures(F)",fontsize = 16)
    plt.tick_params(axis = 'both',which='major',labelsize = 16)

    plt.show()
```

### 2.1.6使用更多的数据，并再绘制个数据系列

```python
import csv
import matplotlib.pyplot as plt
from datetime import datetime
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = []
    dates = []
    lows = []
    for row in reader:
        dates.append(datetime.strptime(row[0],'%Y-%m-%d'))
        highs.append(int(row[1]))
        lows.append(int(row[3]))

    print(highs)

    fig = plt.figure(dpi = 128,figsize = (10,6))
    plt.plot(dates,highs,c = 'red')
    plt.plot(dates,lows,c = 'b')
    plt.title("Daily high and low temperatures, 2014",fontsize = 20)
    plt.xlabel("",fontsize = 16)
    fig.autofmt_xdate()
    plt.ylabel("Temperatures(F)",fontsize = 16)
    plt.tick_params(axis = 'both',which='major',labelsize = 16)

    plt.show()
```

![10](Matplotlib%E5%AE%9E%E6%88%98.assets/10.png)

### 2.1.7处理错误数据

```python
import matplotlib.pyplot as plt
from datetime import datetime
import csv

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates,highs,lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    fig = plt.figure(dpi = 128,figsize = (10,6))
    plt.plot(dates,highs,c='r',alpha = 0.5)
    plt.plot(dates,lows,c='b',alpha = 0.5)
    plt.fill_between(dates,highs,lows,fc = 'g',alpha = 0.1)

    plt.title('No fault result',fontsize = 24)
    plt.ylabel('Temperatures[F]',fontsize = 16)
    plt.xlabel('date',loc = 'left',fontsize = 16)
    plt.tick_params(axis = 'both',which = 'major',labelsize = 16 )
    fig.autofmt_xdate()

    plt.show()
```

![11](Matplotlib%E5%AE%9E%E6%88%98.assets/11.png)

### 2.1.8练习

#### 练习一：

#### 练习二：

#### 练习三：

#### 练习四：

## 2.2JSON格式

### 2.2.1request下载

略，后期再补

### 2.2.2提取相关数据

```python
import json as j

filename = 'btc_close_2017.json'
with open(filename) as f:
    bct_data = j.load(f)
for bct_dict in bct_data:
    date = bct_dict['date']
    month = bct_dict['month']
    week = bct_dict['week']
    weekday = bct_dict['weekday']
    close = bct_dict['close']
    print('date:{},month:{},week:{},weekday:{},close:{}'.format(date,month,week,weekday,close))
```

### 2.2.3将字符串转换为数字值

```python
import json as j
import matplotlib.pyplot as plt

filename = 'btc_close_2017.json'
with open(filename) as f:
    bct_data = j.load(f)
    dates,months,weeks,weekdays,closes = [],[],[],[],[]
for bct_dict in bct_data:
    dates.append(bct_dict['date'])
    months.append(int(bct_dict['month']))
    weeks.append(int(bct_dict['week']))
    weekdays.append(bct_dict['weekday'])
    closes.append(int(float(bct_dict['close'])))
```

### 2.2.4绘制收盘价折线图

```python
import json as j
import pygal as pg
import matplotlib.pyplot as plt

filename = 'btc_close_2017.json'
with open(filename) as f:
    bct_data = j.load(f)
    dates,months,weeks,weekdays,closes = [],[],[],[],[]
for bct_dict in bct_data:
    dates.append(bct_dict['date'])
    months.append(int(bct_dict['month']))
    weeks.append(int(bct_dict['week']))
    weekdays.append(bct_dict['weekday'])
    closes.append(int(float(bct_dict['close'])))
    # print('date:{},month:{},week:{},weekday:{},close:{}'.format(date,month,week,weekday,close))
line_chart = pg.Line(x_label_rotation = 20,show_minor_x_labels = False)
line_chart.title = '收盘价（￥）'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major =dates[::N]
line_chart.add('收盘价',closes)
line_chart.render_to_file('收盘价折线图（￥）.svg')
```

### 2.2.5时间序列特征初探

```python
import json as j
import pygal as pg
import math

filename = 'btc_close_2017.json'
with open(filename) as f:
    bct_data = j.load(f)
    dates,months,weeks,weekdays,closes = [],[],[],[],[]
for bct_dict in bct_data:
    dates.append(bct_dict['date'])
    months.append(int(bct_dict['month']))
    weeks.append(int(bct_dict['week']))
    weekdays.append(bct_dict['weekday'])
    closes.append(int(float(bct_dict['close'])))
    # print('date:{},month:{},week:{},weekday:{},close:{}'.format(date,month,week,weekday,close))
line_chart = pg.Line(x_label_rotation = 20,show_minor_x_labels = False)
line_chart.title = '收盘价对数变换（￥）'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major =dates[::N]
close_log = [math.log10(_) for _ in closes]

line_chart.add('log收盘价',close_log)
line_chart.render_to_file('收盘价对数变换折线图（￥）.svg')
```

### 2.2.6收盘价均值

```python
import json as j
import pygal as pg
import matplotlib.pyplot as plt
import math
from itertools import groupby

def draw_line(x_data,y_data,title,y_legend):
    xy_map = []
    for x,y in groupby(sorted(zip(x_data,y_data)),key = lambda _:_[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list)/len(y_list)])
    x_unique,y_mean = [*zip(*xy_map)]
    line_chart = pg.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend,y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart

filename = 'btc_close_2017.json'
with open(filename) as f:
    bct_data = j.load(f)
    dates,months,weeks,weekdays,closes = [],[],[],[],[]
for bct_dict in bct_data:
    dates.append(bct_dict['date'])
    months.append(int(bct_dict['month']))
    weeks.append(int(bct_dict['week']))
    weekdays.append(bct_dict['weekday'])
    closes.append(int(float(bct_dict['close'])))

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month],closes[:idx_month],'收盘价月日均值（￥）','月日均值')

idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week],closes[1:idx_week],'收盘价周日均值（￥）','周日均值')

idx_week = dates.index('2017-12-11')
wd = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekdays_int = [wd.index(w)+1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int,closes[1:idx_week],'收盘价星期均值（￥）','星期均值')
```

### 2.2.7收盘价数据仪表盘

```python
import json as j
import pygal as pg
import matplotlib.pyplot as plt
import math
from itertools import groupby

def draw_line(x_data,y_data,title,y_legend):
    xy_map = []
    for x,y in groupby(sorted(zip(x_data,y_data)),key = lambda _:_[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list)/len(y_list)])
    x_unique,y_mean = [*zip(*xy_map)]
    line_chart = pg.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend,y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart

filename = 'btc_close_2017.json'
with open(filename) as f:
    bct_data = j.load(f)
    dates,months,weeks,weekdays,closes = [],[],[],[],[]
for bct_dict in bct_data:
    dates.append(bct_dict['date'])
    months.append(int(bct_dict['month']))
    weeks.append(int(bct_dict['week']))
    weekdays.append(bct_dict['weekday'])
    closes.append(int(float(bct_dict['close'])))

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month],closes[:idx_month],'收盘价月日均值（￥）','月日均值')

idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week],closes[1:idx_week],'收盘价周日均值（￥）','周日均值')

idx_week = dates.index('2017-12-11')
wd = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekdays_int = [wd.index(w)+1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int,closes[1:idx_week],'收盘价星期均值（￥）','星期均值')

with open('收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write(
        '<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in [
            '收盘价折线图（￥）.svg', '收盘价对数变换折线图（￥）.svg', '收盘价月日均值（￥）.svg',
            '收盘价周日均值（￥）.svg', '收盘价星期均值（￥）.svg'
    ]:
        html_file.write(
            '    <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))  # 1
    html_file.write('</body></html>')
```

### 2.2.8练习

#### 练习一：

#### 练习二：

#### 练习三：

#### 练习四：















# 3 使用API

这一节主要基于GitHub中的python项目相关数据进行分析，将其数据下载，提取，最后可视化。

依赖网址：https://api.github.com/search/repositories?q=language:python&sort=stars

## 3.1使用web API

### 3.1.1安装requests

```
pip install --user requests
```

> ```
> Microsoft Windows [版本 10.0.19042.1110]
> (c) Microsoft Corporation。保留所有权利。
> 
> C:\Users\Alan>pip install --user requests
> Collecting requests
>   Downloading requests-2.26.0-py2.py3-none-any.whl (62 kB)
>      |████████████████████████████████| 62 kB 99 kB/s
> Collecting idna<4,>=2.5
>   Downloading idna-3.2-py3-none-any.whl (59 kB)
>      |████████████████████████████████| 59 kB 357 kB/s
> Collecting urllib3<1.27,>=1.21.1
>   Downloading urllib3-1.26.6-py2.py3-none-any.whl (138 kB)
>      |████████████████████████████████| 138 kB 233 kB/s
> Collecting certifi>=2017.4.17
>   Downloading certifi-2021.5.30-py2.py3-none-any.whl (145 kB)
>      |████████████████████████████████| 145 kB 234 kB/s
> Collecting charset-normalizer~=2.0.0
>   Downloading charset_normalizer-2.0.3-py3-none-any.whl (35 kB)
> Installing collected packages: urllib3, idna, charset-normalizer, certifi, requests
>   WARNING: The script normalizer.exe is installed in 'C:\Users\Alan\AppData\Roaming\Python\Python39\Scripts' which is not on PATH.
>   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
> Successfully installed certifi-2021.5.30 charset-normalizer-2.0.3 idna-3.2 requests-2.26.0 urllib3-1.26.6
> WARNING: You are using pip version 21.1.3; however, version 21.2.1 is available.
> You should consider upgrading via the 'd:\dev\python\python3.9\python.exe -m pip install --upgrade pip' command.
> 
> C:\Users\Alan>python -m pip list
> Package            Version
> ------------------ ---------
> certifi            2021.5.30
> charset-normalizer 2.0.3
> cycler             0.10.0
> idna               3.2
> kiwisolver         1.3.1
> matplotlib         3.4.2
> numpy              1.21.0
> Pillow             8.3.1
> pip                21.1.3
> pygal              2.4.0
> pygame             2.0.1
> pyparsing          2.4.7
> python-dateutil    2.8.2
> requests           2.26.0
> setuptools         56.0.0
> six                1.16.0
> urllib3            1.26.6
> WARNING: You are using pip version 21.1.3; however, version 21.2.1 is available.
> You should consider upgrading via the 'D:\Dev\Python\Python3.9\python.exe -m pip install --upgrade pip' command.
> ```

### 3.1.2处理API响应

```python
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print('Status code:',status_code)

response_dict = r.json()

print(responsi_dict.key())
```

### 3.1.3处理响应字典

```python
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print("Status code",r.status_code)

response_dict = r.json()
print(response_dict.keys())

print('Total repositories:', response_dict['total_count'])
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

repo_dict = repo_dicts[0]
print('\nkeys:', len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

```

### 3.1.4研究第一个仓库

```python
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print("Status code",r.status_code)

response_dict = r.json()
print(response_dict.keys())

print('Total repositories:', response_dict['total_count'])
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

repo_dict = repo_dicts[0]
print('\nSelected information about first repository:')
print('Name:',repo_dict['name'])
print('Owner:',repo_dict['owner']['login'])
print('Stars:',repo_dict['stargazers_count'])
print('Repository:',repo_dict['html_url'])
print('Created:',repo_dict['created_at'])
print('Updated:',repo_dict['updated_at'])
print('Description:',repo_dict['description'])

```



### 3.1.5打印所有仓库的主要信息

只需要加个for循环

```python
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print("Status code",r.status_code)

response_dict = r.json()
print(response_dict.keys())

print('Total repositories:', response_dict['total_count'])
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

for i in range(30):
    repo_dict = repo_dicts[i]
    if i+1 == 1:
        print('\nSelected information about 1st repository:')
    elif i+1 == 2:
        print('\nSelected information about 2nd repository:')
    elif i+1 == 3:
        print('\nSelected information about 3rd repository:')
    else:
        print('\nSelected information about {}th repository:'.format(i+1))
    print('Name:',repo_dict['name'])
    print('Owner:',repo_dict['owner']['login'])
    print('Stars:',repo_dict['stargazers_count'])
    print('Repository:',repo_dict['html_url'])
    print('Created:',repo_dict['created_at'])
    print('Updated:',repo_dict['updated_at'])
    print('Description:',repo_dict['description'])
```

### 3.1.6监视API的速率限制

https://api.github.com/rate_limit

## 3.2使用Pygal可视化仓库

```python
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print("Status code",r.status_code)

response_dict = r.json()
print(response_dict.keys())

print('Total repositories:', response_dict['total_count'])
repo_dicts = response_dict['items']

names,stars = [],[]

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(style = my_style,x_label_rotation = 45,show_legend = False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('',stars)
chart.render_to_file('python_repos.svg')
```

### 3.2.1改进Pygal图表，并添加自定义工具提示

```python
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print("Status code",r.status_code)

response_dict = r.json()
print(response_dict.keys())

print('Total repositories:', response_dict['total_count'])
repo_dicts = response_dict['items']

names,plot_dicts = [],[]

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':repo_dict['description'],
    }
    plot_dicts.append(plot_dict)

my_style = LS('#333366',base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style = my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')
```

### 3.2.2在图表中添加可单击的链接

```python
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print("Status code:",r.status_code)

response_dict = r.json()
print(response_dict.keys())

print('Total repositories:', response_dict['total_count'])
repo_dicts = response_dict['items']

names,plot_dicts = [],[]

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # if repo_dict['description'] == None:
    #     repo_dict['description'] = 'There is no description'
    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':repo_dict['description'],
        'xlink':repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

my_style = LS('#333366',base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style = my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')
```

出现了报错：

```python
D:\Dev\Python\WorkSpace\venv\Scripts\python.exe D:/Dev/Python/WorkSpace/data_visualization/python_repos.py
Status code: 200
dict_keys(['total_count', 'incomplete_results', 'items'])
Total repositories: 7667198
Traceback (most recent call last):
  File "D:\Dev\Python\WorkSpace\data_visualization\python_repos.py", line 44, in <module>
    chart.render_to_file('python_repos.svg')
  File "D:\Dev\Python\WorkSpace\venv\lib\site-packages\pygal\graph\public.py", line 114, in render_to_file
    f.write(self.render(is_unicode=True, **kwargs))
  File "D:\Dev\Python\WorkSpace\venv\lib\site-packages\pygal\graph\public.py", line 52, in render
    self.setup(**kwargs)
  File "D:\Dev\Python\WorkSpace\venv\lib\site-packages\pygal\graph\base.py", line 217, in setup
    self._draw()
  File "D:\Dev\Python\WorkSpace\venv\lib\site-packages\pygal\graph\graph.py", line 933, in _draw
    self._plot()
  File "D:\Dev\Python\WorkSpace\venv\lib\site-packages\pygal\graph\bar.py", line 146, in _plot
    self.bar(serie)
  File "D:\Dev\Python\WorkSpace\venv\lib\site-packages\pygal\graph\bar.py", line 113, in bar
    bar = decorate(
  File "D:\Dev\Python\WorkSpace\venv\lib\site-packages\pygal\util.py", line 232, in decorate
    svg.node(node, 'desc', class_='label').text = to_unicode(
  File "D:\Dev\Python\WorkSpace\venv\lib\site-packages\pygal\_compat.py", line 61, in to_unicode
    return string.decode('utf-8')
AttributeError: 'NoneType' object has no attribute 'decode'

Process finished with exit code 1
```

检查后发现，源文件中的description存在Null，所以加入判空条件

```python
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print("Status code:",r.status_code)

response_dict = r.json()
print(response_dict.keys())

print('Total repositories:', response_dict['total_count'])
repo_dicts = response_dict['items']

names,plot_dicts = [],[]

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    if repo_dict['description'] == None:
        repo_dict['description'] = 'There is no description'
    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':repo_dict['description'],
        'xlink':repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

my_style = LS('#333366',base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style = my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')
```

