import pandas as pd
class employee:
    def __init__(self):
        self.names = []
        self.ids = []
        self.salaries = []
        self.positions = []
        self.emails = []
        self.data = {'names': self.names
                     , 'ids': self.ids
                     , 'salaries': self.salaries
                     , 'positions': self.positions
                     , 'emails': self.emails }
    def add_employee(self, name, id, salary, position, email):
        self.names.append(name)
        self.ids.append(id)
        self.salaries.append(salary)
        self.positions.append(str(position))
        self.emails.append(str(email))
        df = pd.DataFrame(self.data)
        df.to_csv('employees.csv')
    def update_employee(self, id, *args):
        for i in self.ids:
            if i == id:
                index = self.ids.index(i)
        #print(type(args[0]))
        for i in range(0, len(args)):
            if '@' in args[i]:
                self.emails[index] = args[i]
            else:
                try:
                    self.salaries[index] = int(args[i])
                except ValueError:
                    self.positions[index] = args[i]
        df = pd.DataFrame(self.data)
        df.to_csv('employees.csv')
    def delete_employee(self, id):
        for i in self.ids:
            if i == id:
                index = self.ids.index(i)
        self.emails.pop(index)
        self.salaries.pop(index)
        self.positions.pop(index)
        self.ids.pop(index)
        self.names.pop(index)
        df = pd.DataFrame(self.data)
        df.to_csv('employees.csv')
    def serach_employee(self, id):
        flag = 0
        for i in self.ids:
            if i == id:
                index = self.ids.index(i)
                flag = 1
        if flag == 0:
            print('Employee not found')
        else:
            print('Employee found')
            print(f"id: {self.ids[index]}")
            print(f"name: {self.names[index]}")
            print(f"salary: {self.salaries[index]}")
            print(f"position: {self.positions[index]}")
            print(f"email: {self.emails[index]}")
    def list_employees(self):
        for i in range(self.ids.__len__()):
            print(self.ids[i], self.names[i], self.salaries[i], self.positions[i], self.emails[i])

    def clear_df(self):
        df = pd.DataFrame()
        df.to_csv('employees.csv')




