# Week2 图形绘制

主要使用turtle库

常用函数：

```python
import turtle as t
t.setup()
t.penup()#别名t.pu()，抬起画笔
t.pu()#别名t.penup()，抬起画笔
t.pendown()#别名pd()，落下画笔
t.pd()#别名pendown()，落下画笔
t.pensize()#别名width()，设置画笔粗细
t.width()#别名pensize()，设置画笔粗细
t.pencolor()#设置画笔颜色，参数可以是颜色字符串，或RGB值
 '''颜色字符串 ：turtle.pencolor("purple")
- RGB的小数值：turtle.pencolor(0.63, 0.13, 0.94)
- RGB的元组值：turtle.pencolor((0.63,0.13,0.94))'''
t.colormode(mode)#改变RGB模式，小数or整数
'''- 1.0：RGB小数值模式
- 255：RGB整数值模式'''
t.forward()#别名fd()，令画笔向前行进，参数为行进距离，可以为负
t.fd()#别名forward()，令画笔向前行进，参数为行进距离，可以为负
t.bk()#令画笔向后退
t.left()#令画笔左转，参数为旋转角度，这里的角度为相对度数
t.right()#令画笔右转，参数为旋转角度，这里的角度为相对度数
t.seth()#令画笔转向，参数为旋转角度，这里的角度为绝对度数
'''- turtle.setheading(angle) 别名 turtle.seth(angle)
改变行进方向，海龟走角度
- angle: 行进方向的绝对角度'''
t.circle()
'''- turtle.circle(r, extent=None)
根据半径r绘制extent角度的弧形
- r: 默认圆心在海龟左侧r距离的位置
- extent: 绘制角度，默认是360度整圆'''
t.goto()#画笔默认起点为(0,0)在画布的中心，该语句控制画笔走向，参数为下一点的坐标值
t.done()#该语句的作用是，在画笔完成绘制之后，停止操作，且画布不关闭
```



#### 案例1蟒蛇绘制

```python
import turtle
#turtle.setup(width.height,startx,starty)
#设置框体，四个参数分别是：宽，高，左上角在屏幕的位置的x值，左上角在屏幕位置的y值,若后面两个参数为空，则默认上居中
turtle.setup(1300,350,10,200)
#用penup()先把笔抬起来
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor('purple')
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()
```

#### 案例2正方形绘制

```python
import turtle as t
t.setup(1000,1000,0,0)
t.pensize(4)
t.goto(100,0)
t.goto(100,100)
t.goto(0,100)
t.goto(0,0)
t.done()
```

#### 案例3六边形绘制

```python
import turtle as t
t.setup(1000,1000,0,0)
t.pensize(4)
for i in range(1,7):
    t.fd(100)
    t.seth(60 * i)
t.done()
```

#### 案例4叠边形绘制

```python
import turtle as t
t.pensize(4)
for i in range(1,12):
    t.fd(100)
    t.seth(65.5*i)
t.done()
```

#### 案例5风轮

```python
import turtle as t
#circle的半径为正，圆心在左侧
for i in range(1,8,2):
    t.seth(45*i)
    t.fd(100)
    t.left(90)
    t.circle(-100,45)
    t.left(90)
    t.fd(100)
t.done()
```

```python
import turtle as t
#circle的半径为负，圆心在左侧
for i in range(1,5):
    t.seth(-90*i)
    t.fd(100)
    t.right(90)
    t.circle(-100,45)
    t.right(90)
    t.fd(100)
t.done()
```

#### 案例6八边形绘制

```python
import turtle as t
t.pensize(2)
for i in range(8):
    t.fd(100)
    t.left(45)
```

#### 案例7八角形绘制

```python
import turtle as t
t.pensize(2)
for i in range(8):
    t.fd(100)
    t.left(135)
```



以下是python123第二周的单选题，答案及官方解析



1、哪个选项不能正确引用turtle库进而使用setup()函数？‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

A import turtle as t

B from turtle import*

C import setup from turtle

D import turtle

 正确答案 C

**解析：**

import只有三种使用方法，以turtle库为例：

import turtle

from turtle import setup  或 from turtle import *

import turtle as t （其中t是别名，可以更换其他名称）



2、关于turtle库，哪个选项的描述是错误的？‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

A turtle绘图体系以水平右侧为绝对方位的0度

B turtle库是一个直观有趣的图形绘制函数库

C turtle库最早成功应用于LOGO编程语言

D turtle坐标系的原点默认在屏幕左上角

 正确答案 D

**解析：**

turtle坐标系的原点默认在窗体正中间



3、哪个选项是turtle绘图中角度坐标系的绝对0度方向？‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

A 画布正下方

B 画布正上方

C 画布正右方

D 画布正左方

 正确答案 C

**解析：**

坐标系类似这样，角度坐标系的绝对0度方向是右侧

![img](E:\Programming Language\Python\Mooc\week2\1a5c4f092fb518564b5e836535a1.png)

 



4、哪个选项是下面代码的执行结果？‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

```python
turtle.circle(-90,90)
```


‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬A 绘制一个半径为90像素的弧形，圆心在小海龟当前行进的左侧

B 绘制一个半径为90像素的弧形，圆心在小海龟当前行进的右侧

C 绘制一个半径为90像素的弧形，圆心在画布正中心

D 绘制一个半径为90像素的整圆形

 正确答案 B

**解析：**

circle(x, y) 表示 以x长度为半径，y为角度，当前方向左侧x出为圆心，画圆。其中x和y都可以是负数，相应取反。



5、关于turtle库绘图函数，哪个选项的描述是错误的？‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

A turtle.seth(to_angle)函数的作用是设置小海龟当前行进方向为to_angle，to_angle是角度是一个数值 (整型或浮点型)

B turtle.circle(radius, extent=None)函数的作用是绘制一个椭圆形，extent参数可选

C turtle.fd(distance)函数的作用是向小海龟当前行进方向前进distance距离

D turtle.pensize(size)函数的作用是改变画笔的宽度为size像素

 正确答案 B

**解析：**

circle()函数不能绘制椭圆形。



6、关于turtle库的画笔控制函数，哪个选项的描述是错误的？‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

A turtle.pendown()作用是落下画笔，并移动画笔绘制一个点

B turtle.width()和turtle.pensize()都可以用来设置画笔尺寸

C turtle.colormode()的作用是设置画笔RGB颜色的表示模式

D turtle.penup()的别名有turtle.pu(),turtle.up()

 正确答案 A

**解析：**

turtle.pendown()只是放下画笔，并不绘制任何内容。



7、哪个选项不能改变turtle画笔的运行方向？‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

A bk()

B left()

C right()

D seth()

 正确答案 A

**解析：**

bk()只能后退，但不改变方向，"后退"不是"转向"。



8、哪个选项所列保留字能够实现对一组语句的循环执行？‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

A range()

B for和in

C while和def

D if和else

 正确答案 B

**解析：**

循环相关保留字是：for..in和while，但def用于定义函数，不相关。



9、哪个选项能够使用turtle库绘制一个半圆形？‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

A turtle.circle(100)

B turtle.fd(100)

C turtle.circle(100, -180)

D turtle.circle(100, 90)

 正确答案 C

**解析：**

circle(x,y)函数的用法，绘制半圆，第二个参数y是180的奇数倍。



10、哪个选项对turtle.done()的描述是正确的？‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

A turtle.done()放在代码最后，是turtle绘图的必要要求，表示绘制完成

B turtle.done()用来停止画笔绘制，但绘图窗体不关闭

C turtle.done()用来暂停画笔绘制，用户响应后还可以继续绘制

D turtle.done()用来隐藏turtle绘制画笔，一般放在代码最后

正确答案 B

**解析：**

建议在每个turtle绘图最后增加turtle.done()。
