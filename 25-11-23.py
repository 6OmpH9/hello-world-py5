import py5

h = 30
v = 30
x = 300
y = 300
dia = 18
angle = 0.0
inc = 1.618/py5.TWO_PI/25.0
i = 0


def setup():
    py5.size(600, 600)


def draw():
    global angle
    py5.background(10)
    for j in range(10):
        for a in range(i, i < 600, i+16):
            py5.rotate(py5.radians(a))
            py5.stroke(0, 255, 0, 100)
            py5.stroke_weight(1)
            py5.fill(0, 255, 0, 10)
            py5.line(h + j * 60, y+py5.sin(py5.radians(angle))*9,
                     h + j * 60, y+py5.sin(py5.radians(angle))*270)
            # py5.line(x + py5.sin(py5.radians(angle))*270, v + j * 60,
            #         x + py5.sin(py5.radians(angle))*9, v + j * 60)
            # py5.ellipse(h + j * 60, y, dia, dia)
            # py5.ellipse(h + j * 60, y+py5.sin(py5.radians(angle))
            #            * 270, dia, dia)
            py5.ellipse(x, v+py5.sin(py5.radians(angle)) + j * 60, dia, dia)
            # py5.ellipse(x+py5.sin(py5.radians(angle))
            #            * 270, v + j * 60, dia, dia)

        angle += inc


py5.run_sketch()
