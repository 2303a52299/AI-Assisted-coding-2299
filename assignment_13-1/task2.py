"""to refactor a legacy script where multiple calculations are embedded directly inside the main code block.
•	Instructions:
o	Identify repeated or related logic and extract it into reusable functions.
o	Ensure the refactored code is modular, easy to read, and documented with docstrings.
# Legacy script with inline repeated logic
price = 250
tax = price * 0.18
total = price + tax
print("Total Price:", total)

price = 500
tax = price * 0.18
total = price + tax
print("Total Price:", total)


"""
# Refactored script with functions to eliminate inline repeated logic
def calculate_total_price(price):
    """
    Calculate the total price including tax.
    
    Parameters:
    price (float): The base price of the item.
    
    Returns:
    float: The total price after adding tax.
    """
    tax = price * 0.18
    total = price + tax
    return total
# List of prices to calculate total for
prices = [250, 500]

# Calculate and print total price for each item
for price in prices:
    total_price = calculate_total_price(price)
    print(f"Total Price: {total_price}")






                                