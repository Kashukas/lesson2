digits_kw = {
        '1': [
        ' \u25A0 ',
        ' \u25A0 ',
        ' \u25A0 ',
        ' \u25A0 ',
        ' \u25A0 '],
        '2': [
        ' \u25A0\u25A0\u25A0 ',
        '   \u25A0 ',
        ' \u25A0\u25A0\u25A0 ',
        ' \u25A0   ',
        ' \u25A0\u25A0\u25A0 '],
        '3': [
        ' \u25A0\u25A0\u25A0 ',
        '   \u25A0 ',
        ' \u25A0\u25A0\u25A0 ',
        '   \u25A0 ',
        ' \u25A0\u25A0\u25A0 '],
        '4': [
        ' \u25A0 \u25A0 ',
        ' \u25A0 \u25A0 ',
        ' \u25A0\u25A0\u25A0 ',
        '   \u25A0 ',
        '   \u25A0 '],
        '5': [
        ' \u25A0\u25A0\u25A0 ',
        ' \u25A0   ',
        ' \u25A0\u25A0\u25A0 ',
        '   \u25A0 ',
        ' \u25A0\u25A0\u25A0 '],
        '6': [
        ' \u25A0\u25A0\u25A0 ',
        ' \u25A0   ',
        ' \u25A0\u25A0\u25A0 ',
        ' \u25A0 \u25A0 ',
        ' \u25A0\u25A0\u25A0 '],
        '7': [
        ' \u25A0\u25A0\u25A0 ',
        '   \u25A0 ',
        '   \u25A0 ',
        '   \u25A0 ',
        '   \u25A0 '],
        '8': [
        ' \u25A0\u25A0\u25A0 ',
        ' \u25A0 \u25A0 ',
        ' \u25A0\u25A0\u25A0 ',
        ' \u25A0 \u25A0 ',
        ' \u25A0\u25A0\u25A0 '],
        '9': [
        ' \u25A0\u25A0\u25A0 ',
        ' \u25A0 \u25A0 ',
        ' \u25A0\u25A0\u25A0 ',
        '   \u25A0 ',
        ' \u25A0\u25A0\u25A0 '],
        '0': [
        ' \u25A0\u25A0\u25A0 ',
        ' \u25A0 \u25A0 ',
        ' \u25A0 \u25A0 ',
        ' \u25A0 \u25A0 ',
        ' \u25A0\u25A0\u25A0 '],
        ':': [
        '   ',
        ' \u25A0 ',
        '   ',
        ' \u25A0 ',
        '   '],
        ':_': [
        '   ',
        '   ',
        ' \u25A0 ',
        '   ',
        '   ']}

while True:
    import datetime
    import os
    import time
    
    time_str = str(datetime.datetime.now().time())
    list_time = []
    list_print = ['', '', '', '', '']
    
    for n in range(0, 8, 1):
        list_time.append(digits_kw[time_str[n]])

    for z in range(0, 5, 1):
        for m in range(0, 8, 1):
            list_print[z] += list_time[m][z]
    
    print(time_str[0:8])
    
    for k in range(0, 5, 1):
        print(list_print[k])
   
    print('''
    Press Ctrl+C to stop
    ''')
    
    time.sleep(0.9)
    os.system('CLS')