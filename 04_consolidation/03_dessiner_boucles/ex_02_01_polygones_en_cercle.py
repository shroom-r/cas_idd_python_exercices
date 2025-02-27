import turtle as t
import math

def drawPolygonesInCircle(nSides, nPolygones):
    t.clearscreen()
    polyAngleStep = 360 / nSides
    angleStep = 360 / nPolygones

    forwardStep = 2*math.cos(math.radians((180-polyAngleStep)/2)) * 100

    for i in range(nPolygones):
        for side in range( nSides):
            t.forward(forwardStep)
            t.right(polyAngleStep)
        t.right(angleStep)
