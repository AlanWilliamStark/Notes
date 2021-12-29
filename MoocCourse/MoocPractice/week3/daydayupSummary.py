import random
def dayUP(df,dayup):
    for i in range(365):
        dayup = dayup+df
    print("在此模式下，努力一年的结果是{:.3f}".format(dayup))
def choice():
    print("1.每天努力0.001")
    print("2.每天努力0.005")
    print("3.每天努力0.01")
    print("4.工作日努力0.019，休息日下降0.001")
    print("5.随机努力与否")
    x = eval(input("选择你的努力模式"))
    if x == 1:
        dayUP(0.001,1)
    elif x==2:
        dayUP(0.005,1)
    elif x==3:
        dayUP(0.01,1)
    elif x==4:
        dayUpwork(0.019,0.001,1)
    elif x==5:
        dayUprand()
    else:
        return('break')
def dayUprand():
    duf = random.choice([0.001,0.002,0.003,0.004,00.005,0.006,0.007,0.008,0.009,0.01])
    ddf = 0.001


    # upday = random.randint(1,365)
    dayup = 1
    for i in range(365):
        upordown = random.choice([0, 1])
        if upordown == 0:
            dayup = dayup+duf
        elif upordown == 1:
            dayup = dayup-ddf
    print("在随机模式下，努力一年的结果是{:.3f}".format(dayup))
def dayUpwork(duf,ddf,dayup):
    for i in range(1,366):
        if i%7 in [6,0]:
            dayup = dayup+duf
        else:
            dayup = dayup-ddf
    print("在工作日模式下，努力一年的结果是{:.3f}".format(dayup))
while True:
    choice()
