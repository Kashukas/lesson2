from digits_keyword import digits_kw

def add_time_symb():
    for n in range(0, 8, 1):
        list_time.append(digits_kw[time_str[n]])

def create_print_list():
    for z in range(0, 5, 1):
        for m in range(0, 8, 1):
            list_print[z] += list_time[m][z]

def print_time():
    for k in range(0, 5, 1):
        print(list_print[k])

while True:
    import datetime
    import os
    import time
    
    time_str = str(datetime.datetime.now().time())
    list_time = []
    list_print = ['', '', '', '', '']
    
    add_time_symb()
    
    create_print_list()

    print_time()
    
    # print(time_str[0:8])
    
    print('''
    Press Ctrl+C to stop
    ''')
    
    time.sleep(0.9)
    os.system('CLS')