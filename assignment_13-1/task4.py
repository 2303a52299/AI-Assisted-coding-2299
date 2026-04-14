'''(Refactoring – Converting Procedural Code to Functions)
• Task:refactor procedural input–processing logic into functions.
Instructions:
o Identify input, processing, and output sections.
o Convert each into a separate function.
o Improve code readability without changing behavior.
• Sample Legacy Code:
num = int(input("Enter number: "))
square = num * num
print("Square:", square)
• Expected Output:
o Modular code using functions like get_input(), calculate_square(), and display_result().
'''

def get_input():
    """
    Prompt the user to enter a number and return it as an integer
     Returns:
    int: The number entered by the user.
    """
    return int(input("Enter number: "))
def calculate_square(num):
    """Calculate the square of a given number.
    Parameters:
    num (int): The number to be squared.    
    Returns:
    int: The square of the input number.
    """
    return num * num
def display_result(square):
    """
    Display the result of the square calculation.
    Parameters:
    square (int): The squared value to be displayed.
    """
    print("Square:", square)

num = get_input()
square = calculate_square(num)
display_result(square)
    
