# Python基础

杨文峰的学习笔记

## CONTENTAS

[TOC]



## #1 变量与数据类型

### Hello python

```python
print("hello python")
```

输出语句

```python
massage = "Hello python world"
print(massage)
```

声名变量massage 并输出massage

```python
massage = "Hello python world"
print(massage)

massage = "Hello again!"
print(massage)
```

变量覆盖，输出结果为

```
Hello python world
Hello again!
```

### Python变量的命名规则

1、只能包含字母、数字和下划线，不能以数字开头；

2、不要将Python关键字和函数名作为变量名。

**避免使用大写字母**

### 字符串

用引号引起来的都是字符串，引号可以是双引号，也可以是单引号。

```python
vote="this is a string"
print(vote)
vote='this is a string'
print(vote)
```

输出结果：

```
this is a string
this is a string
[Finished in 159ms]
```

#### 字符串的操作

##### 字母大小写

###### .title()   首字母大写

###### .upper()  全部大写

###### .lower()全部小写

```python
name="alan william"
print(name)
print(name.title()) # Capitalize the first letter
print(name.upper())	# Capitalize the letter
print(name.lower()) # Lowercase letters
```

运行结果：

```
alan william
Alan William
ALAN WILLIAM
alan william
```



##### 合并字符串  ' +'

```python
#Merge string
first_name="alan"
last_name="william"
full_name=first_name+" "+last_name
print(full_name)
```

##### 制表符\t   和   换行符\n

```python
print("\ttpython")
print("I\nlove\npython")
```

运行结果：

```
	tpython

I
love
python
```



##### 删除空白

###### 尾空白.rstrip()

######  头空白..lstrip()

###### 两端空白..strip()

```python
disgusting_word="python  "
print(disgusting_word)
print(disgusting_word.rstrip)#临时改变#

#永久改变#
disgusting_word=disgusting_word.rstrip()
print(disgusting_word)
```

```
运行结果
python  
python
python
```

######

#### 关于print

在ptyhon2中可以按以下格式

```python
print"Hello Python world!"
```

运行结果：

```
Hello Python world!
```

### 数字

##### 整数

###### 整数的基本运算

![image-20201024162316375](C:\Users\杨文峰\AppData\Roaming\Typora\typora-user-images\image-20201024162316375.png)

常见整数运算问题

5/2=2而不是2.5

但5.0/2=2.5以及5/2.0=2.5

2/3=0

**注意：python中的整数和浮点数的区分是由数字本身决定，而不存在int或float**

##### 浮点

##### str（）

**将任何非字符串变为字符串**

**示例一**

```python
age=23
massage="Happy "+str(age)+"rd Birthday!"
print(massage)
```

运行结果：

```
Happy 23rd Birthday!
```

**示例二**

```python
num=24.0
str_num=str(num)
print(num)
print(str_num)
a=num/2
b=str_num/2  #这一步，因为str_num是一个字符串，所以它不能与2进行除法运算，故会报错
print(a+b)
```

报错结果：

```python
24.0Traceback (most recent call last):

24.0
  File "D:\Dev\Python\WorkSpace\practice1.py", line 6, in <module>
    b=str_num/2
TypeError: unsupported operand type(s) for /: 'str' and 'int'
[Finished in 175ms]
```

### Python之禅

![image-20201024164153075](C:\Users\杨文峰\AppData\Roaming\Typora\typora-user-images\image-20201024164153075.png)

------

## #2列表

由一系列按特定顺序排列的元素组成。

方括号[ ]表示列表，逗号分隔其中的元素

### 列表的创建、查、增、删、改

#### 创建列表

```python
mylist=['first','second','third','forth','fifth']
print(mylist)
```

运行结果：

```
['first', 'second', 'third', 'forth', 'fifth']
```



#### 查

```python
mylist=['first','second','third','forth','fifth']
print(mylist[0]) #List number start at 0 ,not 1
```

运行结果

```
first
```

**列表序号从0开始**

**列表最后一个元素可以用   -1   来访问**

```python
print(mylist[-1])
```

**同理，访问倒数第二个可用  -2  倒数第三个  -3  **

同样，可以利用第一张对字符串的处理来处理列表中的值

```python
massage="third element is "+mylist[2].title()+"."
print(massage)
```

运行结果：

```
third element is Third.
```

#### 增

在列表末尾添加    **.append('element')**

```python
mylist.append('sixth')
print(mylist)
```

运行结果：

```
['first', 'second', 'third', 'forth', 'fifth', 'sixth']
```

**用这种方法也可以对一个空表进行添加**



在列表中插入元素    .insert(插入位置，“插入内容”)

```python
mylist.insert(1,"half past one")
print(mylist)
```

运行结果：

```
['first', 'half past one', 'second', 'third', 'forth', 'fifth', 'sixth']
```

#### 删

**①del()**     del listname[删除位置]

```python
del mylist[1]
print(mylist)
```

运行结果：

```
['first', 'second', 'third', 'forth', 'fifth', 'sixth']
```

**②pop()**   列表类似于一个栈，pop()可以将列表末尾的元素弹出

```python
poped_mylist=mylist.pop()
print(mylist)
print(poped_mylist)
```

运行结果：

```
['first', 'second', 'third', 'forth', 'fifth']
sixth
```

由结果可见，被弹出的元素 “sixth” 是末尾元素，而且已经被存储在poped_mylist的存储空间中

**③pop(n)**   弹出指定位置

```python
mylist=['first', 'second', 'third', 'forth', 'fifth']
poped_mylist=mylist.pop(2)
```

运行结果：

```
third
```

**④remove()**   根据值删除元素

**注意remove()只能删除第一个指定的值**

```python
mylist=['first','second','third','forth','fifth']
print(mylist)
mylist.remove('second')
print(mylist)
```

运行结果：

```
['first', 'second', 'third', 'forth', 'fifth']
['first', 'third', 'forth', 'fifth']
```



#### 改

直接替换指定位置元素

```python
mylist=['first','second','third','forth','fifth']
print(mylist)
mylist[0]="one"
print(mylist)
```

运行结果：

```
['first', 'second', 'third', 'forth', 'fifth']
['one', 'second', 'third', 'forth', 'fifth']
```



### 组织列表

#### 排序

##### 临时性排序

**sorted**按字母顺序排序

```python
mylist=['first','second','third','quater','half']
print(mylist)
print(sorted(mylist))
print(mylist)
```

运行结果：

```
['first', 'second', 'third', 'quater', 'half']
['first', 'half', 'quater', 'second', 'third']
['first', 'second', 'third', 'quater', 'half']
```



**sorted(mylist,reverse=True)**按字母逆序排序

```python
print("\n\n\n")
mylist=['first','second','third','quater','half']
print(mylist)
print(sorted(mylist,reverse=True))
print(mylist)
```

运行结果：

```
['first', 'second', 'third', 'quater', 'half']
['third', 'second', 'quater', 'half', 'first']
['first', 'second', 'third', 'quater', 'half']
```



##### 永久性排序

**sort()**按字母顺序排序

```python
mylist=['first','second','third','quater','half']
print(mylist)
mylist.sort()
print(mylist)
```

运行结果：

```
['first', 'second', 'third', 'quater', 'half']
['first', 'half', 'quater', 'second', 'third']
```

**sort(reverse=True)**按字母逆序排序

```python
mylist=['first','second','third','quater','half']
print(mylist)
mylist.sort(reverse=True)
print(mylist)

```

运行结果：

```
['first', 'second', 'third', 'quater', 'half']
['third', 'second', 'quater', 'half', 'first']
```

#### 倒序打印

**reverse()**

```python
mylist=['first','second','third','quater','half']
print(mylist)
mylist.reverse()
print(mylist)
```

运行结果：

```
['first', 'second', 'third', 'quater', 'half']
['half', 'quater', 'third', 'second', 'first']
```

#### 列表长度

**len()**

```python
mylist=['first','second','third','quater','half']
print(len(mylist))
```

运行结果：

```
5
```

------

## #3操作列表

### 遍历列表   for

Python的for循环语法结构  for a in b：    #a是列表b中的一个元素。（不要忘记冒号）

for循环执行过程：先取 b中第一个值，存储与a中，然后执行for循环里的代码；由于b中还有其他值，则继续执行for，直到b中的值均遍历一遍为止。

```python
countries=['china','korean','british','american','australian']
for country in countries:
	print(country)
```

运行结果：

```
china
korean
british
american
australian
```

同样可以搭配第一章内容使用

```python
print("\n\n\n")
countries=['china','korean','british','american','australian']
for country in countries:
	print(country.title()+" is a country!")
```

运行结果：

```
China is a country!
Korean is a country!
British is a country!
American is a country!
Australian is a country!
```

**for循环中可以包含多条语句**

**Python中不用{ }来限制for循环的循环体，而是通过对齐方式的不同，来确定循环体内和外**

For instance

```python
print("\n\n\n")
countries=['china','korean','british','american','australian']
for country in countries:
	print(country.title()+" is a country!")
	print(country.upper()+" is a name of a country!")
print("That's all thank you!"+country)
```

运行结果：

```
China is a country!
CHINA is a name of a country!
Korean is a country!
KOREAN is a name of a country!
British is a country!
BRITISH is a name of a country!
American is a country!
AMERICAN is a name of a country!
Australian is a country!
AUSTRALIAN is a name of a country!
That's all thank you!australian
```

最后一句未缩进所以只执行一次，而最后的australian你知道为什么吗？

因为在for循环执行的时候，country的最后一次赋值是australian，所以在下一次输出时自然输出的时australian。

同时我们还发现，缩进在Python程序中非常重要，缩进错误或许不会导致语法错误，但将会导致程序逻辑错误。

至此，我们学习的语法规则，只有for循环的循环体语句需要缩进，之后还有哪些语句需要缩进呢，让我们拭目以待！

### 创建数字列表

#### range()

```python
for value in range(1,5):
	print(value)
```

Result：

```
1
2
3
4
```

没有出现数字 5 ，故猜测range()的工作原理是，1<=x<5



##### `list()

使用list()可以将range()的值直接转化为列表

```python
numbers=list(range(1,5))
print(numbers)
```

Result：

```
[1, 2, 3, 4]
```



range()函数还可以指定 步长

```python
print("\n\n\n")
for value in range(1,7,2):
	print(value)
```

Result：

```
1
3
5
```

扩展想象力，range可以创建任何需要的数字集

1-10的平方

```python
squares=[]
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)
```

Result：

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

以上代码还可以进行简化

```python
squares=[]
for value in range(1,11):
	squares.append(value**2)
print(squares)
```

#### 统计数字列表

```python
squares=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
min_squares=min(squares)
max_squares=max(squares)
sum_squares=sum(squares)
print(min_squares)
print(max_squares)
print(sum_squares)
```

Result：

```
1
100
385
```

#### 列表解析

化简以上代码

```python
squares=[value**2 for value in range(1,11)]
print(squares)
```

Result：

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```



### 使用列表的一部分

#### 切片

列表名[起始索引，终止索引+1]

```python
squares=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(squares[0:3])
```

Result：

```
[1, 4, 9]
```

若冒号前为指定起始索引，则默认从列表头开始；

若冒号后未指定终止索引，则默认到表尾。

```python
squares=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(squares[:4])
print(squares[2:])
```

Result：

```
[1, 4, 9, 16]
[9, 16, 25, 36, 49, 64, 81, 100]
```

-2则从倒数第二位开始

```python
print(squares[-2:])
```

Result:

```
[81, 100]
```

**每个切片就相当于一个子列表，子列表也可以通过for循环遍历**

```python
squares=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for square in squares[3:8]:
	print(square)
print("That's end of the FOR")
```

Result：

```
16
25
36
49
64
That's end of the FOR
```

#### 复制列表

将切片的起始索引和末尾索引都为空[:]

```python
squares=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
s_squares=squares[:]
print(s_squares)		
```

Result:

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### 元组（不可变的列表）

#### 元组与列表的区别是用圆括号来表示

```python
dimensions=(200,50,40,10)
print(dimensions[0])
print(dimensions[-1])
```

Result：

```
200
10
```

试图修改元组的值就会报错

![image-20201025152850994](C:\Users\杨文峰\AppData\Roaming\Typora\typora-user-images\image-20201025152850994.png)

#### 遍历元组

```python
for dimension in dimensions:
	print(dimension)
```

Result:

```
200
50
40
10
```

#### 修改元组变量

元组宗旨，要么不变，要么全变

不可修改元组的元素，但可以给存储元组的变量重新赋值。

```python
dimensions=(200,50,40,10)
for dimension in dimensions:
	print(dimension)

print("\n")
dimensions=(40,2,86,3)
for dimension in dimensions:
	print(dimension)
```

Result：

```
200
50
40
10

40
2
86
3
```

## #4if语句

### 判断语句基础知识

格式类似for   不要忘记冒号

```python
names=["alan","lily","elizabeth","william"]
for name in names:
	if name=="elizabeth":
		print("Holly God she is "+name.title())
	else:
		print("Just "+name.title())
```

Result：

```
Just Alan
Just Lily
Holly God she is Elizabeth
Just William
```

#### **常用的判断符号**

 等于： ==

不等于：！=

大于：>  小于：>

大于等于：>=  小于等于：>=

#### 与/或/是/否

与：and  可以用来连接两个判断语句，若都为true，则返回true

或：or     可以用来连接两个判断语句，若一个为true，则返回true

是：in      可以检查某元素是否在列表中，若是返回true，若否返回false

否：not  in  可以检查某元素是否不在列表中，若是则返回true，若否则返回false

### if语句的格

if

```python
age = 19
if age>=18:
	print("You are an aldut now!")
```

```
You are an aldut now!
```

if-else

if-elif-else

if-elif-elif-elif-...-else

if-elif-elif-elif

小练习

```python
for requested_topping in requested_toppings:
	bool=1
	for none_topping in none_toppings:
		if requested_topping==none_topping:
			print(none_topping+" is no more!")
			bool=0
		# else:
		# 	print("Copy that "+requested_topping)
	if bool==1:
		print("Copy that "+requested_topping)
```

```
Copy that 1
Copy that 2
3 is no more!
4 is no more!
5 is no more!
Copy that 6
```

**另外如果列表为空，在if语句中返回值为false**

```python
boxs=[]
if boxs:
	print("it's full")
else:
	print("it's empty")
```

```
it's empty
```

## #5字典

**前面介绍了方括号的列表boxs=[]；圆括号的元组boxs=()；本章将介绍的是花括号的字典boxs={}**

​		在字典中将引入键-值对（key-value）的概念，字典是一系列的键-值对的组合。每个键都与一个值相关联。通过建可以访问其值。与键相关联的可以是数字、字符串、列表甚至是字典。类似于大饼卷万物，任何python对象都能作为字典中的值。

```python
alien_0={'color':'green','point':'5'}
print(alien_0['color'])
```

```
green
```

### 添加键值对

```python
alien_0={'color':'green','point':'5'}
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
```

```
{'color': 'green', 'y_position': 25, 'x_position': 0, 'point': '5'}
```

和列表一样，有的时候，我们可以只创建一个空字典，然后再用代码添加各个键 值对。

```python
alien_0={}
alien_0['color']='green'
alien_0['points']=5
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
```

```
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
```

### 修改字典中的值

**直接对键-值对进行修改**

```python
alien_0={'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
alien_0['color']='blue'
print(alien_0)
```

```
{'color': 'blue', 'points': 5, 'x_position': 0, 'y_position': 25}
```

### 删除键-值对

**del**

```python
alien_0={'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
del alien_0['color']
print(alien_0)
```

```
{'points': 5, 'x_position': 0, 'y_position': 25}
```

### 遍历字典

#### 遍历键-值对    .items()

```python
alien_0={'color': 'green', 'points': '5', 'x_position': '0', 'y_position': '25'}
for key, value in alien_0.items():
	print("key:"+key)
	print("value:"+value)
```

不报错

```
key:color
value:green
key:points
value:5
key:x_position
value:0
key:y_position
value:25
```



```python
alien_0={'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
for key, value in alien_0.items():
	print("key:"+key)
	print("value:"+value)
```

报错（原因在于后面三个键值对的值是整型数字）

```
key:color
value:green
key:points
Traceback (most recent call last):
  File "D:\PYTHONSPACE\�ֵ�.py", line 30, in <module>
    print("value:"+value)
TypeError: cannot concatenate 'str' and 'int' objects
[Finished in 0.3s with exit code 1]
[shell_cmd: python -u "D:\PYTHONSPACE\字典.py"]
[dir: D:\PYTHONSPACE]
```

解决办法

```python
alien_0={'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
for key,value in alien_0.items():
	print("key:"+str(key))#直接将所有key值转为str再输出，既不影响源字典的数据类型，也能成功输出
	print("value:"+str(value))
```

#### 遍历键  .keys()

```python
alien_0={'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
for key in alien_0.keys():
	print(key)
```

```
color
points
x_position
y_position
```

**按顺序遍历键**

```python
alien_0={ 'points': 5, 'x_position': 0, 'y_position': 25,'color': 'green',}
for key in alien_0.keys():
 	print(key)
for key in sorted(alien_0.keys()):
	print(key)
```

```
color
points
x_position
y_position
color
points
x_position
y_position
```

#### 遍历值  .values()

```python
alien_0={'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 5}
for value in alien_0.values():
	print(value)
```

```
green
5
0
5
```

#### 去除重复值  .set(         )

```python
alien_0={'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 5}
for value in set(alien_0.values()):
	print(value)
```

```
0
green
5
```

### 嵌套

**字典和列表可以相互嵌套也可以自己嵌套自己**

#### 在列表中存储字典

建立30个外星人字典，并存到外星人列表中

```python
aliens=[]

for alien_number in range(30):
	new_alien={'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 5}
	aliens.append(new_alien)

for alien in aliens[0:5]:
	print(alien)

print(str(len(aliens)))
```

修改外星人列表中前5个外星人的部分值

```python
aliens=[]

for alien_number in range(30):
	new_alien={'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 5}
	aliens.append(new_alien)


for alien in aliens[:5]:
	if alien['color']=='green':
		alien['color']='yellow'
		alien['points']=8



for alien in aliens[0:10]:
	print(alien)

print(str(len(aliens)))
```

```
{'color': 'yellow', 'points': 8, 'x_position': 0, 'y_position': 5}
{'color': 'yellow', 'points': 8, 'x_position': 0, 'y_position': 5}
{'color': 'yellow', 'points': 8, 'x_position': 0, 'y_position': 5}
{'color': 'yellow', 'points': 8, 'x_position': 0, 'y_position': 5}
{'color': 'yellow', 'points': 8, 'x_position': 0, 'y_position': 5}
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 5}
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 5}
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 5}
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 5}
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 5}
30
```

还可以用elif继续修改

#### 在字典中存储列表

#### 在字典中存储字典





#### 练习

##### #1

```python
dog={'type':'land','hostname':'alan'}
cat={'type':'land','hostname':'barry'}
bird={'type':'sky','hostname':'elizabeth'}
pets=[dog,cat,bird]
for pet in pets:
	for key,value in pet.items():
		if key=='type':
			print(value)

```

```
land
land
sky
```

##### #2

## #6用户输入和while循环

### 6.1 input()和int()

通过前面的学习我们使用的最多的语句莫过于print()了这个语句可以将括号内的内容进行输出。

那么python的输入语句是什么呢？

input()

input()可以接受一个参数，即要向用户显示的提示或说明。**但是输入内容为字符串**

```python
#7.1使用input来获取输入的字符串
prompt = "If you tell us who you are, we can persionlize the message you see."
prompt += "\nWhat is your name?"
name = input(prompt)
print("\nHello, " + name + "!")
```

Result

```
If you tell us who you are, we can persionlize the message you see.
What is your name?Alan

Hello, Alan!
```

input()获取的值为字符串格式，如果想获取一个整数值则使用int()

int()可以输入数值。**输入内容为整型数**

```python
#7.2使用int()来获取数值输入
age = input("How old are you?\n")
age = int(age)
print("I am {:.0f} years old.".format(age))
```

Result:

```
How old are you?
23
I am 23 years old.
```

### 6.2 取模运算

```python
#7.3求摸运算符
num = 4%3
print(num)
num = 5%3
print(num)
num = 6%3
print(num)
num = 7%3
print(num)
```

Result：

```
1
2
0
1
```

取模运算得到的结果是余数。利用这个特性，经常用来寻找某个数的倍数。

例如，一名农夫种了一片菜地，为了菜苗茁壮成长，在未来的100天内，需要每2天要浇一次水，每5天除一次虫。请问分别在第几天浇水，第几天除虫。

Action!

```python
water_day = []
bug_day = []
for i in range(1,101):
    if i % 2 == 0:
        water_day.append(i)
    elif i%5==0:
        bug_day.append(i)
print('需要浇水的日子有')
for d in water_day:
    print(d,end=' ')
print('\n需要除虫的日子有')
for b in bug_day:
    print(b,end=' ')
```

Result:

```
需要浇水的日子有
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100 
需要除虫的日子有
5 15 25 35 45 55 65 75 85 95 
```



### 6.x while

#### **while后面的布尔值为true则执行while中的循环**

#### break：退出循环

#### continue：继续循环



## #7函数

```python
def 函数名(形参):
    函数体
#函数调用
函数名(实参)
```

### 实参传递

#### 位置实参

```python
函数名('实参','实参')#实参严格按照顺序
```

#### 关键字实参

```python
函数名(形参='实参'，形参='实参')#实参顺序不重要
```

**实参可以传递一个列表**



#### 形参的默认值

在定义函数的时候可以给形参设置默认值

```python
def 函数名(形参1,形参2='默认实参'):#若调用函数时，只为形参1传递实参，则形参2默认为其默认实参
```

#### 返回值     return

```python
def 函数名(形参):
    函数体
    return 返回值
函数名(实参)#得到的是返回值
```

**返回值可以是字符、也可以是字典**

**函数可以无限传参**

```python
def 函数名(*形参) //形参前加一个 ‘ * ’ 号即可无限传参
```





## #8类

### 创建类





## #9文件和异常

## #10测试代码

## 项目一：外星人入侵

### **工具准备**

pygame

要用python写一个小游戏，需要借助pygame的帮助。

pygame的安装也非常的简单

```
pip install pygame
```

在cmd中，用以上语句安装即可。

**为了在Pycharm中正常使用pygame**

需要执行一下步骤：

打开Pycharm，File——Settings——Project:WorkSpace——Python Interpreter

点击右侧加号，在其中搜索Pygame，再点击Install即可（PS：这里可能需要点时间加载，耐心等待）

### 1开始游戏项目

#### 1.1创建Pygame窗口以及响应用户输入

一切准备就绪，运行一个简单的代码，生成一个游戏窗口

```python
import sys
import pygame

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("Alien Invasion")
	bg_color = (230,230,230)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.fill(bg_color)
		pygame.display.flip()

run_game()
```

运行结果：

![image-20210706171021793](C:\Users\Alan\Desktop\Python学习文档\Images\image-20210706171021793.png)

好啦，一个游戏面板诞生了，之后在上面添加一些有趣的东西吧。















## 项目二：数据可视化

## 项目三：Web应用程序