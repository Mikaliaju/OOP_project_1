from classes import employee

department = employee()


while(True):
    print('----------------------------------------------------------------------------------')
    x = input('Write 1 to add, 2 to update, 3 to delete, 4 to search, 5 to list all employees, or 6 to exit: ')
    if x == '1':
        a, b, c, d, e = input('Write employee data in (name, id, salary, position, email): ').split()
        department.add_employee(a, b, c, str(d), str(e))
    elif x == '2':
        a = input('Write id of the employee: ')
        b = input('Write updated data of the employee: ')
        department.update_employee(a,b)
    elif x == '3':
        c = input('Write id of the employee to delete: ')
        department.delete_employee(c)
    elif x == '4':
        d = input('Write id of the employee to search: ')
        department.serach_employee(d)
    elif x == '5':
        print('All the employees data: ')
        department.list_employees()
    elif x == '6':
        department.clear_df()
        print('Thank you!')
        break
