import turtle as t
t.setup(1000,1000,0,0)
t.pensize(4)
for i in range(1,7):
    t.fd(100)
    t.seth(60 * i)
t.done()
