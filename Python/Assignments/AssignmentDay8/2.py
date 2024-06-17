import pandas as pd

file_path = '/Users/vedant/Desktop/Atgeir/HandsOn/Python/Assignments/AssignmentDay8/employee_data/countries.csv'

df = pd.read_csv(file_path)

print("DataFrame head:")
print(df.head())

object_columns = df.select_dtypes(include=['object']).columns

print("\nObject type columns:")
print(object_columns)
