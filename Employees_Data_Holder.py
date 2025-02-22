class Employee:
    
    def __init__(self,Name=None,Age=None,Salary=None):
        self.name=Name
        self.age=Age
        self.Salary=Salary
    def __str__(self):
        return f"Name: {self.name}|| Age: {self.age}|| Salary: {self.Salary}"
class EmployeesManager:
   
    def __init__(self):
        self.emplst=[]
    
    def save_emps(self,name,age,salary):
        emp=Employee(name,age,salary)
        self.emplst.append(emp)
   
    def delete_emp(self,sage,lage):
        self.emplst=[snapshot for snapshot in self.emplst if snapshot[0].age not in range(sage,lage)]
                
    
    def __str__(self):
        result=[]
        for snapshot in self.emplst:
            result.append(str(snapshot))
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
            emp.save_emps(input("Enter Employee Name: "),int(input("Enter Employee Age: ")),int(input("Enter Employee Salary: ")))
        
        elif choosed==3:
            emp.delete_emp(int(input("Enter the first of the range: ")),int(input("Enter the last of the range: ")))
            
        elif choosed==4:
            print(str(emp))
        elif choosed==5:
            break

        