from turtle import *
screensize(5000, 5000)
speed(5)


def up():
    fd(20)
def down():
    bk(20)
def left():
    lt(15)
def right():
    rt(15)

def pen_up():
    penup()
def pen_down():
    pendown()
def clear_scr():
    penup()
    clear()
    home()
    pendown()

onkeypress(up, "Up")
onkeypress(up, "w")
onkeypress(up, "W")

onkeypress(down, "Down")
onkeypress(down, "s")
onkeypress(down, "S")

onkeypress(left, "Left")
onkeypress(left, "a")
onkeypress(left, "A")

onkeypress(right, "Right")
onkeypress(right, "d")
onkeypress(right, "D")

onkeypress(pen_up, "space")
onkeypress(pen_down, "Shift_L")

onkeypress(clear_scr, "Escape")

listen()
done()