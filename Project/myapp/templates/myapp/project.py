#Feature selection in machine learning is selecting the functions that you want by making them higher

#If you increase the training sample then the ai has more input data, so more accurate results

# def function():
#     number = input("Enter a number")
#     if number == 1:
#         print(number, "is not a prime number")
#     elif number > 1:
#         for x in range(2,number):
#             if (number % x) == 0:
#                 print(number,"is not a prime number")
#                 print(i,"times",number//i,"is",number)
#                 break


#the steps of machine learning is gathering a dataset, setting up the notebook, getting everything imported, and then coding the splitting the input from the output, selecting the model, training it, testing it, running it, test the accuracy, exporting it and using it for whatever program you want



class student:
    def __init__(self, name, roll_number, grade, attendance, marks):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade
        attendance = {}
        self.attendance = attendance
        marks = {}
        self.marks = marks

    
    def update_grade(self, new_grade):
        self.grade = new_grade
        print(new_grade)

    def add_attendance(self, date, status, attendance):
        self.attendance = attendance
        attendance = {}
        self.date = date
        self.status = status
        attendance.append({date:status})
        print(attendance)


    def update_marks(self, subject, marks_obtained):
        self.marks = marks
        marks = {}
        self.subject = subject
        self.marks_obtained = marks_obtained
        marks.append({subject:marks_obtained})

        print("This student got a " + marks_obtained + " in " + subject)

    def calculate_average_marks(self, marks_list):
        self.marks_list = marks_list
        print(sum(marks_list)/len(marks_list))


    def display_info(self, name, roll_number, grade, attendance, marks):
        print(name, roll_number, grade, attendance, marks)

	# creat a student object
student1 = Student("John Smith", 12345, "A")
	
	# Update the student's grade
student1.update_grade("B")
	
	# add attndance records
student1.add_attendance("2023-06-25", "Present")
student1.add_attendance("2023-06-26", "Absent")
	
	# update marks
student1.update_marks("Math", 85)
student1.update_marks("Science", 92)
	
	# calculate average marks
	average_marks = student1.calculate_average_marks()
	
	# display student information
	student1.display_info()
	print(f"Average Marks: {average_marks}")

#how do you read a csv file in python
#import pandas as pd
#df = pd.read_csv("blah.csv")

#What will df.tail
#It prints the last 5 rows

