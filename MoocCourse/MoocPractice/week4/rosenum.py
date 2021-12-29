for s in range(1000,10000,1):
    if eval(str(s)[0])**4+eval(str(s)[1])**4+eval(str(s)[2])**4+eval(str(s)[3])**4 == s:
        print(s)
