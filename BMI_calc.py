weight = input('Введите ваш вес в килограммах (например, 86): ')  # Get weight from user.
# Handling ValueError from weight.
try:
    weight = float(weight)  # Convert weight to a floating point number.
    # Check if weight is more than 0.
    if weight > 0:
        height = input('Введите ваш рост в метрах (например, 1.82): ')  # Get height from user.
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
            else:
                print('Рост должен быть больше 0. Работа калькулятора завершена.')
        except ValueError:
            print('Некорректно введен рост. Работа калькулятора завершена.')
    else:
        print('Вес должен быть больше 0. Работа калькулятора завершена.')
except ValueError:
    print('Некорректно введен вес. Работа калькулятора завершена.')