from myShape import move

def polygon(t,d,s):
  a = 360 / s
  t.begin_fill()
  for times in range(s):
    t.fd(d)
    t.left(a)
  t.end_fill()

def bgdesign(t):
    move(t,-55,0)
    t.left(90)
    t.color(255,0,0)
    t.begin_fill()
    for times in range(36):
        for times in range(10):
            t.fd(1)
            t.right(1)
        t.left(90)
        t.fd(1000)
        t.back(1000)
        t.right(90)
    t.end_fill()

def spiny(t):
  move(t,-55,0)
  for times in range(36):
    polygon(t,20,3)
    for times in range(10):
      t.fd(1)
      t.right(1)


def spiral(t):
  t.color(100,100,100)
  move(t,55,-55)
  for times in range(800):
    t.fd(100 - times  * 2)
    t.left(90)

    


