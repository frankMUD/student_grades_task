# Create  Student class
class Student():
    # Constructor method
    def __init__(self, age, name, gender, grades):
        self.age = age
        self.name = name
        self.gender = gender
        self.grades = grades

    # Method to calculate average grade
    def compute_average(self):
        average = sum(self.grades) / len(self.grades)
        print("The average for student " + self.name + " is " + str(average))

    # Function to find highest grade for the student
    def find_highest_grade(self):
        highest_grade = max(self.grades)
        print("The highest grade for student " + self.name + " is " + str(highest_grade))


# Create Student objects
philani = Student(20, "Philani Sithole", "Male", [64, 65])
sarah = Student(19, "Sarah Jones", "Female", [82, 58])

# Method calls
sarah.compute_average()
sarah.find_highest_grade()
