class ff2cc:
    def fc(self,Temp):
        if Temp[-1] in ['F', 'f']:
            new_Temp = (eval(Temp[0:-1])-32)/1.8
            print("转化后的温度是{:.2f}C".format(new_Temp))
        elif Temp[0] in ['F','f']:
            new_Temp = (eval(Temp[1:])-32)/1.8
            print("转化后的温度是{:.2f}C".format(new_Temp))


    def check(Temp):
        if Temp[-1] in ['F','f'] or Temp[0] in ['F','f']:
            ff2cc.fc(ff2cc,Temp)
        elif Temp[-1] in ['C','c'] or Temp[0] in ['C','c']:
            ff2cc.cf(ff2cc,Temp)
        else:
            print("输入有误")

    def cf(self,Temp):
        if Temp[-1] in ['C', 'c']:
            new_Temp = 1.8*eval(Temp[0:-1])+32
            print("转化后的温度是{:.2f}F".format(new_Temp))
        elif Temp[0] in ['C','c']:
            new_Temp = 1.8*eval(Temp[1:])+32
            print("转化后的温度是{:.2f}F".format(new_Temp))
        # if Temp[-1] in ['F','f'] :
        #     new_Temp = (eval(Temp[0:-1])-32)/1.8
        #     print("转化后的温度是{:.2f}C".format(new_Temp))
        # elif Temp[0] in ['F','f']:
        #     new_Temp = (eval(Temp[1:])-32)/1.8
        #     print("转化后的温度是{:.2f}C".format(new_Temp))
        # elif Temp[-1] in ['C','c']:
        #     new_Temp = 1.8*eval(Temp[0:-1])+32
        #     print("转化后的温度是{:.2f}F".format(new_Temp))
        # elif Temp[0] in ['C','c']:
        #     new_Temp = 1.8*eval(Temp[1:])+32
        #     print("转化后的温度是{:.2f}F".format(new_Temp))
        # else:
        #     print("输入有误")
