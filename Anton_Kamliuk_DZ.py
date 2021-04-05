text = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"
print('1. Количество символов - ' + str(len(text))) # 1. Посчитать количество символов.
print('2. Развернутая строка: ' + text[::-1]) # 2. Развернуть строку.
print('3. Каждое слово с большой буквы: ' + text.title()) # 3. Сделать каждое слово с большой буквы.
print('4. Весь текст прописными буквами: ' + text.upper()) # 4. Сделать весь текст прописными буквами.
print('5.1 Число вхождений "нд" в строку - ' + str(text.count('нд'))) # 5.1. Найти число вхождений "нд" в строку.
print('5.2 Число вхождений "ам" в строку - ' + str(text.count('ам'))) # 5.2. Найти число вхождений "ам" в строку.
print('5.3 Число вхождений "о" в строку - ' + str(text.count('о'))) # 5.3. Найти число вхождений "о" в строку.
print('7. Исходная строка: ' + text) # 7. Вывести в консоль исходную строку.
print('6. Собственные упражнения: ')
print(text[0:2] + text[18:25] + '\n')
print(text[::5] + '\n')

# Method capitalize.
print('Method capitalize:')
print(text.capitalize())
print('\n')

# Method casefold.
print('Method casefold:')
print(text.casefold())
print('\n')

# Method center.
print('Method center:')
print(text.center(150))
print('\n')

# Method encode.
print('Method encode:')
print(text.encode())
print('\n')

# Method endswith.
print('Method endswith:')
print(text.endswith('собака')) 
print(text.endswith('собака', 0, 56))
print('\n')

# Method expandtabs.
print('Method expandtabs:')
tabtext = 'One \t two'
print(tabtext.expandtabs(tabsize = 2))
print(tabtext)
print('\n')

# Method rfind.
print('Method rfind:')
print(text.rfind('а'))
print('\n')

# Method find.
print('Method find:')
print(text.find('а'))
print('\n')

# Method format.
print('Method format:')
print('Не {}, как там в {}'.format('знаю', 'Лондоне') ) 
print('\n')

# Method format in python 3.6.
verb = 'знаю'
city = 'Лондоне'
print(f'Не {verb}, как там в {city}')
print('\n')

# Method split.
print('Method split:')
print(text.split(', '))
print(text.split())
splitted = text.split(', ')
print('\n')

# Methon rsplit.
print('Method rsplit:')
print(text.rsplit(', '))
print('\n')

# Method splitlines.
print('Method splitlines:')
text_splitlines = '123 \n 456 \n 789'
print(text_splitlines.splitlines())
print(text_splitlines.splitlines(True))
print('\n')

# Method join.
print('Method join:')
print('_'.join(splitted))
print('\n')

# Method index.
print('Method index:')
print(text.index('друг'))
print('\n')

# Method rindex.
print('Method rindex:')
print(text.rindex('друг'))
print('\n')

# Method replace.
print('Method replace:')
print(text.replace('там', '999'))
print('\n')

# Method strip.
print('Method strip:')
text_for_strip = '123______322'
print(text_for_strip.strip('123'))
print('\n')

# Method rstrip.
print('Method rstrip:')
print(text_for_strip.rstrip('123'))
print('\n')

# Method removesuffix.
print('Method removesuffix:')
print(text_for_strip.removesuffix('___322'))
print('\n')

# Methon startswith.
print('Method startswith:')
print(text.startswith('Не'))
print(text.startswith('друг', 59))
print('\n')

# Methods isalpha, isalnum, isascii, isprintable.
print('Methods isalpha, isalnum, isascii, isprintable:')
print(text.isalpha())
print(text.isalnum())
print(text.isascii())
print(text.isprintable())
print('\n')

#Method ljust.
print('Method ljust:')
print('1'.ljust(4, 'a'))
print('1'.ljust(2, 'w'))
print('\n')

#Method rjust.
print('Method rjust:')
print('1'.rjust(4, 'a'))
print('1'.rjust(2, 'w'))
print('\n')

#Method translate.
print('Method translate:')
table_trans = str.maketrans({'Л': 'М', 'с': 'к'})
print(text.translate(table_trans))
print('\n')

#Method swapcase.
print('Method swapcase:')
print(text.swapcase())
print('\n')

long_string = 'Не знаю, как там в Лондоне, я не была. '\
              'Может, там собака — друг человека. А у '\
              'нас управдом — друг человека!'
print(long_string)
long_string1 = """
               1) 123dfghjkdfghmbjnfxgvbnm
               2) 456dfhbjnkfgnbmxcvbnm cvbnm
               3) 789gfhbjnkml,hbjnmkfhbjnkmfghbjn
               """
print(long_string1)