'''refactor a given Python script that contains multiple repeated code blocks.
identify duplicate logic and replace it with functions or classes.
o	Ensure the refactored code maintains the same output.
o	Add docstrings to all functions.
# Legacy script with repeated logic
print("Area of Rectangle:", 5 * 10)
print("Perimeter of Rectangle:", 2 * (5 + 10))

print("Area of Rectangle:", 7 * 12)
print("Perimeter of Rectangle:", 2 * (7 + 12))

print("Area of Rectangle:", 10 * 15)
print("Perimeter of Rectangle:", 2 * (10 + 15))
'''
# Refactored script with functions to eliminate duplicate code
def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    
    Returns:
    float: The area of the rectangle.
    """
    return length * width
def calculate_rectangle_perimeter(length, width):
    """
    Calculate the perimeter of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    
    Returns:
    float: The perimeter of the rectangle.
    """
    return 2 * (length + width)
# List of rectangle dimensions
rectangles = [(5, 10), (7, 12), (10,15)]
# Calculate and print area and perimeter for each rectangle
for length, width in rectangles:
    area = calculate_rectangle_area(length, width)
    perimeter = calculate_rectangle_perimeter(length, width)
    print(f"Area of Rectangle: {area}")
    print(f"Perimeter of Rectangle: {perimeter}")


