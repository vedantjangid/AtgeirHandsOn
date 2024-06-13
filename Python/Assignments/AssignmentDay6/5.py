class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def get_String(self):
        self.input_string = input("Enter a string: ")

    def print_String(self):
        print("String in upper case:", self.input_string.upper())

manipulator = StringManipulator()
manipulator.get_String()
manipulator.print_String()
