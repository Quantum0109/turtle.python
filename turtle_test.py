import turtle as t

"""
    TODO: узнать размер экрана пользователя
          узнать корды
"""

def draw_square(side_lenght = 30, x = -100, y = -100, line_color = "#FF3300", pen_size = 1):
    # setup
    t.penup()
    t.goto(x, y)
    t.pencolor(line_color)
    t.pensize(pen_size)
    t.pendown()

    for number in range (4):
        t.forward(side_lenght)
        t.left(90)
    t.setheading(0)

# general setup
t.shape("turtle")
t.speed(1)


# выполнение
draw_square(line_color = "#FFFF00", x = 150, side_lenght = 100, pen_size = 10)


# ждём выхода
t.done()
