import turtle            # set up alex
#wn = turtle.Screen()
#alex = turtle.Turtle()
#d=0
#e=0
#for c in ["red", "blue", "yellow","green"]:
#    d=d+40
#    for i in range(4):      # repeat four times
#        alex.color(c)
#        alex.forward(70+d)
#        alex.left(90)
#        alex.shape("circle")
#
#wn.exitonclick()

wn = turtle.Screen()
jose = turtle.Turtle()
jose.shape("turtle")
jose.penup()
for size in range(10):
    jose.forward(50)
    jose.stamp()
    jose.forward(-50)
    jose.right(36)
wn.exitonclick()
