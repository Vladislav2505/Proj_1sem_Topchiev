# Вариант №28
import tkinter as tk  # Ипортируем tkinter


# Задача из PZ_4_1
def PZ_4_1():
    try:
        N = int(en1.get())
        result = 0
        i = N

        while i <= 2 * N:
            result += i ** 2
            i += 1
        print(result)  # Вывод данных.
        g = tk.Label(text=f'{result}',
                     bg='#CD5C5C',
                     fg='black',
                     font=('Arial', '20', 'bold'),
                     padx=100)
        g.place(x=150, y=150)
        lb3 = tk.Label(root, text='ОТВЕТ!!!:',
                       bg='#CD5C5C',
                       fg='black',
                       font=('Arial', '20', 'bold'))
        lb3.place(x=50, y=150)
    except ValueError:
        lb4 = tk.Label(root, text='ОШИБКА!!!',
                       padx=150,
                       bg='#CD5C5C',
                       fg='black',
                       font=('Arial', '20', 'bold'))
        lb4.place(x=0, y=150)


root = tk.Tk()  # Создаем корневое окно
root.title("PZ_4_1")
root.geometry("400x300")  # Устанавливаем размер окна
root.resizable(height=False, width=False)  # Запрет на изменение размера окна
root["bg"] = "#CD5C5C"  # Устанавливаем цвет фона

# Создание и упаковка меток
lb = tk.Label(root, text='Введите целое положительное число > 0:',
              bg='#CD5C5C',
              fg='black',
              font=('Arial', '9', ''))
lb.place(x=0, y=75)

lb2 = tk.Label(root, text="Нахождение суммы",
               bg='#CD5C5C',
               fg='black',
               font=('Arial', '15', 'bold'))
lb2.place(x=100, y=10)

# Создание и упаковка виджета Entry
en1 = tk.Entry(root)
en1.place(x=250, y=76)

# Создание и упаковка кнопки
bu = tk.Button(root, text='Даллее', command=PZ_4_1, fg='black', bg='#4169E1')
bu.place(x=325, y=100)

root.mainloop()  # Запускаем главный цикл приложения
