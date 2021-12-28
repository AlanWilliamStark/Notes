import random
x = 1
while True:
    set=[]
    upordown = random.choice([0, 1])
    if upordown == 0:
        print('1')
        set.append(1)
    elif upordown == 1:
        print('2')
        set.append(2)

    x+=1
    if x >100:
        print(set)
        break
