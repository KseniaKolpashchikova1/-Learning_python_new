import BD_model
import view_person

def button_click():
    get_menu()

def get_menu():
    while True:
        print('Введите "1", чтобы создать новую запись\n'
        'Введите "2", чтобы посмотреть весь список сотрудников\n'
        # 'Введите "3", чтобы найти сотрудника по фамилии\n'
        # 'Введите "4", чтобы удалить запись\n'
        'Введите "x", чтобы закрыть программу\n')
        user_number = input('Введите одну из указанных команд: ')
        if user_number == '1':
            add_person = view_person.get_info()
            company_as_dict.append(add_person)
            BD_model.save_json(add_person)
        elif user_number == '2':
            BD_model.read_json(company_as_dict)
        # elif user_number == '3':
        #     find_surname_per()
        # elif user_number == '4':
        #     BD_model.remove_person(company_as_dict)
        elif user_number == 'x':
            break
        else:
            print('Вы указали неккоректную команду. Выберете одно из значений меню!!!')

company_as_dict = [{'Surname': 'surname', 'Name': 'name', 'Departament': 'departament', 'Position': 'position', 'Salary': 100}]
