import tkinter as tk
import threading
import time
import os
import psutil

# Define function1 to start Record_key.py process
def function1():
    os.system('python Record_key.py')

# Define function2 to stop Record_key.py process
def function2():
    print("ok")

# Dummy function3
def function3():
    os.system('move.py')

# Run function1 in a separate thread
def run_function1():
    thread = threading.Thread(target=function1)
    thread.start()

# Run function2 in a separate thread
def run_function2():
    thread = threading.Thread(target=function2)
    thread.start()

# Run function3 in a separate thread
def run_function3():
    thread = threading.Thread(target=function3)
    thread.start()

# Create the main window
root = tk.Tk()
root.title("B.A.B.Y")

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the coordinates to center the window
x = (screen_width - 300) // 2
y = (screen_height - 300) // 2

# Set window size to 300x300 and center it on the screen
root.geometry("300x300+{}+{}".format(x, y))

# Create buttons for each function with yellow background color and margin
button1 = tk.Button(root, text="Start", command=run_function1, bg="yellow", width=25, height=2)
button1.pack(pady=5)

label2 = tk.Label(root, text="To Stop/Save = Press Delete Button on Keybord", bg="yellow", width=40, height=3)
label2.pack(pady=5)

button3 = tk.Button(root, text="Run Task", command=run_function3, bg="yellow", width=25, height=2)
button3.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
