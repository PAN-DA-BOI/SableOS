import os
import tkinter as tk
import tkinterweb
from support import read_todo_file, write_subject_to_file, write_task_to_file, create_checklist
colors = ["#1a1f16", "#1e3f20", "#345830", "#4a7856", "#94ecbe"]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("SableOS")
main.config(bg=colors[0])
main.geometry("1024x600")

def add_task(file_path, subjects, subject_var, task_entry, option_menu, canvas):
    subject = subject_var.get()
    task = task_entry.get()

    if subject and task:
        if subject in subjects:
            subjects[subject].append(task)
        else:
            subjects[subject] = [task]

        try:
            write_task_to_file(file_path, subject, task)
            task_entry.delete(0, tk.END)
            canvas.delete("all")
            create_checklist(canvas, subjects, colors)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input error", "Subject and task cannot be empty.")
def add_subject(file_path, subjects, subject_entry, option_menu, subject_var, canvas):
    subject = subject_entry.get()

    if subject:
        if subject not in subjects:
            subjects[subject] = []
            try:
                write_subject_to_file(file_path, subject)
                subject_entry.delete(0, tk.END)

                menu = option_menu["menu"]
                menu.delete(0, "end")
                for subj in subjects:
                    menu.add_command(label=subj, command=tk._setit(subject_var, subj))

                canvas.delete("all")
                create_checklist(canvas, subjects, colors)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input error", "Subject already exists.")
    else:
        messagebox.showwarning("Input error", "Subject cannot be empty.")


def show_main_menu():
    for widget in main.winfo_children():
        widget.destroy()
    create_main_menu()
def todo_list():
    for widget in main.winfo_children():
        widget.destroy()
    file_path = r"todolist.opfile"
    subjects = read_todo_file(file_path)

    canvas = tk.Canvas(main, bg=colors[2], width=370, height=500)
    canvas.place(x=10, y=74)

    scrollbar = tk.Scrollbar(main, orient="vertical", command=canvas.yview)
    scrollbar.place(x=370, y=74, height=500)
    canvas.configure(yscrollcommand=scrollbar.set)

    if subjects:
        create_checklist(canvas, subjects, colors)
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
                       command=lambda: add_task(file_path, subjects, subject_var, entry1, option_menu, canvas))
    button1.place(x=228, y=168, width=115, height=80)

    frame2 = tk.Frame(master=main, bg=colors[2])
    frame2.place(x=409, y=99, width=370, height=170)

    entry2 = tk.Entry(master=frame2, bg=colors[2], fg="#000")
    entry2.place(x=41, y=61, width=121, height=42)

    button2 = tk.Button(master=frame2, text="Add Subject", bg=colors[1], fg="#000",
                       command=lambda: add_subject(file_path, subjects, entry2, option_menu, subject_var, canvas))
    button2.place(x=225, y=35, width=115, height=80)

    button3 = tk.Button(master=main, text="Back", bg=colors[1], fg="#000")
    button3.place(x=870, y=195, width=115, height=80)

    button = tk.Button(master=main, text="Daily Routine", bg=colors[1], fg="#000")
    button.place(x=870, y=394, width=115, height=80)


def text_editor():
    for widget in main.winfo_children():
        widget.destroy()

    Text = tk.Text(master=main)
    Text.config(bg=colors[2], fg="#000")
    Text.place(x=7, y=112, width=1000, height=460)

    button = tk.Button(master=main, text="Save")
    button.config(bg=colors[1], fg="#000")
    button.place(x=810, y=10, width=200, height=100)

    button1 = tk.Button(master=main, text="Back", command=show_main_menu)
    button1.config(bg=colors[1], fg="#000")
    button1.place(x=595, y=10, width=200, height=100)

    entry1 = tk.Entry(master=main)
    entry1.config(bg=colors[2], fg="#000")
    entry1.place(x=43, y=49, width=300, height=40)

def file_viewer():
    for widget in main.winfo_children():
        widget.destroy()

    frame = tk.Frame(master=main)
    frame.config(bg=colors[2])
    frame.place(x=53, y=91, width=913, height=452)

    button = tk.Button(master=main, text="Back", command=show_main_menu)
    button.config(bg=colors[1], fg="#000")
    button.place(x=783, y=7, width=141, height=68)

    label = tk.Label(master=main, text="Label")
    label.config(bg=colors[1], fg="#000")
    label.place(x=122, y=29, width=518, height=45)

def browser():
    for widget in main.winfo_children():
        widget.destroy()

    browser_frame = tk.Frame(master=main)
    browser_frame.config(bg=colors[2])
    browser_frame.place(x=21, y=75, width=955, height=500)

    button = tk.Button(master=main, text="Back", command=show_main_menu)
    button.config(bg=colors[1], fg="#000")
    button.place(x=860, y=15, width=85, height=50)

    button1 = tk.Button(master=main, text="Reset")
    button1.config(bg=colors[1], fg="#000")
    button1.place(x=755, y=15, width=85, height=50)

    entry = tk.Entry(master=main)
    entry.config(bg=colors[2], fg="#000")
    entry.place(x=92, y=24, width=511, height=39)

    button2 = tk.Button(master=main, text="Button")
    button2.config(bg=colors[1], fg="#000")
    button2.place(x=650, y=15, width=85, height=50)

    frame = tkinterweb.HtmlFrame(browser_frame)
    frame.load_website('https://google.com')
    frame.place(x=0, y=0, width=955, height=500)
def settings():
    for widget in main.winfo_children():
        widget.destroy()
    
    frame = tk.Frame(master=main)
    frame.config(bg=colors[2])
    frame.place(x=46, y=114, width=206, height=359)

    radio_button_var = tk.IntVar()

    radio_button_0 = tk.Radiobutton(master=frame, variable=radio_button_var, text="Option 1")
    radio_button_0.config(bg=colors[1], fg="#000", value=0)
    radio_button_0.place(x=38, y=24, width=120, height=30)

    radio_button_1 = tk.Radiobutton(master=frame, variable=radio_button_var, text="Option 2")
    radio_button_1.config(bg=colors[1], fg="#000", value=1)
    radio_button_1.place(x=41, y=66, width=120, height=30)

    button = tk.Button(master=main, text="New Palette")
    button.config(bg=colors[1], fg="#000")
    button.place(x=55, y=500, width=104, height=65)

    button1 = tk.Button(master=main, text="Save")
    button1.config(bg=colors[1], fg="#000")
    button1.place(x=173, y=500, width=80, height=65)

    label = tk.Label(master=main, text="Palettes")
    label.config(bg=colors[1], fg="#000")
    label.place(x=50, y=51, width=200,height=55)

    button = tk.Button(master=main, text="Back", command=show_main_menu)
    button.config(bg=colors[1], fg="#000")
    button.place(x=860, y=15, width=85, height=50)
    
    
def meshtastic():
    for widget in main.winfo_children():
        widget.destroy()

    messages = tk.Frame(master=main)
    messages.config(bg=colors[2])
    messages.place(x=25, y=73, width=950, height=444)

    button = tk.Button(master=main, text="Send")
    button.config(bg=colors[1], fg="#000")
    button.place(x=835, y=522, height=48)

    entry = tk.Entry(master=main)
    entry.config(bg=colors[2], fg="#000")
    entry.place(x=35, y=532, width=780, height=31)

    button1 = tk.Button(master=main, text="Back", command=show_main_menu)
    button1.config(bg=colors[1], fg="#000")
    button1.place(x=824, y=13, width=141, height=49)

def create_main_menu():
    # Load images
    text_editor_icon = tk.PhotoImage(file="icons/texteditoricon.png")
    file_viewer_icon = tk.PhotoImage(file="icons/foldericon.png")
    meshtastic_icon = tk.PhotoImage(file="icons/meshtasticicon.png")
    browser_icon = tk.PhotoImage(file="icons/browsericon.png")
    settings_icon = tk.PhotoImage(file="icons/gearicon.png")
    todolist_icon = tk.PhotoImage(file="icons/todolisticon.png")
    # Create buttons with images
    button = tk.Button(master=main, image=text_editor_icon, command=text_editor)
    button.config(bg=colors[1])
    button.place(x=44, y=60, width=200, height=200)

    button1 = tk.Button(master=main, image=file_viewer_icon, command=file_viewer)
    button1.config(bg=colors[1])
    button1.place(x=288, y=60, width=200, height=200)

    button2 = tk.Button(master=main, image=meshtastic_icon, command=meshtastic)
    button2.config(bg=colors[1])
    button2.place(x=532, y=60, width=200, height=200)

    button3 = tk.Button(master=main, image=browser_icon, command=lambda: browser())
    button3.config(bg=colors[1])
    button3.place(x=776, y=60, width=200, height=200)

    button4 = tk.Button(master=main, image=settings_icon, command=settings)
    button4.config(bg=colors[1])
    button4.place(x=44, y=330, width=200, height=200)
    
    button5 = tk.Button(master=main, image=todolist_icon, command=todo_list)
    button5.config(bg=colors[1])
    button5.place(x=288, y=330, width=200, height=200)
    buttons = [button, button1, button2, button3, button4, button5]
    for btn in buttons:
        btn.image = [text_editor_icon, file_viewer_icon, meshtastic_icon, browser_icon, settings_icon, todolist_icon]


create_main_menu()
main.mainloop()
