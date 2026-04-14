'''
Task 5 (Refactoring Procedural Code into OOP Design)
• Task:refactor procedural code into a class-based design.
Focus Areas:
o Object-Oriented principles
o Encapsulation
Legacy Code:
salary = 50000
tax = salary * 0.2
net = salary - tax
print(net)

'''
#refactored code using a class-based design
class SalaryCalculator:
    """
    A class to calculate the net salary after tax deduction.
    
    This class encapsulates the logic for calculating the net salary based on a given gross salary and a fixed tax rate.
    """
    
    def __init__(self, salary):
        """
        Initialize the SalaryCalculator with the gross salary.
        
        Parameters:
        salary (float): The gross salary before tax deduction.
        """
        self.salary = salary
        self.tax_rate = 0.2  # Fixed tax rate of 20%
    
    def calculate_net_salary(self):
        """
        Calculate the net salary after deducting tax from the gross salary.
        
        Returns:
        float: The net salary after tax deduction.
        """
        tax = self.salary * self.tax_rate
        net_salary = self.salary - tax
        return net_salary
# Example usage
if __name__ == "__main__":
    gross_salary = 50000
    salary_calculator = SalaryCalculator(gross_salary)
    net_salary = salary_calculator.calculate_net_salary()
    print(net_salary)
