import pandas as pd
import matplotlib.pyplot as plt

# File paths to your CSV data

employees_df = pd.read_csv('/Users/vedant/Desktop/Atgeir/HandsOn/Python/Assignments/AssignmentDay8/employee_data/employees.csv')
departments_df = pd.read_csv('/Users/vedant/Desktop/Atgeir/HandsOn/Python/Assignments/AssignmentDay8/employee_data/departments.csv')


merged_df = pd.merge(employees_df, departments_df, on='department_id', how='left')

department_counts = merged_df['department_name'].value_counts()

department_percentages = department_counts / department_counts.sum() * 100

plt.figure(figsize=(12, 8))
plt.pie(department_percentages, labels=department_percentages.index, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Percentage of Employees in Each Department')
plt.show()