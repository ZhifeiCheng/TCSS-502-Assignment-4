from ShapeFactory import ShapeFactory
from DrawingProgram import DrawingProgram
from DrawingProgramIterator import DrawingProgramIterator
from Shape import Shape


class DrawingProgramMain:
    drawing_program = DrawingProgram()

    shape_factory = ShapeFactory()

    print(" ")
    print(" ------------Creating Shapes------------")
    drawing_program.add_shape(shape_factory.create_shape('circle', 1.0))
    drawing_program.add_shape(shape_factory.create_shape('circle', 1.0))
    drawing_program.add_shape(shape_factory.create_shape('square', 3.0))
    drawing_program.add_shape(shape_factory.create_shape('rectangle', 1.0, 2.0))
    drawing_program.add_shape(shape_factory.create_shape('triangle', 3.0, 4.0, 5.0))
    drawing_program.add_shape(shape_factory.create_shape('circle', 3.0))
    drawing_program.add_shape(shape_factory.create_shape('square', 5.0))
    drawing_program.add_shape(shape_factory.create_shape('rectangle', 5.0, 2.0))
    drawing_program.add_shape(shape_factory.create_shape('triangle', 5.0, 12.0, 13.0))
    drawing_program.add_shape(shape_factory.create_shape('triangle', 12.0, 16.0, 20.0))

    iterable = DrawingProgramIterator(drawing_program.shapes)
    for shape in iterable:
        Shape.draw(shape)

    print("  ")
    print("----------------Removing Shapes-----------")
    """ The get_shape below passes an 'index' based on the above create shapes to get the shape.
    We can pick a different shape by manually changing the index below. 
    The may have to be improved"""
    shape = drawing_program.get_shape(4)
    drawing_program.remove_shape(shape)
    print('REMOVED SHAPE:', shape.shape_name)
    print(' ')
    iterable1 = DrawingProgramIterator(drawing_program.shapes)
    for shape1 in iterable1:
        Shape.draw(shape1)

    print(" ")
    print("-------Sorting Shapes (based on shape name  and then area-------")
    iterable2 = DrawingProgramIterator(drawing_program.sort_shapes())
    for shape2 in iterable2:
        Shape.draw(shape2)
    print(" ")
