# Вариант №28
import tkinter as tk  # Ипортируем tkinter
from tkinter import ttk

root = tk.Tk()  # Создаем корневое окно
root.title("Sign in")
root.geometry("580x700")  # Устанавливаем размер окна
root["bg"] = "#222536"  # Устанавливаем цвет фона
root.resizable(height=False, width=False)  # Запрет на изменение размера окна

#  Создание и упаковка метки "Sign up"
lb = tk.Label(root, text='Sign up',
              bg='orange',
              fg='yellow',
              pady=10,
              width=100,
              font=('Arial', '15', 'bold'),
              anchor='w')
lb.place(x=0, y=0)

#  Создание и упаковка метки "First Name"
lb2 = tk.Label(root, text='First Name',
               bg='#222536',
               fg='yellow',
               pady=10,
               width=10,
               font=('Arial', '12', ''))
lb2.place(x=90, y=50)

en = tk.Entry()
en.place(x=200, y=60, width=350, height=25)

#  Создание и упаковка метки "Last Name"
lb3 = tk.Label(root, text='Last Name',
               bg='#222536',
               fg='yellow',
               pady=10,
               width=10,
               font=('Arial', '12', ''))
lb3.place(x=90, y=100)

en2 = tk.Entry()
en2.place(x=200, y=110, width=350, height=25)

#  Создание и упаковка метки "Screen Name"
lb4 = tk.Label(root, text='Screen Name',
               bg='#222536',
               fg='yellow',
               pady=10,
               width=10,
               font=('Arial', '12', ''))
lb4.place(x=90, y=150)

en3 = tk.Entry()
en3.place(x=200, y=160, width=350, height=25)

#  Создание и упаковка метки "Date of Birth"
lb5 = tk.Label(root, text='Date of Birth',
               bg='#222536',
               fg='yellow',
               pady=10,
               width=10,
               font=('Arial', '12', ''))
lb5.place(x=90, y=200)

Cb = ttk.Combobox()
Cb.place(x=200, y=210, width=130, height=25)
Cb2 = ttk.Combobox()
Cb2.place(x=355, y=210, width=60, height=25)
Cb3 = ttk.Combobox()
Cb3.place(x=440, y=210, width=110, height=25)

#  Создание и упаковка метки "Gender"
lb6 = tk.Label(root, text='Gender',
               bg='#222536',
               fg='yellow',
               pady=10,
               width=10,
               font=('Arial', '12', ''))
lb6.place(x=105, y=250)

rad0 = tk.Radiobutton(root, text="Male",
                      bg='#222536',
                      fg='yellow',
                      font=('Arial', '12', ''))
rad0.place(x=200, y=255)
rad1 = tk.Radiobutton(root, text="Female",
                      bg='#222536',
                      fg='yellow',
                      font=('Arial', '12', ''))
rad1.place(x=265, y=255)

#  Создание и упаковка метки "Country"
lb7 = tk.Label(root, text='Country',
               bg='#222536',
               fg='yellow',
               pady=10,
               width=10,
               font=('Arial', '12', ''))
lb7.place(x=105, y=300)

Cb4 = ttk.Combobox()
Cb4.place(x=200, y=310, width=350, height=25)

#  Создание и упаковка метки "E-mail"
lb8 = tk.Label(root, text='E-mail',
               bg='#222536',
               fg='yellow',
               pady=10,
               width=10,
               font=('Arial', '12', ''))
lb8.place(x=105, y=350)

en4 = tk.Entry()
en4.place(x=200, y=360, width=350, height=25)

#  Создание и упаковка метки "Phone"
lb9 = tk.Label(root, text='Phone',
               bg='#222536',
               fg='yellow',
               pady=10,
               width=10,
               font=('Arial', '12', ''))
lb9.place(x=105, y=400)

en5 = tk.Entry()
en5.place(x=200, y=410, width=350, height=25)

#  Создание и упаковка метки "Password"
lb10 = tk.Label(root, text='Password',
                bg='#222536',
                fg='yellow',
                pady=10,
                width=10,
                font=('Arial', '12', ''))
lb10.place(x=90, y=450)

en6 = tk.Entry()
en6.place(x=200, y=460, width=350, height=25)

#  Создание и упаковка метки "Confirm Password"
lb11 = tk.Label(root, text='Confirm Password',
                bg='#222536',
                fg='yellow',
                pady=10,
                width=15,
                font=('Arial', '12', ''))
lb11.place(x=38, y=500)

en7 = tk.Entry()
en7.place(x=200, y=510, width=350, height=25)

che = tk.Checkbutton(root, text='I agree to the Terms of Use',
                     bg='#222536',
                     fg='yellow',
                     pady=10,
                     width=20,
                     font=('Arial', '12', ''))
che.place(x=197, y=560)

lb12 = tk.Label(root, text='',
                bg='orange',
                fg='yellow',
                pady=50,
                width=100,
                font=('Arial', '15', 'bold'),
                anchor='w')
lb12.place(x=0, y=640)

#  Создание и упаковка метки "submit"
lb13 = tk.Button(root, text='submit',
                 bg='#5bb85d',
                 fg='white',
                 padx=10,
                 pady=5,
                 font=('Arial', '10', 'bold'),
                 anchor='center')
lb13.place(x=425, y=655)

#  Создание и упаковка метки "Cancel"
lb14 = tk.Button(root, text='Cancel',
                 bg='#d1584c',
                 fg='white',
                 padx=10,
                 pady=5,
                 font=('Arial', '10', 'bold'),
                 anchor='center')
lb14.place(x=500, y=655)
root.mainloop()  # Запускаем главный цикл приложения
