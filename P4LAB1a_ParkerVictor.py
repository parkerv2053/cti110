import turtle as vp
win = vp.Screen()


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
