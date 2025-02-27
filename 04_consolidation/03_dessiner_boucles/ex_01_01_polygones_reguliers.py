import turtle as t

def draw_polygone(n):
    angleStep = 360/n
    forwardStep = 200 / n
    while True:
        t.forward(forwardStep)
        t.right(angleStep)
        if (abs(t.pos()) < 1):
            break
    # t.mainloop()