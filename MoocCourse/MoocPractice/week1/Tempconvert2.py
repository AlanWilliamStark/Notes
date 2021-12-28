Temp = input()
if Temp[0] in ['C','c']:
    new_Temp = eval(Temp[1:])*1.8+32
    print("F{:.2f}".format(new_Temp))
elif Temp[0] in ['F','f']:
    new_Temp = (eval(Temp[1:])-32)/1.8
    print("C{:.2f}".format(new_Temp))