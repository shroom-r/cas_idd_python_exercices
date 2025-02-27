import turtle as t
import math

circleIsDrawn = False

def drawCircle(radius):
    global circleIsDrawn
    if not circleIsDrawn:
        t.circle(radius)
        circleIsDrawn = True

def draw_inscribed_polygone(nSides, circleRadius):
    drawCircle(circleRadius)
    angleStep = 360/nSides
    forwardStep = 2*math.cos(math.radians((180-angleStep)/2)) * circleRadius
    t.left(angleStep/2)
    while True:
        t.forward(forwardStep)
        t.left(angleStep)
        if (abs(t.pos()) < 1):
            t.right(angleStep/2)
            break
