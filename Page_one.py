import tkinter as tk
import json
import os

def add_command():
    command = entry.get("1.0", "end-1c")  # Get the text from the Text widget
    if not command:
        return
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
    if command in data:
        result_label.config(text="Key already exists. Please enter a different command.", fg="red", font=("Helvetica", 12))
    else:
        data.setdefault(command, [])
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        result_label.config(text="Command added successfully!", fg="black", font=("Helvetica", 10))
        
        root.destroy()
        os.system('Page_two.py')

def task():
    root.destroy()
    os.system('task.py')
        
# Create the main window
root = tk.Tk()
root.title("B.A.B.Y")
root.geometry("300x300")

# Calculate the center of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (300 / 2))
y_coordinate = int((screen_height / 2) - (300 / 2))
root.geometry("+{}+{}".format(x_coordinate, y_coordinate))

# Create a label and entry for user input
tk.Label(root, text="Enter task name:").pack()
entry = tk.Text(root, height=2, width=30)
entry.pack()

# Create a button to trigger the command addition
add_button = tk.Button(root, text="Add Command", command=add_command, bg="yellow", width=25, height=2)
add_button.pack(pady=5)

# Create a button to show tasks
show_tasks_button = tk.Button(root, text="Show Tasks",command=task, bg="lightblue", width=25, height=2)
show_tasks_button.pack(pady=5)

# Create a label to show the result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
