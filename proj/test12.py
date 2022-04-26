import tkinter as tk
import pandas as pd
import numpy as np
from tkinter import ttk

root = tk.Tk()

k = ''
bad = 1

def zaprosta():
    if k == "Толкование":    
        df = pd.read_csv('slovarikkkk.txt','\t', on_bad_lines='skip')
        zap = df.iloc[:, [0]]
        ot = df.iloc[:, [1]]
        ot = ot.values
        zp = zap.values

    if k == "Перевод":
        df = pd.read_csv("EN1.csv", encoding='utf-8', on_bad_lines='skip')
        ot = df.loc[2::2, ['a few']] #russ
        zap = df.loc[1::2, ['a few']] #en1
        ot = ot.values
        zp = zap.values
        
    def search(lst, item):
        low = 0
        result = False

        while low < len(lst) and not result:
            if lst[low] == item:
                result = True
            else:
                low += 1
        return result
    
    lst = zp
    value = cityField.get()
    res = search(lst, value)
    bad = 1
    
    if res:
        bad = 0
        index = np.where(lst==value)[0]
        ind = int(index[0])
        info['text'] = 'Это слово означает: '+ ot[ind][0]
            
    else:
        bad = 0
        info['text'] = f'{"К сожалению, слово не найдено..."}'
        
    if bad == 1:
        info['text'] = f'{"Что-то пошло не так"}'
        

param = ("Толкование", "Перевод")

root['bg'] = '#2F4F4F'
root.title('Поисковый алгоритм')
root.geometry('1060x642')
root.resizable(width=False, height=False)


cumb = ttk.Combobox(root, values = param, state = 'readonly')
cumb.current(0)

def com():
    global k
    k = cumb.get()
    print(k)
cumb.pack()

bt_1 = tk.Button(root, activebackground='#7FFFD4')
bt_1.configure(text = 'Применить', command = com)
bt_1.pack()

frame_top = tk.Frame(root, bg='#228B22', bd=10)
frame_top.place(relx=0.1, rely=0.10, relwidth=0.8, relheight=0.2)

frame_bottom = tk.Frame(root, bg='#B2EC5D', bd=5)
frame_bottom.place(relx=0.1, rely=0.42, relwidth=0.8, relheight=0.45)

cityField = tk.Entry(frame_top, bg='white', font=30)
cityField.pack()

btn = tk.Button(frame_top, text='Найти слово!', bd=4,
                activebackground='#7FFFD4',
                command=zaprosta,
                font = ("Times New Roman", 15))
btn.pack()

info = tk.Label(frame_bottom,
                text='Результаты запроса',
                bg='#B2EC5D',
                wraplength=801,
                font = ("Times New Roman", 18),
                anchor='nw',
                justify='left'
                )
info.pack()


root.mainloop() 
