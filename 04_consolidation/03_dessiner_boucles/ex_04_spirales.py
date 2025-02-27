import turtle as t

def spiral(nTurns, space):
    t.speed(0)
    t.clearscreen()
    t.color('red')
    for i in range(4):
        while True:
            t.forward(20)
            t.right(90)
            if abs(t.pos()) < 1:
                break
        t.right(90)
    t.color('black')
    for turn in range(nTurns * 4):
        t.forward(20 + turn * space / 2)
        t.right(90)

spiral(5,10)