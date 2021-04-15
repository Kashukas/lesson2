a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
# 1 task
out1 = a and b and c and "Нет нулевых значений!!!"
print('1. ' + str(out1))
# 2 task
out2 = a or b or c or "Введены все нули!"
print('2. ' + str(out2))
# 3 task
if a > (b + c):
    print('3. ' + str(a-b-c))
# 4 task
if a < (b + c):
    print('4. ' + str(b + c - a))
# 5 task
if a > 50 and (b > a or c > a):
    print("5. Вася")
# 6 task
if a > 5 or (b == 7 and c == 7):
    print('6. Петя')