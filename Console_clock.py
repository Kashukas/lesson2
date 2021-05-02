from digits_dict import digits_d  # Import digits dictionary.

def add_time_symb():  # Create current time digits list.
    for n in range(0, 8, 1):
        list_time.append(digits_d[time_str[n]])

def create_print_list():
    for z in range(0, 5, 1):
        for m in range(0, 8, 1):
            list_print[z] += list_time[m][z]

def print_time():  # Print list_print line by line.
    for k in range(0, 5, 1):
        print(list_print[k])

while True:  # Clock cycle.
    import datetime
    import os
    import time
    import colon_blinking
    
    time_str = str(datetime.datetime.now().time())
    list_time = []
    list_print = ['', '', '', '', '']
    
    add_time_symb()
    
    create_print_list()

    print_time()

    colon_blinking.colon_blinking()
    
    print('''
    Press Ctrl+C to stop
    ''')
    
    time.sleep(0.9)  # Delay.
    os.system('CLS')  # Screen clear.