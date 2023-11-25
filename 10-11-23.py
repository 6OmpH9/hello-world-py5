import py5


def setup():
    py5.size(595, 742)
    py5.background(155)

# Top square


x = py5.width/2  # Horizontal axis (from left)
y = py5.height/2  # Vertical axis (from top)
w = 100  # With in pixels
h = w   # This will create a square

# Image revealed

xco = 400
yco = 440


def draw():
    py5.fill(30)
    py5.rect(x, y, w, h)

    py5.fill(255)
    py5.stroke(90)
    py5.stroke_weight(1)
    py5.line(py5.width/2, py5.height/3, xco, yco)
    py5.ellipse(py5.width/11, py5.height/14, py5.width/11, py5.height/14)
    py5.ellipse(py5.width/19, py5.height/22, py5.width/19, py5.height/22)
    py5.line(xco, yco, py5.width-xco, yco)
    py5.line(py5.width-xco, yco, py5.width/2, py5.height/3)
    py5.ellipse(py5.width/5, py5.height/8, py5.width/5, py5.height/8)
    py5.no_fill()
    py5.arc(py5.width/2, py5.height/2, 200, 200, 0, 2)
    py5.arc(py5.width/2, py5.height/2, 300, 300, 0, py5.PI)
    py5.arc(py5.width/2, py5.height/2, 400, 400, 0, py5.TAU)
    py5.arc(py5.width/2, py5.height/2, 350, 350,
            3.4, py5.TAU-py5.HALF_PI, py5.PIE)


py5.run_sketch()

# Take notice of PI, TAU, HALF_PI, PIE.
