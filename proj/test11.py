import tkinter as tk
import pandas as pd
import numpy as np

root = tk.Tk()

def zaprosta():
    df = pd.read_csv('slovarikkkk.txt','\t', on_bad_lines='skip')
    zap = df.iloc[:, [0]]
    ot = df.iloc[:, [1]]
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

    if res:
        index = np.where(lst==value)[0]
        ind = int(index[0])
        info['text'] = 'Это слово означает: '+ ot[ind][0]
        
    else:
        info['text'] = f'{"К сожалению, слово не найдено..."}'


root['bg'] = '#A9A9A9'
root.title('Поисковый алгоритм')
root.geometry('1060x642')
root.resizable(width=False, height=False)

frame_top = tk.Frame(root, bg='#3CB371', bd=5)
frame_top.place(relx=0.1, rely=0.10, relwidth=0.8, relheight=0.2)

frame_bottom = tk.Frame(root, bg='#2E8B57', bd=5)
frame_bottom.place(relx=0.1, rely=0.42, relwidth=0.8, relheight=0.4)

cityField = tk.Entry(frame_top, bg='white', font=30)
cityField.pack()
btn = tk.Button(frame_top, text='Найти слово!', command=zaprosta)
btn.pack()

info = tk.Label(frame_bottom,
                text='Результаты запроса',
                bg='#2E8B57',
                wraplength=801,
                font = ("Times New Roman", 16),
                anchor='nw',
                justify='left'
                )
info.pack()

root.mainloop() 
