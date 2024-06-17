import pandas as pd

file_path = '/Users/vedant/Desktop/Atgeir/HandsOn/Python/Assignments/AssignmentDay8/employee_data/employees.csv'

df = pd.read_csv(file_path)

selected_columns = ['employee_id', 'first_name', 'last_name', 'hire_date']
df_selected = df[selected_columns]

print(df_selected)
