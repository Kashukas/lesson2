def user_input():
    try:
        return int(input('Choose option: '))
    except ValueError:
        print('Enter integer from 1 to 6.')
    pass

user_data = {
            'Mike': {
                'weight': '76',
                'height': '1.80',
                'gender': 'm',
                'BMI': 23.45,
                'BMI scale': '10**********|**********50'
            },
            'Nick': {
                'weight': 80,
                'height': 1.82,
                'gender': 'm',
                'BMI': 24.15,
                'BMI scale': '10**********|**********50'
            }
            }

def print_key():
    for key in user_data.keys():
        print(key)

def users_list():
    print('Users list: ')
    print_key()

def user_info():
    print('Saved users: ')
    print_key()
    name = input('Enter user name: ')
    print(name + ' info:')
    print(user_data.get(name, 'User not found'))

def user_change():
    print('User change')

def user_del():
    print('Saved users: ')
    print_key()
    del_name = input('Enter the name of user you want to delete: ')
    del(user_data[del_name])
    print('User ' + del_name + ' deleted.')

def user_add():
    name = input('Enter your name: ') # Get name from user
    gender = input('Enter your gender (m/f): ')
    weight = input('Enter your weight in kilograms (for example, 86): ')  # Get weight from user.
    # Handling ValueError from weight.
    try:
        weight = float(weight)  # Convert weight to a floating point number.
        # Check if weight is more than 0.
        if weight > 0:
            height = input('Enter your height in meters (for example, 1.82): ')  # Get height from user.
            # Handling ValueError from height.
            try:
                height = float(height)  # Convert height to a floating point number.
                if height > 0:  # Check if height is more than 0.
                    bmi = weight / height ** 2  # Calculate bmi.
                    print('Your BMI: ' + str(round(bmi)) + '\n')
                    # Create scale from 10 to 50 with step 1.
                    if bmi > 10 and bmi < 50:  # Check if bmi value get in scale.
                        left_scale = round(bmi) - 11  # Left part of scale.
                        right_scale = 49 - round(bmi)  # Right part of scale.
                        scale = '10' + '-'*left_scale + '|' + '-'*right_scale + '50'
                        print(scale)  # Print scale.
                        user_data[name] = {
                            'weight': weight,
                            'height': height,
                            'gender': gender,
                            'BMI': bmi,
                            'BMI scale': scale
                            }
                    else:
                        print('The value of your BMI is not in the period 10-50.')  # Message if bmi value is out of scale.
                    print('Your gender: ' + gender)
                    if bmi < 18.5:
                        print('Your weight is lower than normal.')
                    if bmi >= 18.5 and bmi < 25:
                        print('You are of normal weight.')
                    if bmi >= 25:
                        print('You are overweight.')
                    print('User ' + name + ' added')
                else:
                    print('The height should be more than 0. Exit.')
            except ValueError:
                print('The height is incorrect. Exit.')
        else:
            print('The weight should be more than 0. Exit.')
    except ValueError:
        print('The weight is incorrect. Exit.')

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