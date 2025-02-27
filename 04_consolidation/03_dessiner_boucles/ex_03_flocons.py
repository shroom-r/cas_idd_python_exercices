import turtle as t

def drawSnowFlake(nBranches):
    angleStep = 360 / nBranches
    t.speed(0)
    t.width(3)
    for i in range(nBranches):
        t.forward(100)
        t.left(30)
        for j in range(3):
            t.forward(20)
            t.up()
            t.backward(20)
            t.down()
            t.right(30)
        t.left(60)
        t.up()
        t.backward(100)
        t.down()
        t.left(angleStep)
        # if abs(t.pos()) < 1:
        #     break

drawSnowFlake(10)