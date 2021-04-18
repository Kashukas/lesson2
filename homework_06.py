login = input('Введите ваш логин: ')
def check_login(func):  # Decorator definition.
    def wr_check_login(x):
        if x == 'admin':
            return func()
        print('Доступ запрещен')
    return wr_check_login
@check_login  # Decorator call.
def sum():  # Main function definition.
    print('Сумма на счете: 5000$')
sum(login)  # Main function call.