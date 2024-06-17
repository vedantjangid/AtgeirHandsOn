import pandas as pd 

df = pd.read_csv('/Users/vedant/Desktop/Atgeir/HandsOn/Python/Assignments/AssignmentDay8/employee_data/departments.csv')


dtoshow = df[['department_id', 'department_name']]
print(dtoshow)