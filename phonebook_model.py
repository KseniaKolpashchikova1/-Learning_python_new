def get_abonents():
    info_ab = []
    surname = input('Введите, пожалуйста, фамилию: ')
    info_ab.append(surname)
    name = input('Введите, пожалуйста, имя: ')
    info_ab.append(name)
    phone_number = ''
    valid = False
    while not valid:
        try:
            phone_number = input('Введите, пожалуйста, номер телефона: ')
            if len(phone_number) !=11:
                print('Номер телефона должен состоять из 11 цифр. Введите корректное значение!')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять из цифр!')
            continue
    info_ab.append(phone_number)
    description = input('Введите, пожалуйста, описание: ')
    info_ab.append(description)
    return info_ab
    
