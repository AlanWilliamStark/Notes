n = input()
word = 'Hello World'
l = len(word)
if eval(n)>0:
    for x in range(l):
        print(word[x],end='') if x%2==0 else print(word[x])
elif eval(n)<0:
    for x in word:
        print(x)
else:
    print(word)
