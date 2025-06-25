import os
import tkinter as tk
colors = ["#1a1f16", "#1e3f20", "#345830", "#4a7856", "#94ecbe"]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("Main Window")
main.config(bg=colors[1])
main.geometry("1024x600")

frame = tk.Frame(master=main)
frame.config(bg=colors[2])
frame.place(x=11, y=80, width=841, height=466)

check_box = tk.Checkbutton(master=frame, text="Checkbox")
check_box.config(bg=colors[1], fg="#000")

check_box.select()
check_box.place(x=32, y=39, width=120, height=30)

entry = tk.Entry(master=main)
entry.config(bg=colors[2], fg="#000")
entry.place(x=867, y=29, width=121, height=40)

button = tk.Button(master=main, text="Add Subject")
button.config(bg=colors[1], fg="#000")
button.place(x=870, y=85, width=115, height=80)

button1 = tk.Button(master=main, text="Daily Routine")
button1.config(bg=colors[1], fg="#000")
button1.place(x=870, y=394, width=115, height=80)

button2 = tk.Button(master=main, text="Back")
button2.config(bg=colors[1], fg="#000")
button2.place(x=870, y=496, width=115, height=80)

button3 = tk.Button(master=main, text="add task")
button3.config(bg=colors[1], fg="#000")
button3.place(x=870, y=303, width=115, height=80)

entry1 = tk.Entry(master=main)
entry1.config(bg=colors[2], fg="#000")
entry1.place(x=867, y=245, width=121, height=40)

option_menu_options = ["option 1"]
option_menu_var = tk.StringVar(value="Select option")
option_menu = tk.OptionMenu(main, option_menu_var, *option_menu_options)
option_menu.config(bg=colors[1], fg="#000")
option_menu.place(x=874, y=187)

main.mainloop()