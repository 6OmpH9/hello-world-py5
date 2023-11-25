import py5


def setup():
    py5.size(800, 800)

    grid = py5.load_image('images/grid.png')
    py5.image(grid, 0, 0)


def draw():
    py5.no_fill()
    py5.stroke_weight(3)

    py5.begin_shape()
    py5.vertex(100, 400)
    py5.vertex(400, 400)
    py5.vertex(400, 400)
    py5.vertex(100, 100)
    py5.end_shape(py5.CLOSE)

    py5.stroke('#FF99FF')  # Pink
    cp1x = 250
    cp1y = 150
    cp2x = 300
    cp2y = 350
    py5.bezier(400, 100, cp1x, cp1y, cp2x, cp2y, 100, 400)

    py5.stroke('#11CC88')  # Mint green
    # Ellipses at the control points for our Bezier curve
    py5.ellipse(cp1x, cp1y, 20, 20)
    py5.ellipse(cp2x, cp2y, 20, 20)

    py5.stroke('#FF0000')  # Red
    # Line connecting a control point to the first vertex of the curve
    py5.line(400, 100, cp1x, cp1y)
    py5.line(100, 400, cp2x, cp2y)

    py5.curve_tightness(3)
    py5.stroke('#0099FF')  # Pale blue
    # py5.line(100, 100, 400, 400)
    py5.curve(0, 0, 100, 100, 400, 400, 500, 500)

    py5.stroke('#FFFF00')  # Yellow
    py5.curve(0, 250, 100, 100, 400, 400, 500, 250)

    py5.stroke('#FF9900')  # Orange
    py5.curve(0, 250, 0, 250, 100, 100, 400, 400)  # Control point1
    py5.curve(100, 100, 400, 400, 500, 250, 500, 250)  # Control point2

    py5.stroke('#11CC88')  # Mint green
    py5.ellipse(0, 250, 20, 20)
    py5.ellipse(500, 250, 20, 20)


py5.run_sketch()
