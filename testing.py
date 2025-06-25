import tkinter as tk
from tkinter import messagebox

colors = ["#1a1f16", "#1e3f20", "#345830", "#4a7856", "#94ecbe"]

def read_todo_file(file_path):
    subjects = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        subject, task = line.split(',')
                        subject = subject.strip().strip('"')
                        task = task.strip().strip('"')

                        if subject not in subjects:
                            subjects[subject] = []
                        subjects[subject].append(task)
                    except ValueError as e:
                        print(f"Error parsing line: {line}. Error: {e}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return subjects

def write_subject_to_file(file_path, subject):
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            # Just write the subject without a task
            file.write(f'"{subject}",""\n')
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while writing to the file: {e}")

def write_task_to_file(file_path, subject, task):
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f'"{subject}","{task}"\n')
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while writing to the file: {e}")

def create_checklist(main, subjects):
    y_offset = 74
    for subject, tasks in subjects.items():
        frame_height = 40 + len(tasks) * 30
        frame = tk.Frame(master=main, bg=colors[2], height=frame_height)
        frame.place(x=11, y=y_offset, width=350, height=frame_height)

        label = tk.Label(master=frame, text=subject, bg=colors[2], fg="#000", font=('Helvetica', 12, 'bold'))
        label.place(x=10, y=10)

        for i, task in enumerate(tasks):
            var = tk.IntVar()
            check_box = tk.Checkbutton(master=frame, text=task, bg=colors[2], fg="#000", variable=var)
            check_box.place(x=30, y=40 + i * 30)

        y_offset += frame_height + 10

def add_task(file_path, subjects, subject_var, task_entry, option_menu):
    subject = subject_var.get()
    task = task_entry.get()

    if subject and task:
        if subject in subjects:
            subjects[subject].append(task)
        else:
            subjects[subject] = [task]

        write_task_to_file(file_path, subject, task)
        option_menu['menu'].delete(0, 'end')

        for subject in subjects:
            option_menu['menu'].add_command(label=subject, command=tk._setit(subject_var, subject))

        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input error", "Subject and task cannot be empty.")

def add_subject(file_path, subjects, subject_entry, option_menu):
    subject = subject_entry.get()

    if subject:
        if subject not in subjects:
            subjects[subject] = []
            write_subject_to_file(file_path, subject)
            option_menu['menu'].add_command(label=subject, command=tk._setit(option_menu.cget("textvariable"), subject))
            subject_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input error", "Subject already exists.")
    else:
        messagebox.showwarning("Input error", "Subject cannot be empty.")

def main():
    main = tk.Tk()
    main.title("Main Window")
    main.config(bg=colors[1])
    main.geometry("1024x600")

    file_path = r"C:\Users\Brody Evans\Documents\GitHub\SableOS\todolist.opfile"
    subjects = read_todo_file(file_path)

    if subjects:
        create_checklist(main, subjects)
    else:
        print("No subjects found or error reading the file.")

    frame1 = tk.Frame(master=main, bg=colors[2])
    frame1.place(x=415, y=292, width=370, height=270)

    subject_var = tk.StringVar(main)
    subject_var.set(next(iter(subjects)) if subjects else "")

    option_menu = tk.OptionMenu(frame1, subject_var, *subjects)
    option_menu.config(bg=colors[1], fg="#000")
    option_menu.place(x=21, y=16)

    entry1 = tk.Entry(master=frame1, bg=colors[2], fg="#000")
    entry1.place(x=178, y=23, width=121, height=40)

    button1 = tk.Button(master=frame1, text="Add Task", bg=colors[1], fg="#000",
                       command=lambda: add_task(file_path, subjects, subject_var, entry1, option_menu))
    button1.place(x=228, y=168, width=115, height=80)

    frame2 = tk.Frame(master=main, bg=colors[2])
    frame2.place(x=409, y=99, width=370, height=170)

    entry2 = tk.Entry(master=frame2, bg=colors[2], fg="#000")
    entry2.place(x=41, y=61, width=121, height=42)

    button2 = tk.Button(master=frame2, text="Add Subject", bg=colors[1], fg="#000",
                       command=lambda: add_subject(file_path, subjects, entry2, option_menu))
    button2.place(x=225, y=35, width=115, height=80)

    button3 = tk.Button(master=main, text="Back", bg=colors[1], fg="#000")
    button3.place(x=870, y=195, width=115, height=80)

    button = tk.Button(master=main, text="Daily Routine", bg=colors[1], fg="#000")
    button.place(x=870, y=394, width=115, height=80)

    main.mainloop()

if __name__ == "__main__":
    main()
