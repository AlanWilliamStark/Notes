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