def calculate_area(shape, *args):
    if shape == 'rectangle':
        if len(args) == 2:
            width, height = args
            area = width * height
            return area
        else:
            return "Error: Rectangle area calculation requires exactly 2 dimensions (width, height)."
    
    elif shape == 'equilateral_triangle':
        if len(args) == 1:
            side_length = args[0]
            area = (side_length ** 2) * (3 ** 0.5) / 4  # Area formula for equilateral triangle
            return area
        else:
            return "Error: Equilateral triangle area calculation requires exactly 1 dimension (side length)."
    
    elif shape == 'isosceles_trapezoid':
        if len(args) == 3:
            a, b, h = args
            area = 0.5 * (a + b) * h
            return area
        else:
            return "Error: Isosceles trapezoid area calculation requires exactly 3 dimensions (a, b, height)."
    
    else:
        return "Error: Unsupported shape. Supported shapes are 'rectangle', 'equilateral_triangle', and 'isosceles_trapezoid'."
