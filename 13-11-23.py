import py5


def setup():
    py5.size(800, 800)

    grid = py5.load_image('images/grid.png')
    py5.image(grid, 0, 0)


def draw():
    py5.fill(255, 255, 255)
    py5.stroke(15)
    py5.stroke_weight(1)

    py5.begin_shape()  # Left white circle
    py5.vertex(100, 600)
    py5.bezier_vertex(100, 545, 145, 500, 200, 500)
    py5.bezier_vertex(255, 500, 300, 545, 300, 600)
    py5.bezier_vertex(300, 655, 255, 700, 200, 700)
    py5.bezier_vertex(145, 700, 100, 655, 100, 600)
    py5.end_shape()

    py5.begin_shape()  # Right white circle
    py5.vertex(500, 600)
    py5.bezier_vertex(500, 545, 545, 500, 600, 500)
    py5.bezier_vertex(655, 500, 700, 545, 700, 600)
    py5.bezier_vertex(700, 655, 655, 700, 600, 700)
    py5.bezier_vertex(545, 700, 500, 655, 500, 600)
    py5.end_shape()

    py5.fill(15, 15, 15)
    py5.stroke(15)
    py5.stroke_weight(1)

    py5.begin_shape()  # Middle Bezier shape
    py5.vertex(400, 200)  # Starting (upper) vertex
    py5.bezier_vertex(300, 300,  # Control point for the starting vertex
                      500, 500,  # Control point for the second (lower) vertex
                      400, 600)  # Second (lower) vertex coordinates
    py5.vertex(400, 200)
    py5.bezier_vertex(500, 300,  # Control point for the starting vertex
                      300, 500,  # Control point for the second (lower) vertex
                      400, 600)  # Second (lower) vertex coordinates
    py5.end_shape(py5.CLOSE)

    py5.fill(250, 0, 0)
    py5.stroke(250, 0, 0)
    py5.stroke_weight(1)
    py5.begin_shape()  # Left love heart
    py5.vertex(200, 400)
    py5.bezier_vertex(20, 300,
                      150, 150,
                      200, 250)
    py5.vertex(200, 400)
    py5.bezier_vertex(380, 300,
                      250, 150,
                      200, 250)
    py5.end_shape(py5.CLOSE)

    py5.begin_shape()  # Right love heart
    py5.vertex(600, 400)
    py5.bezier_vertex(420, 300,
                      550, 150,
                      600, 250)
    py5.vertex(600, 400)
    py5.bezier_vertex(780, 300,
                      650, 150,
                      600, 250)
    py5.end_shape(py5.CLOSE)


py5.run_sketch()
