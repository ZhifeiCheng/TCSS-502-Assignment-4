from DrawingProgram import DrawingProgram
from ShapeFactory import ShapeFactory


class DrawingProgramMain:
    @staticmethod
    def main():
        drawing_program = DrawingProgram()
        circle_1 = ShapeFactory.create_shape("Circle", 20)
        circle_2 = ShapeFactory.create_shape("Circle", 60)
        circle_3 = ShapeFactory.create_shape("Circle", 80)
        rectangle_1 = ShapeFactory.create_shape("Rectangle", 80, 120)
        square_1 = ShapeFactory.create_shape("Square", 100)
        square_2 = ShapeFactory.create_shape("Square", 100)
        triangle_1 = ShapeFactory.create_shape("Triangle", 150, 200, 250)
        triangle_2 = ShapeFactory.create_shape("Triangle", 100, 150, 200)
        drawing_program.add_shape(square_1)
        drawing_program.add_shape(rectangle_1)
        drawing_program.add_shape(rectangle_1)
        drawing_program.add_shape(rectangle_1)
        drawing_program.add_shape(rectangle_1)
        drawing_program.add_shape(circle_1)
        drawing_program.add_shape(square_2)
        drawing_program.add_shape(circle_2)
        drawing_program.add_shape(circle_3)
        drawing_program.add_shape(triangle_1)
        drawing_program.add_shape(triangle_2)
        drawing_program.remove_shape(square_2)
        drawing_program.sort_shape()
        drawing_program.print_shape(circle_2)
        drawing_program.get_shape(2)
        drawing_program.set_shape(4, square_2)
        drawing_program.print_shape(circle_2)
        for shape in drawing_program:
            shape.draw()
            shape.draw_graphic()


if __name__ == "__main__":
    DrawingProgramMain.main()