import py5

# The inspiration for this code comes from
# thedotisblack.com, IG @thedotisblack.com


x = 300
y = 300
angle = py5.radians(45)


def setup():

    py5.size(600, 600)


def draw():

    py5.background(10, 10, 10, 0)
    py5.translate(py5.width/2, py5.height/2)

    for a in range(0, 360, 10):
        py5.push_matrix()
        py5.rotate(py5.radians(a))
        py5.stroke(255)
        py5.stroke_weight(3)
        py5.line(x*py5.sin(angle), 0, x, y)
        py5.pop_matrix()


py5.run_sketch()
