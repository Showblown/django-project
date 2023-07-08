#What is feature selection in machine learning?
    #Sorting through the feautres and choosing the most relevant features which can make your model simpler and more efficient.
#What will happen to accuracy if you will increase the training sample?
    #an increased training sample will increase your accuracy because it has more data to learn from 
def primeornot(number):
    if number < 2:
        return False

    for x in range(2, int(number ** 0.5) + 1):
        if number % x == 0:
            return False

    return True
print(primeornot(14))
print(primeornot(7))
# Know the problem statement
# Gather the data
# use things like (df.describe(), df['Species'].value_counts(), df.mean()
#Cleaning the data (dealing with null values, converting categorical features into numerical, scaling) 
#Split the data (training and testing)
#Select the algorithm (KNeighborsClassifier)
#Train the model
#Test the model (compute accuracy)
class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade
        self.attendance = {}
        self.marks = {}

    def update_grade(self, new_grade):
        self.grade = new_grade

    def add_attendance(self, date, status):
        self.attendance[date] = status

    def update_marks(self, subject, marks_obtained):
        self.marks[subject] = marks_obtained

    def calculate_average_marks(self): 
        total_marks = sum(self.marks.values())
        average_marks = total_marks / len(self.marks)
        return average_marks
    def display_info(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Grade:", self.grade)
        print("attendance:")
        for date, status in self.attendance.items():
            print(f"{date}: {status}")
        print("Marks:")
        for subject, marks_obtained in self.marks.items():
            print(f"{subject}: {marks_obtained}")
            
student1 = Student("John Smith", 12345, "A")

student2 = Student(roll_number = 123, name="Shiz", grade="B")


student1.update_grade("B")

student1.add_attendance("2023-06-25", "Present")
student1.add_attendance("2023-06-26", "Absent")

student1.update_marks("Math", 85)
student1.update_marks("Science", 92)

average_marks = student1.calculate_average_marks()

student1.display_info()
print(f"Average Marks: {average_marks}")
