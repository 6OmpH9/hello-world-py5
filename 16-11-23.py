import py5

# The inspiration for this code comes from
# thedotisblack.com, IG @thedotisblack.com


x = 300
y = 300
angle = 0  # Initialized the rotation angle
dia = 20


def setup():

    py5.size(600, 600)


def draw():

    global angle  # Declare angle as a global variable
    py5.background(10, 10, 10, 0)
    py5.translate(py5.width/2, py5.height/2)

    for a in range(0, 360, 10):
        py5.push_matrix()
        py5.rotate(py5.radians(a))  # Rotate by the current angle
        py5.stroke(255)
        py5.stroke_weight(3)
        py5.line(x*py5.sin(py5.radians(angle)), 0, 0, y-dia/2)

        py5.no_stroke()
        py5.fill(255)
        py5.ellipse(x*py5.sin(py5.radians(angle)), 0, dia/2, dia/2)
        py5.stroke(255)
        py5.no_fill()
        py5.ellipse(0, y, dia, dia)
        py5.pop_matrix()

        angle += 0.01


py5.run_sketch()
