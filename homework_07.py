def user_input():
    try:
        return int(input('Choose option: '))
    except ValueError:
        print('Enter integer from 1 to 6.')
    pass

user_data = {}

def users_list():
    print('Users list')

def user_info():
    print('User info')

def user_change():
    print('User change')

def user_del():
    print('Delete user')

def user_add():
    name = input('Enter your name: ') # Get name from user
    weight = input('Введите ваш вес в килограммах (например, 86): ')  # Get weight from user.
    # Handling ValueError from weight.
    try:
        weight = float(weight)  # Convert weight to a floating point number.
        # Check if weight is more than 0.
        if weight > 0:
            height = input('Введите ваш рост в метрах (например, 1.82): ')  # Get height from user.
            gender = input('Введите ваш пол (m/f): ')
            # Handling ValueError from height.
            try:
                height = float(height)  # Convert height to a floating point number.
                if height > 0:  # Check if height is more than 0.
                    bmi = weight / height ** 2  # Calculate bmi.
                    print('Ваш индекс массы тела: ' + str(round(bmi)) + '\n')
                    # Create scale from 10 to 50 with step 1.
                    if bmi > 10 and bmi < 50:  # Check if bmi value get in scale.
                        left_scale = round(bmi) - 11  # Left part of scale.
                        right_scale = 49 - round(bmi)  # Right part of scale.
                        print('10' + '-'*left_scale + '|' + '-'*right_scale + '50')  # Print scale.
                    else:
                        print('Значение вашего ИМТ не попадает в шкалу от 10 до 50.')  # Message if bmi value is out of scale.
                    print('Ваш пол: ' + gender)
                    if bmi < 18.5:
                        print('Ваш вес ниже нормального.')
                    if bmi >= 18.5 and bmi < 25:
                        print('У вас нормальный вес.')
                    if bmi >= 25:
                        print('У вас избыточный вес.')
                else:
                    print('Рост должен быть больше 0. Работа калькулятора завершена.')
            except ValueError:
                print('Некорректно введен рост. Работа калькулятора завершена.')
        else:
            print('Вес должен быть больше 0. Работа калькулятора завершена.')
    except ValueError:
        print('Некорректно введен вес. Работа калькулятора завершена.')
    user_data.update(name = [height, weight, gender, bmi])
    print('User added')
    print(user_data)

def exit_pr():
    print('Turn off')
    quit()

menu_dict = {1: users_list, 2: user_info, 3: user_change, 4: user_del, 5: user_add, 6: exit_pr}

def menu():
    print('''
    BMI calculator:

    1. Users list.
    2. User info.
    3. Change user info.
    4. Delete user.
    5. Add user.
    6. Exit.
    ''')
    ui = user_input()
    while ui in [1, 2, 3, 4, 5, 6]:
        menu_dict[ui]()
        menu()
    print('Wrong option selected, try again.')
    menu()
menu()