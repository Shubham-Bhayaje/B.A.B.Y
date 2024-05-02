import json
import pyautogui
import keyboard
import time
import tkinter as tk


def get_input():
    global command
    command = entry.get()
    root.destroy()  # Close the window after getting input

# Create the main window
root = tk.Tk()
root.title("B.A.B.Y")

# Calculate the position to center the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - 300) // 2
y = (screen_height - 300) // 2

# Set the window size and position
root.geometry(f"300x300+{x}+{y}")

# Create a label
label = tk.Label(root, text="Select action:")
label.pack()

# Create an entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=15)



# Create a button to get user input
button = tk.Button(root, text="Run", command=get_input, bg="yellow",height=2, width=30)
button.pack()

root.mainloop()



# Define a dictionary to map special keys to their corresponding keyboard actions
special_keys_mapping = {
    'Key.enter': 'enter',
    'Key.backspace': 'backspace',
    'Key.tab': 'tab',
    'Key.space': 'space',
    'Key.esc': 'esc',
    'Key.up': 'up',
    'Key.down': 'down',
    'Key.left': 'left',
    'Key.right': 'right',
    'Key.shift': 'shift',
    'Key.ctrl': 'ctrl',
    'Key.alt': 'alt',
    'Key.caps_lock': 'caps_lock',
    'Key.delete': 'delete',
    'Key.home': 'home',
    'Key.end': 'end',
    'Key.page_up': 'page_up',
    'Key.page_down': 'page_down',
    'Key.insert': 'insert',
    'Key.f1': 'f1',
    'Key.f2': 'f2',
    'Key.f3': 'f3',
    'Key.f4': 'f4',
    'Key.f5': 'f5',
    'Key.f6': 'f6',
    'Key.f7': 'f7',
    'Key.f8': 'f8',
    'Key.f9': 'f9',
    'Key.f10': 'f10',
    'Key.f11': 'f11',
    'Key.f12': 'f12',
    'Key.media_play_pause': 'media_play_pause',
    'Key.media_stop': 'media_stop',
    'Key.media_previous': 'media_previous',
    'Key.media_next': 'media_next',
    'Key.media_volume_mute': 'volume_mute',
    'Key.media_volume_down': 'volume_down',
    'Key.media_volume_up': 'volume_up',
    'Key.media_select': 'media_select',
    'Key.print_screen': 'print_screen',
    'Key.scroll_lock': 'scroll_lock',
    'Key.pause': 'pause',
    'Key.num_lock': 'num_lock',
    'Key.menu': 'menu'
}

# Read data from JSON file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Extract actions from the list under the specified command
actions = data[command]

# Perform actions based on the extracted list of actions
for index, action in enumerate(actions[:-1]):
    if action.startswith('Mouse Click'):
        x, y = map(int, action.split(': ')[1][1:-1].split(','))
        print("Moving to coordinates:", x, y)
        pyautogui.moveTo(x, y, duration=1)
        pyautogui.click()
    elif action.startswith('Key Pressed'):
        key_pressed = action.split(': ')[1]
        print("Pressing key:", key_pressed)
        keyboard.press_and_release(key_pressed)
    elif action.startswith('Special Key Pressed'):
        key_pressed = action.split(': ')[1]
        if key_pressed in special_keys_mapping:
            print("Pressing special key:", key_pressed)
            keyboard.press_and_release(special_keys_mapping[key_pressed])
        else:
            print("Unknown special key:", key_pressed)
    else:
        print("Error: Unknown action format")
    time.sleep(1)

# Release all keys after all actions are executed

