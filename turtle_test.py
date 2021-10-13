import turtle as t

"""
    TODO: узнать размер экрана пользователя
        Узнать корды
"""

def draw_square(side_lenght):
    for i in range (4):
        t.forward(side_lenght)
        t.left(90)

# setup
t.shape("turtle")
t.speed(1)
t.pencolor("#00FF00")
t.pensize(2)
t.goto(0, 0)
t.setheading(0)

#выполнение
draw_square(20)
draw_square(200)
draw_square(400)
draw_square(600)


#ждём выхода
t.done()
