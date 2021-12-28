import turtle as t
t.setup(1000,500)
t.penup()
t.fd(-400)
t.pendown()
t.pensize(15)
t.pencolor('purple')
t.seth(-40)
for i in range(4):
    t.circle(40,80)
    t.circle(-40,80)
t.circle(40,40)
t.fd(60)
t.circle(16,180)
t.fd(30)
t.done()


