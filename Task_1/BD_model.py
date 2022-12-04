import os.path
import json
from pprint import pprint

company_as_dict = [{'Surname': 'surname', 'Name': 'name', 'Departament': 'departament', 'Position': 'position', 'Salary': 100}]
file_name = './Seminar_8'

def read_json(company_as_dict):
    with open(file_name,'r', encoding = 'utf-8') as f:
            company_as_dict = json.load(f)
    pprint(company_as_dict)

def save_json(company_as_dict):
    with open(file_name,'w') as f:
        json.dump(company_as_dict, f)
        print(f'Файл {file_name} сохранен')

def add_new_person(company_as_dict):
    with open(file_name,'r') as f:
        data = json.dump(company_as_dict, f)
    n_data = {'Surname': 'surname', 'Name': 'name', 'Departament': 'departament', 'Position': 'position', 'Salary': 100}
    data[file_name].append(n_data)

# def remove_person(company_as_dict):
#     with open(file_name,'a') as f:
#         query = str(input('Введите фамилию сотрудника, запись которого нужно удалить: '))
#         for k in f:
#             if k == query:
#                 del f[k] 
#                 print('Запись по данному сотруднику удалена')             
#             else:
#                 print('Сведения о данном сотруднике отсутствуют в базе данных!')

file_name = './Seminar_8'


