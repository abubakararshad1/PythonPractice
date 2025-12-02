class Employee:
    def __init__(self, empid, empname, empsalary):
        self.empid = empid
        self.empname = empname
        self.empsalary = empsalary

    def display(self):
        print("Employee ID:", self.empid)
        print("Employee Name:", self.empname)
        print("Employee Salary:", self.empsalary)

    def printdata(self):
        print("Emp ID:", self.empid)
        print("Emp Name:", self.empname)


# Create first object
emp1 = Employee(1, "Abubakar", 10000)
emp1.display()

# Create second object
emp2 = Employee(2, "Raza", 15000)
emp2.printdata()
