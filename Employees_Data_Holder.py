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
        self.org=[]
    
    def save_emps(self,name,age,salary):
        emp=Employee(name,age,salary)
        self.emplst.append(emp)
        self.org.append([emp])
   

    
    def __str__(self):
        result=[]
        for lis in self.org:
            snapshot="\n".join(str(emp) for emp in lis)
            result.append(snapshot)
        return "\n".join(result)

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

        