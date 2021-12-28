import turtle
#turtle.setup(width.height,startx,starty)
#设置框体，四个参数分别是：宽，高，左上角在屏幕的位置的x值，左上角在屏幕位置的y值,若后面两个参数为空，则默认上居中
turtle.setup(1300,350,10,200)
#用penup()先把笔抬起来
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor('purple')
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()