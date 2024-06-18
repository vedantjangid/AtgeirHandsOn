import pandas as pd

employees_df = pd.read_csv('/Users/vedant/Desktop/Atgeir/HandsOn/Python/Assignments/AssignmentDay8/employee_data/employees.csv')
jobs_df = pd.read_csv('/Users/vedant/Desktop/Atgeir/HandsOn/Python/Assignments/AssignmentDay8/employee_data/jobs.csv')
departments_df = pd.read_csv('/Users/vedant/Desktop/Atgeir/HandsOn/Python/Assignments/AssignmentDay8/employee_data/departments.csv')

null_values_employees = employees_df.isnull().sum()
null_values_jobs = jobs_df.isnull().sum()
null_values_departments = departments_df.isnull().sum()

print(null_values_employees)
print(null_values_jobs)
print(null_values_departments)

employee_details = employees_df.merge(jobs_df, on='job_id').merge(departments_df, on='department_id')

employee_details = employee_details[['employee_id', 'first_name', 'last_name', 'email', 'hire_date', 'job_title', 'department_name']]

print(employee_details)