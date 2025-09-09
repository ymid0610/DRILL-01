import turtle

for x,y,r in [
    (0,0,10),
    (90,90,90),
    (0,90,10),
    (90,190,90), ]:
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(r)
    turtle.write(str((x,y)))
