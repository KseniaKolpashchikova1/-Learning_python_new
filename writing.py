from asyncore import write
from phonebook_model import get_abonents as ga

info = ga()

def writing_csv():
    file = 'phone_book.csv'
    with open(file, 'a', encoding = 'utf-8') as data:
        data.write(f'; \n{info[0]}; \n\n{info[1]}; \n\n{info[2]}; \n\n{info[3]}')

def writing_txt():
    file = 'phone_book.txt'
    with open(file, 'a', encoding = 'utf-8') as data:
       data.write(f'\nФамилия: {info[0]} \n\nИмя:{info[1]} \n\nНомер телефона: {info[2]} \n\nОписание: {info[3]}\n')
