class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
    
    def display(self):
        print("Attributes and their values:")
        for attr, value in vars(self).items():
            print(f"{attr}: {value}")

student = Student(1, "John Doe")

student.display()

student.student_class = "Grade 10"

print("\nAfter adding student_class:")
student.display()

del student.student_name

print("\nAfter removing student_name:")
student.display()
