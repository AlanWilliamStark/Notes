user = 'Kate'
password = '666666'

count = 0
while True:
    u = input()
    p = input()
    if u == user and p == password:
        print('登录成功！')
        break
    if u!=user or p!=password:
        count+=1
    if count==3:
        print('3次用户名或者密码均有误！退出程序。')
        break