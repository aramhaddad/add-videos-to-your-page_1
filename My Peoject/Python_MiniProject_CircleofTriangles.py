

import turtle
def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    
    #brad = turtle.Turtle()
    #brad.shape("turtle")
    #brad.color("yellow")
    #brad.speed(5)
    #for a in range(1,37):
    #    for i in range(1,5):
    #        brad.forward(100)
    #        brad.right(90)
    #    brad.right(10)
        
   

    #angie = turtle.Turtle()
    #angie.circle(100)
    #angie.shape("arrow")
    #angie.color("blue")

    aram = turtle.Turtle()
    aram.color("blue")
    aram.shape("turtle")
    aram.left(90)
    aram.forward(200)
    for a in range(1,50):
            for i in range(1,4):
                aram.forward(100)
                aram.right(120)
            aram.right(10)
    #a = 0
    #while a < 3:
    #    aram.forward(100)
    #    aram.right(120)
    #   a = a + 1

    
    window.exitonclick()

draw_shapes()
