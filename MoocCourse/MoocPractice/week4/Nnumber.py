Nnums = []
for i in range(100,1000):
    if pow(eval(str(i)[0]),3)+pow(eval(str(i)[1]),3)+pow(eval(str(i)[2]),3) == i:
        Nnums.append(i)
print(*Nnums,sep = ',')