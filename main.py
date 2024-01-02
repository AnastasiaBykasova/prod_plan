import tkinter as tk
from tkinter import ttk
import sqlite3

def show_greeting_window():
    window = tk.Tk()
    window.title("ProdPlan")

    window.geometry("400x300")

    greeting_label = tk.Label(window, text="Welcome")
    greeting_label.pack(padx=20, pady=20)
    
    window.mainloop()

show_greeting_window()

conn = sqlite3.connect('prod_plan.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS machines
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT)''')

def add_machine(cursor, name):
    cursor.execute("INSERT INTO machines (name) VALUES (?)", (name,))

machines = ["Станок 1", "Станок 2", "Станок 3", "Станок 4", "Станок 5",
            "Станок 6", "Станок 7", "Станок 8", "Станок 9", "Станок 10"]

# for machine in machines:
#     add_machine(cursor, machine)

conn.commit()
conn.close()

def get_machines_from_db():
    conn = sqlite3.connect('prod_plan.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM machines") 
    machines = [row[0] for row in cursor.fetchall()]
    conn.close()
    return machines


# def show_machines_window():
#     machines = get_machines_from_db()

#     # Создаем главное окно
#     window = tk.Tk()
#     window.title("Список станков")
#     window.geometry("400x300")


#     # Создаем список (Listbox) для отображения названий станков
#     machines_list = tk.Listbox(window)
#     for machine in machines:
#         machines_list.insert(tk.END, machine)
#     machines_list.pack(padx=20, pady=20)

#     # Запускаем главный цикл обработки событий
#     window.mainloop()


# Создаем функцию для отображения окна с выпадающим списком и кнопкой
def show_selection_window():
    machines = get_machines_from_db()

    def on_button_click():
        selected_machine = machine_combobox.get()
        label.config(text="Выбран станок: " + selected_machine)

    # Создаем главное окно
    window = tk.Tk()
    window.title("Выбор станка")
    window.geometry("600x500")

    # Создаем выпадающий список (Combobox) для выбора станка
    machine_combobox = ttk.Combobox(window, values=machines)
    machine_combobox.pack(padx=20, pady=10)

    # Создаем кнопку
    button = tk.Button(window, text="Выбрать", command=on_button_click)
    button.pack(pady=10)

    # Создаем метку, которая будет отображать выбранный станок
    label = tk.Label(window, text="")
    label.pack(pady=10)

    # Запускаем главный цикл обработки событий
    window.mainloop()

# Вызываем функцию для отображения окна с выбором станка
show_selection_window()
