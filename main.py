import os
import tkinter as tk


colors = ["#1a1f16","#1e3f20","#345830","#4a7856","#94ecbe"]


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("SableOS")
main.config(bg=colors[0])
main.geometry("1024x600")




def show_main_menu():
    for widget in main.winfo_children():
        widget.destroy()
    create_main_menu()

    
def text_editor():
    for widget in main.winfo_children():
        widget.destroy()
    
    entry = tk.Entry(master=main)
    entry.config(bg=colors[2], fg="#000")
    entry.place(x=7, y=112, width=1000, height=460)

    button = tk.Button(master=main, text="save")
    button.config(bg=colors[1], fg="#000")
    button.place(x=810, y=10, width=200, height=100)

    button1 = tk.Button(master=main, text="Back",command=show_main_menu)
    button1.config(bg=colors[1], fg="#000")
    button1.place(x=595, y=10, width=200, height=100)

    entry1 = tk.Entry(master=main)
    entry1.config(bg=colors[2], fg="#000")
    entry1.place(x=43, y=49, width=300, height=40)
    
    
def file_viewer():
    for widget in main.winfo_children():
        widget.destroy()
    frame = tk.Frame(master=main)
    frame.config(bg=colors[0])
    frame.place(x=53, y=91, width=913, height=452)

    button = tk.Button(master=main, text="Back", command=show_main_menu)
    button.config(bg=colors[1], fg="#000")
    button.place(x=783, y=7, width=141, height=68)

    label = tk.Label(master=main, text="Label")
    label.config(bg=colors[1], fg="#000")
    label.place(x=122, y=29, width=518, height=45)
    
def create_main_menu():
    button = tk.Button(master=main, text="Text Editor", command=text_editor)
    button.config(bg=colors[1], fg="#000")
    button.place(x=32, y=60, width=200, height=200)

    button1 = tk.Button(master=main, text="File viewer", command=file_viewer)
    button1.config(bg=colors[1], fg="#000")
    button1.place(x=252, y=60, width=200, height=200)

    button2 = tk.Button(master=main, text="Button")
    button2.config(bg=colors[1], fg="#000")
    button2.place(x=472, y=60, width=200, height=200)

    button3 = tk.Button(master=main, text="Button")
    button3.config(bg=colors[1], fg="#000")
    button3.place(x=692, y=60, width=200, height=200)

    button4 = tk.Button(master=main, text="Button")
    button4.config(bg=colors[1], fg="#000")
    button4.place(x=32, y=330, width=200, height=200)

    

create_main_menu()

main.mainloop()