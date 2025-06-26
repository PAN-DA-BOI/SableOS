import os
from PIL import Image, ImageTk
import tkinter as tk
import json
from tkinter import ttk
import tkinterweb
from support import read_todo_file, write_subject_to_file, write_task_to_file, create_checklist, add_daily_tasks_to_file, remove_task_from_file
colors = ["#1a1f16", "#1e3f20", "#345830", "#4a7856", "#94ecbe"]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("SableOS")
main.config(bg=colors[0])
main.geometry("1024x600")
def load_palettes():
    palettes = {}
    palette_dir = "coolors"
    for filename in os.listdir(palette_dir):
        if filename.endswith(".coolor"):
            with open(os.path.join(palette_dir, filename), 'r') as file:
                palette = json.load(file)
                palette_name = os.path.splitext(filename)[0]
                palettes[palette_name] = palette
    return palettes
def save_file():
    # Get the file name from entry1
    file_name = entry1.get()

    # Check if the file name is not empty
    if not file_name:
        print("Error", "File name cannot be empty!")
        return

    # Get the content from the Text widget
    content = Text.get("1.0", tk.END)

    # Write the content to the file
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print.showinfo("Success", "File saved successfully!")
    except Exception as e:
        print("Error", f"An error occurred while saving the file: {e}")
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
            print("Error", str(e))
    else:
        print("Input error", "Subject and task cannot be empty.")
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
                print("Error", str(e))
        else:
            print("Input error", "Subject already exists.")
    else:
        print("Input error", "Subject cannot be empty.")
def add_daily_tasks(file_path, canvas):
    try:
        add_daily_tasks_to_file(r"daily.opfile", file_path)
        subjects = read_todo_file(file_path)
        canvas.delete("all")
        create_checklist(canvas, subjects, colors)
    except Exception as e:
        print("Error", str(e))
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
    if subjects:
        subject_var.set(next(iter(subjects)))
    else:
        subject_var.set("")

    # Ensure subjects is a list of strings
    subject_list = list(subjects.keys()) if subjects else [""]
    option_menu = tk.OptionMenu(frame1, subject_var, *subject_list)
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

    button3 = tk.Button(master=main, text="Back", bg=colors[1], fg="#000", command=show_main_menu)
    button3.place(x=870, y=195, width=115, height=80)

    button = tk.Button(master=main, text="Daily Routine", bg=colors[1], fg="#000",
                       command=lambda: add_daily_tasks(file_path, canvas))
    button.place(x=870, y=394, width=115, height=80)

    main.mainloop()
def text_editor():
    for widget in main.winfo_children():
        widget.destroy()
    global Text, entry1
    Text = tk.Text(master=main)
    Text.config(bg=colors[2], fg="#000")
    Text.place(x=7, y=112, width=1000, height=460)

    button = tk.Button(master=main, text="Save", command=save_file)
    button.config(bg=colors[1], fg="#000")
    button.place(x=810, y=10, width=200, height=100)

    button1 = tk.Button(master=main, text="Back", command=show_main_menu)
    button1.config(bg=colors[1], fg="#000")
    button1.place(x=595, y=10, width=200, height=100)

    entry1 = tk.Entry(master=main)
    entry1.config(bg=colors[2], fg="#000")
    entry1.place(x=43, y=49, width=300, height=40)
def file_viewer(directory="."):
    for widget in main.winfo_children():
        widget.destroy()

    frame = tk.Frame(master=main)
    frame.config(bg=colors[2])
    frame.place(x=53, y=91, width=913, height=452)

    button = tk.Button(master=main, text="Back", command=show_main_menu)
    button.config(bg=colors[1], fg="#000")
    button.place(x=783, y=7, width=141, height=68)

    label = tk.Label(master=main, text=f"Viewing: {directory}")
    label.config(bg=colors[1], fg="#000")
    label.place(x=122, y=29, width=518, height=45)

    # Load icons
    folder_icon = ImageTk.PhotoImage(Image.open("icons/foldericon.png").resize((50, 50)))
    file_icon = ImageTk.PhotoImage(Image.open("icons/fileicon.png").resize((50, 50)))

    # Iterate over the directory contents
    for index, item in enumerate(os.listdir(directory)):
        item_path = os.path.join(directory, item)
        is_directory = os.path.isdir(item_path)

        # Create a frame for each item
        item_frame = tk.Frame(frame)
        item_frame.config(bg=colors[2])
        item_frame.grid(row=index // 5, column=index % 5, padx=10, pady=10)

        # Display icon
        icon_label = tk.Label(item_frame, image=folder_icon if is_directory else file_icon, bg=colors[2])
        icon_label.image = folder_icon if is_directory else file_icon  # Keep a reference

        # Bind the click event to folder icons
        if is_directory:
            icon_label.bind("<Button-1>", lambda e, path=item_path: on_folder_click(path))

        icon_label.pack()

        # Display name
        name_label = tk.Label(item_frame, text=item, bg=colors[2], fg="#000")
        name_label.pack()
def on_folder_click(folder_path):
    file_viewer(directory=folder_path)
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

    palettes = load_palettes()

    # Create a scrollable frame
    canvas = tk.Canvas(main, bg=colors[2])
    scrollbar = ttk.Scrollbar(main, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas, style="Background.TFrame")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.place(x=46, y=114, width=800, height=359)
    scrollbar.place(x=846, y=114, height=359)

    radio_button_var = tk.StringVar(value=json.dumps(colors))

    for idx, (name, palette) in enumerate(palettes.items()):
        row, col = divmod(idx, 4)
        radio_button = tk.Radiobutton(
            master=scrollable_frame,
            variable=radio_button_var,
            text=name,
            value=json.dumps(palette),
            bg=colors[1],
            fg="#000"
        )
        radio_button.grid(row=row, column=col, padx=10, pady=10, sticky="w")

    def save_settings():
        global colors
        selected_palette = json.loads(radio_button_var.get())
        colors = selected_palette
        main.config(bg=colors[1])  # Update the root window background
        settings()  # Reload settings to apply new colors

    button1 = tk.Button(master=main, text="Save", command=save_settings, bg=colors[1], fg="#000")
    button1.place(x=173, y=500, width=80, height=65)

    label = tk.Label(master=main, text="Palettes", bg=colors[1], fg="#000")
    label.place(x=50, y=51, width=200, height=55)

    button = tk.Button(master=main, text="Back", command=show_main_menu, bg=colors[1], fg="#000")
    button.place(x=860, y=15, width=85, height=50)
def on_message_received(message):
    messages_text.insert(tk.END, f"Received: {message['text']}\n")

def send_message():
    message = entry.get()
    if message:
        interface.sendText(message, destinationId=None, wantResponse=False, wantAck=False)
        messages_text.insert(tk.END, f"Sent: {message}\n")
        entry.delete(0, tk.END)

def meshtastic():
    for widget in main.winfo_children():
        widget.destroy()

    global messages_text, entry, interface

    messages_frame = tk.Frame(master=main)
    messages_frame.config(bg=colors[2])
    messages_frame.place(x=25, y=73, width=950, height=444)

    messages_text = tk.Text(messages_frame, wrap=tk.WORD, bg=colors[2], fg="#000")
    messages_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(messages_frame, command=messages_text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    messages_text.config(yscrollcommand=scrollbar.set)

    button = tk.Button(master=main, text="Send", command=send_message, bg=colors[1], fg="#000")
    button.place(x=835, y=522, height=48)

    entry = tk.Entry(master=main)
    entry.config(bg=colors[2], fg="#000")
    entry.place(x=35, y=532, width=780, height=31)

    button1 = tk.Button(master=main, text="Back", command=show_main_menu, bg=colors[1], fg="#000")
    button1.place(x=824, y=13, width=141, height=49)

    # Initialize Meshtastic interface
    interface = serial_interface.SerialInterface()
    pub.subscribe(on_message_received, "meshtastic.receive.text")
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
