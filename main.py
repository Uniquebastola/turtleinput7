import turtle
import random
screen=turtle.Screen()

screen.screensize(500,500)
screen.bgcolor('black')

t=turtle.Turtle()
#menu
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor('white')
t.write("Background Color",font=("arial",30,"normal"),align="center")

t.penup()
t.goto(-75,100)
t.pendown()
t.pencolor('tan')
t.write("1. tan",font=("arial",20,"normal"),align="left")

t.penup()
t.goto(-75,50)
t.pendown()
t.pencolor('azure')
t.write("2. azure",font=("arial",20,"normal"),align="left")

t.penup()
t.goto(-75,0)
t.pendown()
t.pencolor('aquamarine')
t.write("3. aquamarine",font=("arial",20,"normal"),align="left")

t.penup()
t.goto(-75,-50)
t.pendown()
t.pencolor('DarkKhaki')
t.write("4. DarkKhaki",font=("arial",20,"normal"),align="left")

t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor('white')
t.write("Select A Color",font=("arial",30,"normal"),align="left")

choose = int(input("select a color"))
if choose == 1:
    screen.bgcolor("tan")
elif choose == 2:
    screen.bgcolor("azure")
elif choose == 3:
    screen.bgcolor("aquamarine")
elif choose == 4:
    screen.bgcolor("darkkhaki")
t.clear()

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('black')
t.write("enter your name",font=("arial",30,"normal"),align="left")

name = input("what your name be: ")
t.clear()
# number = int(input("enter your number:"))
# num2 =   int(input("enter your second number:"))
operation = random.randint(1,4)
if operation == 1:
    symbol = "+"
    number= random.randint(-100,100)
    num2= random.randint(-100,100)
    solution = number + num2

elif operation == 2:
    symbol = "-"
    number= random.randint(-100,100)
    num2= random.randint(-100,100)
    solution = number - num2

elif operation == 3:
    symbol = "*"
    number= random.randint(-10,10)
    num2= random.randint(-10,10)
    solution = number * num2


elif operation == 4:
    symbol = "/"
    number= random.randint(-10,10)
    num2 = random.randint(1,10)
    sign = random.randint (1,2)
    if sign == 2:
        num2 = -1 * num2
    solution = number / num2


t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor('blue')
t.write(number,font=("arial",30,"normal"),align="center")

t.penup()
t.goto(-100,0)
t.pendown()
t.pencolor('yellow')
t.write(symbol,font=("arial",30,"normal"),align="center")

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('blue')
t.write(num2,font=("arial",30,"normal"),align="center")

t.penup()
t.goto(0,100)
t.pendown()
t.pencolor('blue')
t.write(name,font=("arial",30,"normal"),align="center")

t.penup()
t.goto(100,0)
t.pendown()
t.pencolor('blue')
t.write("=",font=("arial",30,"normal"),align="center")

ans=float(input("enter the answer:"))

t.penup()
t.goto(200,0)
t.pendown()
t.pencolor('blue')
t.write(solution,font=("arial",30,"normal"),align="center")

t.penup()
t.goto(0,250)
t.pendown()
t.pencolor('black')
t.write("your answer: "+str(ans),font=("arial",30,"normal"),align="center")

if ans == solution:
    screen.bgcolor("dodgerblue")
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.pencolor('black')
    t.write("correct", font=("arial", 30, "normal"), align="center")
else:
    screen.bgcolor('darkorange')
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.pencolor('black')
    t.write("incorrect", font=("arial", 30, "normal"), align="center")

turtle.done()