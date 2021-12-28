import random as rd
bits = eval(input())
round = 0.0
rd.seed(123)
for i in range(1,bits+1):
    x,y = rd.random(),rd.random()
    if pow(x**2+y**2,0.5)<1:
        round = round+1
print('{:.6f}'.format(4*round/bits))
