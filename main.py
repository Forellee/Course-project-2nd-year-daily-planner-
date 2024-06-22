import tkinter
from time import strftime
from tkinter import messagebox
import customtkinter

# Флаг для отслеживания текущего формата времени
is_us_time = False


def toggle_time_format():
    global is_us_time
    is_us_time = not is_us_time


def time():
    if is_us_time:
        string = strftime('%I:%M:%S %p')
    else:
        string = strftime('%H:%M:%S')
    time_label.config(text=string)
    time_label.after(1000, time)



def us_time():
    string = strftime('%I:%M:%S %p')
    time_label.config(text=string)
    time_label.after(1000, us_time)


def count_updater():  # Обновляет количество задач в task_count. Использовать в кнопках для обновления по нажатию.
    clear_listbox()
    for task in task_list:
        listbox_tasks.insert("end", task)
    numtask = len(task_list)
    task_count['text'] = numtask


def add_task():
    empty_field_text["text"] = ""
    new_task = text_input.get()
    if new_task != "":
        task_list.append(new_task)
        count_updater()
    else:
        empty_field_text["text"] = "Введите текст"
    text_input.delete(0, 'end')


def clear_listbox():
    listbox_tasks.delete(0, "end")


def delete_all():
    delask = messagebox.askquestion(
        'Удалить всё', 'Вы согласны?')
    print(delask)
    if delask.upper() == "YES":
        global task_list
        task_list = []
        count_updater()
    else:
        pass


def completed():
    choice = listbox_tasks.get("active")
    if choice in task_list:
        task_list.remove(choice)
    count_updater()


def sort_abc():
    task_list.sort()
    count_updater()


def saver():
    saveask = messagebox.askquestion(
        'Сохранение', 'Сохранить?')
    if saveask.upper() == "YES":
        with open("SaveFile.txt", "w") as filehandle:
            for listitem in task_list:
                filehandle.write('%s\n' % listitem)
    else:
        pass


def loader():
    loadask = messagebox.askquestion(
        'Загрузить', 'Подтвердите загрузку')
    if loadask.upper() == "YES":
        task_list.clear()

        with open('SaveFile.txt', 'r') as filereader:
            for line in filereader:
                currentask = line
                task_list.append(currentask)
            count_updater()

    else:
        pass


def close_app():
    closer = messagebox.askquestion(
        'Выход', 'Хотите закрыть программу?')
    if closer.upper() == "YES":
        window.destroy()
    else:
        pass


def about():
    messagebox.showinfo(
        "О программе", "  Daily Planner \n\n  Манохов Максим \n\n  2023")


"""Настройка окна window"""

window = customtkinter.CTk()
window.resizable(False, False)
window.title("Daily Planner")
window.geometry("490x400+1390+290")  # Вернуть после работы window.geometry("490x400+690+290")
window.attributes("-topmost", True)  # УДАЛИТЬ!!! Сделано для удобства написания текстовой части


# Список задач
task_list = []


"""Виджеты"""

label_title = customtkinter.CTkLabel(window, text="Список задач", font=("Calibri Bold", 20))
label_title.grid(row=0, column=0, padx=10, pady=10)

empty_field_text = tkinter.Label(window, text="")
empty_field_text.grid(row=0, column=1)

task_count = tkinter.Label(window, text="")
task_count.grid(row=0, column=2, columnspan=2)

text_input = customtkinter.CTkEntry(window, width=300)
text_input.grid(row=1, column=1, columnspan=2)

complete_button = customtkinter.CTkButton(
    window, text="Выполнить", corner_radius=10, command=completed)
complete_button.grid(row=2, column=1, pady=5)

"""Кнопки"""

text_add_button = customtkinter.CTkButton(
    window, text="Добавить", font=("Arial", 15), fg_color="green", width=1, corner_radius=15, command=add_task)
text_add_button.grid(row=1, column=0)

delete_all_button = customtkinter.CTkButton(
    window, text="Удалить всё", fg_color="Red", corner_radius=10, command=delete_all)
delete_all_button.grid(row=2, column=2, pady=5)

sort_abc = customtkinter.CTkButton(window, text="По алфавиту", text_color="black", width=100, fg_color="white",
                                   border_color="black",
                                   border_width=1, corner_radius=15, command=sort_abc)
sort_abc.grid(row=4, column=0)

exit_button = customtkinter.CTkButton(window, text="Выход", text_color="black", width=100, fg_color="white",
                                      border_color="black",
                                      border_width=1, corner_radius=15, command=close_app)
exit_button.grid(row=8, column=0)

save_button = customtkinter.CTkButton(
    window, text="Сохранение", text_color="black", fg_color="white", border_color="black",
    border_width=1, corner_radius=10, command=saver)
save_button.grid(row=10, column=1)

load_button = customtkinter.CTkButton(
    window, text="Загрузка", text_color="black", fg_color="white", border_color="black",
    border_width=1, corner_radius=10, command=loader)
load_button.grid(row=10, column=2)

about_button = customtkinter.CTkButton(
    window, text="Информация", width=15, fg_color="gray", command=about)
about_button.grid(row=11, column=0, columnspan=1, pady=15)

listbox_tasks = tkinter.Listbox(window, width=50)
listbox_tasks.grid(row=3, column=1, rowspan=7, columnspan=2, pady=5)


"""Часы"""

time_label = tkinter.Label(window)
time_label.grid(row=11, column=2, columnspan=3, padx=130, pady=45)
time()


"""Настройки"""
def unlocker():
    window.attributes('-disabled', False)


def preventClose():
    pass


def settings_window():
    set_window = tkinter.Tk()
    set_window.title("Настройки")
    set_window.geometry("300x200+1390+290")
    set_window.attributes("-topmost", True)
    set_window.protocol("WM_DELETE_WINDOW", preventClose)
    window.attributes('-disabled', True)
    set_window.resizable(False, False)
    settings_label = tkinter.Label(set_window, text="Меню настроек")
    settings_label.grid(row=0, column=2, padx=100, pady=5)
    time_format_button = tkinter.Button(set_window, text="Сменить формат времени", command=toggle_time_format)
    time_format_button.grid(row=1, column=2, pady=5)
    close_button = tkinter.Button(set_window, text="Закрыть окно", command=lambda: [set_window.destroy(), unlocker()])
    close_button.grid(row=3, column=2, pady=45)

settings_button = customtkinter.CTkButton(window, text="Настройки", text_color="black", width=100, fg_color="white",
                                          border_color="black", border_width=1, corner_radius=15,
                                          command=settings_window)
settings_button.grid(row=5, column=0)

window.mainloop()