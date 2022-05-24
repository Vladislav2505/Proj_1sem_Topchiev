# Вариант №28
# Приложение ПАРИКМАХЕРСКАЯ для некоторой организации.

import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):  # Функция главного окна

        # Создание кнопок и добавление картинок

        toolbar = tk.Frame(bg='#009E8E', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="DB/add.png")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить запись', command=self.open_dialog,
                                         bg='#009E8E', bd=0,
                                         compound=tk.TOP, image=self.add_img, width=100, fg='black')
        self.btn_open_dialog.pack(side=tk.LEFT, padx=25)

        self.update_img = tk.PhotoImage(file="DB/update.png")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать запись", command=self.open_update_dialog,
                                    bg='#009E8E',
                                    bd=0, compound=tk.TOP, image=self.update_img, width=120, fg='black')
        btn_edit_dialog.pack(side=tk.LEFT, padx=25)

        self.delete_img = tk.PhotoImage(file="DB/delete.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#009E8E',
                               bd=0, compound=tk.TOP, image=self.delete_img, width=100, fg='black')
        btn_delete.pack(side=tk.LEFT, padx=25)

        self.search_img = tk.PhotoImage(file="DB/search.gif")
        btn_search = tk.Button(toolbar, text="Поиск стоимости", command=self.open_search_dialog, bg='#009E8E',
                               bd=0, compound=tk.TOP, image=self.search_img, width=100, fg='black')
        btn_search.pack(side=tk.LEFT, padx=25)

        self.refresh_img = tk.PhotoImage(file="DB/refresh.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#009E8E',
                                bd=0, compound=tk.TOP, image=self.refresh_img, width=100, fg='black')
        btn_refresh.pack(side=tk.LEFT, padx=25)

        self.tree = ttk.Treeview(self, columns=('client_id', 'master', 'client', 'sex', 'Haircut', 'price'), height=15,
                                 show='headings')

        # Колонки БД на главном окне

        self.tree.column('client_id', width=50, anchor=tk.CENTER)
        self.tree.column('master', width=180, anchor=tk.CENTER)
        self.tree.column('client', width=140, anchor=tk.CENTER)
        self.tree.column('sex', width=100, anchor=tk.CENTER)
        self.tree.column('Haircut', width=140, anchor=tk.CENTER)
        self.tree.column('price', width=140, anchor=tk.CENTER)

        self.tree.heading('client_id', text='ID')
        self.tree.heading('master', text='ФИО Мастера')
        self.tree.heading('client', text='ФИО Клиента')
        self.tree.heading('sex', text='Пол клиента')
        self.tree.heading('Haircut', text='Название стрижки')
        self.tree.heading('price', text='Стоимость руб')

        self.tree.pack()

    def records(self, client_id, master, client, sex, Haircut, price):
        self.db.insert_data(client_id, master, client, sex, Haircut, price)
        self.view_records()

    def update_record(self, client_id, master, client, sex, Haircut, price):
        self.db.cur.execute("""UPDATE salon SET client_id=?, master=?, client=?, sex=?, Haircut=?, price=? 
        WHERE client_id=?""",
                            (client_id, master, client, sex, Haircut, price, self.tree.set(self.tree.selection()[0],
                                                                                           '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM salon""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM salon WHERE client_id=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, price):
        price = (price,)
        self.db.cur.execute("""SELECT * FROM salon WHERE price>?""", price)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):  # Функция дочернего окна

        # Оформление дочернего окна

        self.title('Добавить клиента')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Номер клиента')
        label_description.place(x=15, y=25)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=140, y=25)

        label_name = tk.Label(self, text='Имя мастера')
        label_name.place(x=15, y=50)
        self.entry_master = ttk.Entry(self)
        self.entry_master.place(x=140, y=50)

        label_name = tk.Label(self, text='Имя клиента')
        label_name.place(x=15, y=75)
        self.entry_client = ttk.Entry(self)
        self.entry_client.place(x=140, y=75)

        label_sex = tk.Label(self, text='Пол')
        label_sex.place(x=15, y=100)
        self.combobox = ttk.Combobox(self, values=[u'Мужской', u'Женский'])
        self.combobox.current(0)
        self.combobox.place(x=140, y=100)

        label_old = tk.Label(self, text='Название стрижки')
        label_old.place(x=15, y=125)
        self.entry_haircut = ttk.Entry(self)
        self.entry_haircut.place(x=140, y=125)

        label_score = tk.Label(self, text='Цена')
        label_score.place(x=15, y=150)
        self.entry_price = ttk.Entry(self)
        self.entry_price.place(x=140, y=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=180)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=180)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_master.get(),
                                                                       self.entry_client.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_haircut.get(),
                                                                       self.entry_price.get()))
        self.grab_set()
        self.focus_set()


class Update(Child):
    """Класс для окна редактирования записи"""

    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=180)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_master.get(),
                                                                          self.entry_client.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_haircut.get(),
                                                                          self.entry_price.get()))
        self.btn_ok.destroy()


class Search(tk.Toplevel):
    """Класс для окна поиска"""

    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск (> стоимость )")  # Функция получения информации по стоимости (Значение > стоимость)
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Стоимость")
        label_search.place(x=35, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add=True)


class DB:
    """Класс для правильной работы БД"""

    def __init__(self):
        with sq.connect('DB/services.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS salon(
                client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                master TEXT NOT NULL,
                client TEXT NOT NULL,
                sex INTEGER NOT NULL DEFAULT 1,
                Haircut TEXT NOT NULL,
                price INTEGER
                )""")

    def insert_data(self, client_id, master, client, sex, Haircut, price):
        self.cur.execute("""INSERT INTO salon(client_id, master, client, sex, Haircut, price) 
        VALUES (?, ?, ?, ?, ?, ?)""",
                         (client_id, master, client, sex, Haircut, price))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Работа с базой данных Салон")
    root.geometry("815x400+300+200")
    root.configure(bg='#04859D')
    root.iconphoto(True, tk.PhotoImage(file='DB/icon.png'))
    root.resizable(False, False)
    root.mainloop()