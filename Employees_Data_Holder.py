class Employee:
    
    def __init__(self,Name=None,Age=None,Salary=None):
        self.name=Name
        self.age=Age
        self.Salary=Salary
    def __str__(self):
        return f"Name: {self.name} || Age: {self.age} || Salary: {self.Salary}"
    

class EmployeesManager:
   
    def __init__(self):
        self.emplst=[]
    
    def save_emps(self,name,age,salary):
        emp=Employee(name,age,salary)
        self.emplst.append(emp)
    
    def find_employee_by_name(self,name):
        search=[(the_name.name,the_name.age,the_name.Salary) for the_name in self.emplst if the_name.name==name]
        return search
   
    def delete_emp(self,sage,lage):
        self.emplst=[snapshot for snapshot in self.emplst if snapshot.age not in range(sage,lage+1)]
    
    def update_salary_by_name(self,name,salary):
        for item in self.emplst:
            if name==item.name:
                item.Salary=salary
    
    def __str__(self):
        result=[]
        for snapshot in self.emplst:
            result.append(str(snapshot))
        return "\n".join(result)

emp=EmployeesManager()
while True:
    message=["Program Options:",
      "(1) Add Employee",
      "(2) Update Salary Employee",
      "(3) Update Employee by age range",
      "(4) Show Employee Data Base",
      "(5) find Employee by name",
      "(6) End the Program"]
    print("\n".join(message))
    choosed=int(input())
    if choosed in range(1,6+1):
        if choosed==1:
            print(20*"#")
            emp.save_emps(input("Enter Employee Name: "),int(input("Enter Employee Age: ")),int(input("Enter Employee Salary: ")))
            print(20*"#")
            print("-------------------------------")
            print("|Employee was Added Successfully|")
            print("-------------------------------\n")

        elif choosed==2:
            print(20*"#")
            emp.update_salary_by_name(input("Enter the Name: "),int(input("Enter the New Salary: ")))
            print(20*"#")
            print("-----------------------------")
            print("|Salary Changed Successfuly|")
            print("-----------------------------\n")

        elif choosed==3:
            emp.delete_emp(int(input("Enter the first of the range: ")),int(input("Enter the last of the range: ")))
        
        elif choosed==4:
            print(str(emp))
        elif choosed==5:
            print(20*"#")
            print(str(emp.find_employee_by_name(input("Enter Name: "))))
            print(20*"#")
        elif choosed==6:
            break
    else:
        print("-------------------------------")
        print("Invalid!, Choose between 1 to 6")
        print("-------------------------------\n")

        