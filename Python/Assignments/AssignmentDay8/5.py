import pandas as pd

employee_file = '/Users/vedant/Desktop/Atgeir/HandsOn/Python/Assignments/AssignmentDay8/employee_data/employees.csv'
department_file = '/Users/vedant/Desktop/Atgeir/HandsOn/Python/Assignments/AssignmentDay8/employee_data/departments.csv'
location_file = '/Users/vedant/Desktop/Atgeir/HandsOn/Python/Assignments/AssignmentDay8/employee_data/locations.csv'

def get_dataset_sizes(employee_path, department_path, location_path):
    df_employee = pd.read_csv(employee_path)
    df_department = pd.read_csv(department_path)
    df_location = pd.read_csv(location_path)

    size_employee = df_employee.shape
    size_department = df_department.shape
    size_location = df_location.shape

    dataset_sizes = {
        'employee': size_employee,
        'department': size_department,
        'location': size_location
    }

    return dataset_sizes

dataset_sizes = get_dataset_sizes(employee_file, department_file, location_file)

print("Dataset Sizes:")
print(dataset_sizes)
