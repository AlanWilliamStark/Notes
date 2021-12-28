height,weight = eval(input())
c ,a = '',''
x = weight/pow(height,2)
if x < 18.5:
    a = '偏瘦'
    c = '偏瘦'
elif 18.5 < x < 24:
    a = '正常'
    c = '正常'
elif 24<x<25:
    a = '正常'
    c = '偏胖'
elif 25<x<28:
    a = '偏胖'
    c = '偏胖'
elif 28<x<30:
    a = '偏胖'
    c = '肥胖'
elif x>30:
    a = '肥胖'
    c = '肥胖'
print('BMI数值为:{:.2f}'.format(x))
print("BMI指标为:国际'{}',国内'{}'".format(a,c))