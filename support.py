import tkinter as tk
from tkinter import messagebox

def read_todo_file(file_path):
    subjects = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        parts = [part.strip().strip('"') for part in line.split('"') if part.strip()]
                        if len(parts) >= 2:
                            subject, task = parts[0], parts[1]
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
            file.write(f'"{subject}",""\n')
    except Exception as e:
        raise Exception(f"An error occurred while writing to the file: {e}")

def write_task_to_file(file_path, subject, task):
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f'"{subject}","{task}"\n')
    except Exception as e:
        raise Exception(f"An error occurred while writing to the file: {e}")

def create_checklist(canvas, subjects, colors):
    y_offset = 10
    for subject, tasks in subjects.items():
        frame_height = 40 + len(tasks) * 30
        frame = tk.Frame(master=canvas, bg=colors[2], height=frame_height)
        canvas.create_window((10, y_offset), anchor="nw", window=frame, width=340, height=frame_height)

        label = tk.Label(master=frame, text=subject, bg=colors[2], fg="#000", font=('Helvetica', 12, 'bold'))
        label.place(x=10, y=10)

        for i, task in enumerate(tasks):
            var = tk.IntVar()
            check_box = tk.Checkbutton(master=frame, text=task, bg=colors[2], fg="#000", variable=var)
            check_box.place(x=30, y=40 + i * 30)

        y_offset += frame_height + 10

    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
