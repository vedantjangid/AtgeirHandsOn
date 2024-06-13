# test_script.py

from Atgeir.Data import Learner

# Example data to write
data_to_write = "This is an example of data being written to a file."

# Path to the file
file_path = "example_file.txt"

# Write data to file
Learner.write_data(file_path, data_to_write)

# Read data from file
read_data = Learner.read_data(file_path)

# Print the read data
print("Read Data:")
print(read_data)
