class Employee:
    def __init__(self, name, id , position, salary):
        self.name = name
        self.id = id
        self.position = position
        self.salary = salary

    def displayDetails(self):
        print(f"Employee Name : {self.name} : Employee ID : {self.id} : Employee Position : {self.position} : Employee salary :{self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"The New Salary of {self.name} is {self.salary}.")
        
e1 = Employee("aditya", 101, "HR", 1000000000000)
e1.displayDetails()
e1.update_salary(10)
e1.displayDetails()
