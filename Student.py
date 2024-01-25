class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def studentDetails(self):
        print(f"Students name  : {self.name} , Students Age : {self.age} , Students grade : {self.grade}.")

    def calculate_grade(self, percentage):
        if percentage > 90:
            self.grade = "A+"
        elif percentage >  70:
            self.grade = "B"
        elif percentage >  60:
            self.grade = "C"
        elif percentage >  40:
            self.grade = "D"
        else:
            self.grade = "F"

s1 = Student("Aditya varshney", 18, "NA")
s1.calculate_grade(100)
s1.studentDetails()
