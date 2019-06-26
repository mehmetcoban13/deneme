import turtle, random, time
def polygon(sides, length, color):
    turtle.penup()
    if sides == 4:
        turtle.setposition(-length/2, -length/2)
    elif sides == 3:
        turtle.setposition(-(length/2), -(length/4*(3**(1/2))))
    else:
        turtle.setposition(-length/2, -length/2)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(length)
        turtle.left(360//sides)
        turtle.end_fill()
    #input() # to stop the function
    time.sleep(10)

def ddAlanHesaplama(a,b):
    return a * b

def kareAlanHesaplama(a):
    return ddAlanHesaplama(a,a)

#print("Dikdörtgen Alanı :", ddAlanHesaplama(1,3), "\nKare Alanı :", kareAlanHesaplama(3))
#polygon(4, 300, "darkred")
polygon(5, 100, "blue")