import turtle as t
#circle的半径为正，圆心在左侧
# for i in range(1,8,2):
#     t.seth(45*i)
#     t.fd(100)
#     t.left(90)
#     t.circle(-100,45)
#     t.left(90)
#     t.fd(100)
# t.done()

for i in range(1,5):
    t.seth(-90*i)
    t.fd(100)
    t.right(90)
    t.circle(-100,45)
    t.right(90)
    t.fd(100)
t.done()
