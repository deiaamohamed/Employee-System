class Employee:
    
    def __init__(self,Name=None,Age=None,Salary=None):
        self.name=Name
        self.age=Age
        self.Salary=Salary
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.Salary}"
class EmployeesManager:
   
    def __init__(self):
        self.emplst=[]
    
    def save_emps(self,name,age,salary):
        emp=Employee(name,age,salary)
        self.emplst.append(emp)

    
    def __str__(self):
        return "\n".join(str(emp) for emp in self.emplst)

emp=EmployeesManager()
while True:
    print("Program Options:\n"
      "(1) Add Employee\n"
      "(2) Delete Employee(under test request)\n"
      "(3) Update Employee by age range(under test request)\n"
      "(4) Show Employee Data Base\n"
      "(5) End the Program\n\n")
    choosed=int(input())
    if choosed in range(1,6):
        if choosed==1:
            emp.save_emps(input("Enter Employee Name: "),input("Enter Employee Age: "),input("Enter Employee Salary: "))
        elif choosed in range(2,4):
            print("out of services due to mantinance")
        elif choosed==4:
            print(str(emp))
        elif choosed==5:
            break

        