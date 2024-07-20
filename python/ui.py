import interface as inter
import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("To Do List")
root.geometry('1080x720')


def clear_widget(row, column):
    for widget in root.grid_slaves(row=row, column=column):
        widget.grid_forget()


def insert_menu():
    if not hasattr(insert_menu, 'submit_button'):
        # Task Input
        insert_menu.task_label = tk.Label(root, text="Task Name:")
        insert_menu.task_label.grid(row=1, column=1, padx=0, pady=5)

        insert_menu.task = tk.Entry(root)
        insert_menu.task.grid(row=1, column=2, padx=5, pady=5)

        # Time Input
        insert_menu.time_label = tk.Label(root, text="Time:")
        insert_menu.time_label.grid(row=2, column=1, padx=0, pady=5)

        insert_menu.time = tk.Entry(root)
        insert_menu.time.grid(row=2, column=2, padx=5, pady=5)

        insert_menu.submit_button = tk.Button(root, text="Submit", command=lambda: process_insert_task(insert_menu.task.get(), insert_menu.time.get()))
        insert_menu.submit_button.grid(row=1, column=3, padx=0, pady=5)


def process_insert_task(task, time):
    # insert the task into the list
    if not task.isdigit() and time.isdigit():
        clear_widget(1, 5)
        to_print = "Valid Additions: " + task + " " + "{:.2f}".format(float(time))
        text = tk.Label(root, text=to_print)
        text.grid(row=1, column=5, padx=5, pady=5)

        # call to interface
        inter.insert_task(task, float(time))
        print_menu()

        # clear the entries
        insert_menu.task.delete(0, tk.END)
        insert_menu.time.delete(0, tk.END)
    else:
        text = tk.Label(root, text="Invalid Entry: (Insert Time as integer, no decimals) or (Task has no characters)")
        text.grid(row=1, column=5, padx=5, pady=5)


def remove_menu():
    if not hasattr(remove_menu, 'submit_button'):
        # task to be removed
        remove_menu.task_label = tk.Label(root, text="Task Name:")
        remove_menu.task_label.grid(row=6, column=1, padx=0, pady=5)

        remove_menu.task = tk.Entry(root)
        remove_menu.task.grid(row=6, column=2, padx=5, pady=5)

        remove_menu.submit_button = tk.Button(root, text="Submit", command=lambda: process_remove_task(remove_menu.task.get()))
        remove_menu.submit_button.grid(row=6, column=3, padx=0, pady=5)


def process_remove_task(task):
    if not task.isdigit():
        if inter.remove_task(task) is True:
            clear_widget(6, 5)
            to_print = "Success: " + task + " has been removed"
            text = tk.Label(root, text=to_print)
            text.grid(row=6, column=5, padx=5, pady=5)

            # clear the entries
            remove_menu.task.delete(0, tk.END)
            print_menu()
    else:
        text = tk.Label(root, text="Invalid Entry: (Task has no characters)")
        text.grid(row=6, column=5, padx=5, pady=5)


def print_menu():
    # task to be removed
    clear_widget(11, 5)
    print_menu.task_label = tk.Label(root, text="Current List:", bg="yellow")
    print_menu.task_label.grid(row=11, column=1, padx=0, pady=5)
    process_print_task()


def process_print_task() -> None:
    clear_widget(12, 5)
    tuple_tasks = inter.print_task_list()

    count = 0
    column = 2
    rows = 12
    for task, time in tuple_tasks:
        to_print = f"[ ({count}) Task: {task}, Time: {time} ]"
        label = tk.Label(root, text=to_print)
        label.grid(row=rows, column=column+1, padx=5, pady=5)
        if column + 1 == 5:
            column = 2
            rows += 1
        else:
            column += 1
        count += 1


def main_menu():

    insert_button = tk.Button(
        text="Insert Task",
        width=30,
        height=5,
        bg="white",
        command=insert_menu
    )
    insert_button.grid(row=1, column=0, rowspan=5, padx=10, pady=10)

    remove_button = tk.Button(
        text="Remove Task",
        width=30,
        height=5,
        bg="white",
        command=remove_menu
    )
    remove_button.grid(row=6, column=0, rowspan=5, padx=10, pady=10)

    print_button = tk.Button(
        text="Print List",
        width=30,
        height=5,
        bg="white",
        command=print_menu
    )
    print_button.grid(row=11, column=0, rowspan=5, padx=10, pady=10)

    exit_button = tk.Button(
        text="Exit",
        width=30,
        height=5,
        bg="red",
        command=root.quit
    )
    exit_button.grid(row=21, column=0, rowspan=5, padx=10, pady=10)

    # This is all the main title
    bold_font = font.Font(family="Helvetica", size=20, weight="bold")
    title = tk.Label(root, text="To Do List: CAMMY CORP", font=bold_font)
    title.grid(row=0, column=0, padx=10, pady=10)

    # RUN IT UP
    root.mainloop()


main_menu()
