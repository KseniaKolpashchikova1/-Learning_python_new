import BD_model

def get_info():
    per_surname = input('Введите фамилию: ')
    per_name = input('Введите имя: ')
    per_department = input('Введите наименование отдела: ')
    per_position = input('Введите должность: ')
    per_salary = int(input('Введите зарплату: '))
    add_person = {"surname":per_surname, "name": per_name, "departament":per_department, 
                "position": per_position, "salary": per_salary}
    return(add_person)