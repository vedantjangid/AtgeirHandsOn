import pandas as pd
import matplotlib.pyplot as plt


employees_df = pd.read_csv('/Users/vedant/Desktop/Atgeir/HandsOn/Python/Assignments/AssignmentDay8/employee_data/employees.csv')
departments_df = pd.read_csv('/Users/vedant/Desktop/Atgeir/HandsOn/Python/Assignments/AssignmentDay8/employee_data/departments.csv')
locations_df=pd.read_csv('/Users/vedant/Desktop/Atgeir/HandsOn/Python/Assignments/AssignmentDay8/employee_data/locations.csv')


# Merge employees_df with departments_df on 'department_id'
merged_df = pd.merge(employees_df, departments_df, on='department_id', how='left')

# Merge the result with locations_df on 'location_id'
merged_df = pd.merge(merged_df, locations_df, left_on='location_id', right_on='location_id', how='left')


# Count the number of employees per country
country_counts = merged_df['country_id'].value_counts()

# Create a bar chart
plt.figure(figsize=(12, 6))
country_counts.plot(kind='bar')
plt.xlabel('Country')
plt.ylabel('Number of Employees')
plt.title('Number of Employees per Country')
plt.show()