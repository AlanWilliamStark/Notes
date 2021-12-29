Temp = input()
if Temp[-1] in ['C','c']:
    new_Temp = eval(Temp[:-1])*1.8+32
    print("{:.2f}F".format(new_Temp))
elif Temp[-1] in ['F','f']:
    new_Temp = (eval(Temp[:-1])-32)/1.8
    print("{:.2f}C".format(new_Temp))
else:
    print("输入格式错误")