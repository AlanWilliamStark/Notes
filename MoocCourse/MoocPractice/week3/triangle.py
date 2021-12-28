x = eval(input())
for i in range(1,x+1,2):
    print("{0:^{1}}".format('*'*i,x))
    # print("{}{}".format(' '*((x-i)//2),'*'*i))