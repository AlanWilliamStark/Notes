count = 0
for i in range(1,967):
    if i%2 == 1:
        a = i
        print(a)
    elif i%2 == 0:
        a = -i
        print(a)
    count = count+a
print(count)