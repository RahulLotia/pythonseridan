import turtle
import random

#will create a screen/racetrack
racetrack = turtle.Screen()
racetrack.bgcolor("black")

#create a turtle named jack
jack = turtle.Turtle()
jack.penup()

#apply shape to jack
jack.shape("turtle")

#apply color to jack
jack.color("yellow")
jack.left(90)
jack.pendown()


#face jack up/North
#jack.left(90)

#jack.forward(150)
#jack.right(90)
#jack.forward(100)
#jack.right(90)
#jack.forward(150)
#jack.right(90)
#jack.forward(100)

#create another turtle
jill = turtle.Turtle("turtle")
jill.penup()
jill.color("red")
jill.left(90)



jill.left(90)
jill.forward(100)
jill.right(90)

jill.pendown()


#create another turtle
jim = turtle.Turtle("turtle")
jim.penup()
jim.color("pink")
jim.left(90)
jim.right(90)
jim.forward(100)
jim.left(90)

jim.pendown()


#setup of race
#get rendom distance
distancejack = random.randint(100,200)
jack.forward(distancejack)

distancejill = random.randint(100,200)
jill.forward(distancejill)

distancejim = random.randint(100,200)
jim.forward(distancejim)


#declare the winner
#compare the more
#distancejim == distancejill == distancejack

print("Jack's distance = ", distancejack)
print("Jill's distance = ", distancejill)
print("Jim's distance = ", distancejim)

#compare dif method
if distancejack > distancejill and distancejack > distancejim:
    print("Jack is the winner")
elif distancejill > distancejim and distancejill > distancejack:
    print("Jill is winner")
elif distancejim > distancejill and distancejim > distancejill:
    print("Jim is the winner")

#compare on racetrack
if jack.ycor() > jill.ycor() and jack.ycor() > jim.ycor():
    print("Jack is the winner via yaxis")
elif jill.ycor() > jim.ycor() and jill.ycor() > jack.ycor():
    print("Jill is winner via yaxis")
elif jim.ycor() > jill.ycor() and jim.ycor() > jill.ycor():
    print("Jim is the winner via yaxis")


#screen should wait until we manually close it
racetrack.exitonclick()