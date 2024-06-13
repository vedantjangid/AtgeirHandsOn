# Atgeir/Data/Learner.py

def write_data(file_path, data):
    """
    Writes data to a file.
    
    Args:
        file_path (str): The path to the file where data will be written.
        data (str): The data to write to the file.
    """
    with open(file_path, 'w') as file:
        file.write(data)
    print(f"Data written to {file_path}")

def read_data(file_path):
    """
    Reads data from a file.
    
    Args:
        file_path (str): The path to the file to read data from.
        
    Returns:
        str: The content of the file.
    """
    with open(file_path, 'r') as file:
        data = file.read()
    print(f"Data read from {file_path}")
    return data
