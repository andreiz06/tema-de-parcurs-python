from employee import Employee

class Manager(Employee):
    mgrCount=0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department="F27"
        Manager.mgrCount+=1

    def display_employee(self):
        
        X=7  #Zaharia
        Y=14 #Andrei Cristian -> pentru a stii cate instante de manageri creăm(Y/3=3 manageri)
        if X%3==0:
            print(f"Name: {self.name}")
        elif X%3==1:
            print(f"Salary: {self.salary}")
        elif X%3==2:
            print(f"Department: {self.department}")

if __name__=="__main__":

    managers=[]
    managers.append(Manager("Bombonel", 7000, "Sales"))
    managers.append(Manager("Luis", 8000, "Marketing"))
    managers.append(Manager("Mihaita", 9000, "Finance"))

    print("Managers:")
    for mgr in managers:
        mgr.display_employee()

    employees=[]
    employees.append(Employee("Mario", 3500))
    employees.append(Employee("Luigi", 4000))

    print("\nEmployees:")
    for emp in employees:
        emp.display_employee()

    print(f"\nNumber of employees: {Employee.empCount}")
    print(f"Number of managers: {Manager.mgrCount}")