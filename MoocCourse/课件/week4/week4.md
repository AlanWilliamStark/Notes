# 程序的控制结构

顺序、选择、循环

省略if   elif   else等一堆基础知识



## 异常处理

```python
try:
	<语句块1>
except:
	<语句块2>
	
try:
	<语句块1>
except <异常类型>:
	<语句块2>
```

例如

```python
try :
	num = eval(input("请输入一个整数: "))
	print(num**2)
except :
	print("输入不是整数")
```

当程序发生异常时，执行except后面的语句

```python
try :
num = eval(input("请输入一个整数: "))
	print(num**2)
except NameError:
	print("输入不是整数")
```

## 异常处理2

```python
try:
	<语句块1>
except:
	<语句块2>
else:
	<语句块3>
#else对应的语句块3在不发生异常时执行
finally:
	<语句块4>
#finally对应的语句块4一定执行

```

## random库

```python
import random as rd

rd.seed(8)
a = rd.random()
b = rd.random()
c = rd.random()
print(a)
print(b)
print(c)
```

0.2267058593810488
0.9622950358343828
0.12633089865085956

### 扩展随机数函数

|         函数         |                             描述                             |
| :------------------: | :----------------------------------------------------------: |
|    randint(a, b)     |    生成一个[a, b]之间的整数 >>>random.randint(10, 100) 64    |
| randrange(m, n[, k]) | 生成一个[m, n)之间以k为步长的随机整数 >>>random.randrange(10, 100, 10) 80 |
|    getrandbits(k)    |  生成一个k比特长的随机整数 >>>random.getrandbits(16) 37885   |
|    uniform(a, b)     | 生成一个[a, b]之间的随机小数 >>>random.uniform(10, 100) 13.096321648808136 |
|     choice(seq)      | 从序列seq中随机选择一个元素 >>>random.choice([1,2,3,4,5,6,7,8,9]) 8 |
|     shuffle(seq)     | 将序列seq中元素随机排列，返回打乱后的序列 >>>s=[1,2,3,4,5,6,7,8,9];random.shuffle(s);print(s) [3, 5, 8, 9, 6, 1, 2, 7, 4] |





### 计算圆周率

```python
import random as rd
from time import perf_counter

darts = 100000000
hits = 0.0
start = perf_counter()
for i in range(1,darts+1):
    x,y = rd.random(),rd.random()
    dist = pow(x**2+y**2,0.5)
    if dist<=1.0:
        hits = hits+1
pi = 4*(hits/darts)
print('圆周率的值为{}'.format(pi))
print('运行时间为：{:.5f}s'.format(perf_counter()-start))
```