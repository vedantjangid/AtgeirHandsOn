import pandas as pd


file_path = '/Users/vedant/Desktop/Atgeir/HandsOn/Python/Assignments/AssignmentDay8/employee_data/employees.csv'

df = pd.read_csv(file_path)

unique_hire_dates = df['hire_date'].unique().tolist()

print("Unique hire_dates:")
print(unique_hire_dates)
