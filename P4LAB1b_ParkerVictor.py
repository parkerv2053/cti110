import turtle as vp
win = vp.Screen()

vp.pensize(6)   #display look
vp.shape("turtle")

vp.color('green')
vp.penup()  #movement to place it right
vp.right(180)
vp.forward(300)
vp.right(180)
vp.pendown()
vp.right(70)    #begining of initials VP
vp.forward(100)
vp.left(130)
vp.forward(100)
vp.penup()
vp.right(60)
vp.forward(50)
vp.pendown()
vp.right(90)
vp.forward(100)
vp.right(180)
vp.forward(100)
vp.circle(-30)
vp.penup()  #movement to the start of square
vp.right(90)
vp.forward(200)
vp.pendown()
    

   

for ugh in [0,1,2,3]:   #square
    vp.color('blue')
    vp.forward(100)
    vp.right(90)

vp.penup()
vp.forward(150)
vp.pendown()

for tri in [0,1,2]: #triangle
    vp.color('red')
    vp.forward(100)
    vp.right(120)

#it is ended
win.mainloop()
