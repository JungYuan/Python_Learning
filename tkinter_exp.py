import turtle as ttl
from math import *


def coor_ax(tur_obj):
    tts = tur_obj.getscreen()
    x_limit = tts.window_width()/2 - 10
    y_limit = tts.window_height()/2 - 10
    tts.reset()
    tts.bgcolor("pink")
    tur_obj.up()
    tur_obj.hideturtle()
    tur_obj.clear()
    tur_obj.speed(0)
    tur_obj.goto(-1*x_limit, 0)
    tur_obj.pencolor("yellow")
    tur_obj.down()
    tur_obj.goto(x_limit, 0)
    tur_obj.stamp()
    tur_obj.up()
    tur_obj.goto(0, -1*y_limit)
    tur_obj.down()
    tur_obj.lt(90)
    tur_obj.goto(0, y_limit)
    tur_obj.stamp()
    tur_obj.up()
    tur_obj.rt(90)
    tur_obj.speed(3)
    return (x_limit, y_limit)
    
def xy_function(x, orders, coef):
    y = 0
    for i in range(orders+1):
        y += coef[i]*((sin(x)**i)+cos(x)**i)
    return y
        
    
tt = ttl.Turtle()
tl_screen = tt.getscreen();
tl_screen.title("Draw a function diagram")
#tt_2 = ttl.Turtle()
#tt_2.shape("turtle")
max_x, max_y = coor_ax(tt)
fun_a=[0, 1, 1, 1]
order = 3
max_ax = 10
max_ay = 5
tt.goto(-1*max_x, 0)
tt.write(str(-1*max_ax), align="left")
tt.goto(max_x, 0)
tt.write(str(max_ax), align = "right")
tt.goto(0, -1*max_y)
tt.write(str(-1*max_ay), align="right")
tt.goto(0, max_y-20)
tt.write(str(max_ay), align = "right")
ratio_x = max_x / max_ax
ratio_y = max_y / max_ay
#to first point
tt.speed(0)
draw_x = -1*max_x
draw_y = xy_function(draw_x/ratio_x, order, fun_a)*ratio_y
while(abs(draw_y) > max_y):
    draw_x += 1
    draw_y = xy_function(draw_x/ratio_x, order, fun_a)*ratio_y
tt.goto(draw_x, draw_y)
tt.pencolor("blue")
tt.down()
tt.speed(3)
while(abs(draw_y) <= max_y):
    tt.goto(draw_x, draw_y)
    draw_x += 1
    draw_y = xy_function(draw_x/ratio_x, order, fun_a)*ratio_y
    if (draw_x > max_x):
        draw_y = max_y+1
tt.up()
tt.goto(0, 0)
tl_screen.exitonclick()
