def calculate_gross_salary(basic_salary):
    """
    Calculate the gross salary of Ramesh based on his basic salary,
    dearness allowance (DA), and house rent allowance (HRA).
    
    Parameters:
        basic_salary (float): The basic salary of Ramesh.
        
    Returns:
        float: The gross salary of Ramesh.
    """
    da = 0.4 * basic_salary
    
    hra = 0.2 * basic_salary
    
    gross_salary = basic_salary + da + hra
    return gross_salary

basic_salary = 50000

gross_salary = calculate_gross_salary(basic_salary)

# Print the result
print("Ramesh's gross salary is:", gross_salary)
