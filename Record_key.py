import json
import pyautogui
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyListener, Key
import tkinter as tk


with open('data.json', 'r') as json_file:
    data = json.load(json_file)

command = list(data.keys())[-1]  # Get the last key in the dictionary
recording = True  # Flag to control recording state


def on_click(x, y, button, pressed):
    global recording
    if button == button.left and pressed and recording:
        loc = 'Mouse Click: ({0}, {1})'.format(x, y)
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)

        # Step 2: Modify the specific key
        data[command].append(loc)

        # Step 3: Write the entire modified data back to the JSON file
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print('Mouse click recorded')


def on_press(key):
    global recording
    if recording:
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)

        try:
            char = key.char
            char_lo = 'Key Pressed: {0}'.format(char)
            data[command].append(char_lo)
            with open('data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
            print('Key press recorded')
        except AttributeError:
            special_key = str(key)
            special_key_loc = 'Special Key Pressed: {0}'.format(special_key)
            data[command].append(special_key_loc)
            with open('data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
            print('Special key press recorded')

        # Ensure writing to file immediately
        print('Data saved to data.json')

        if key == Key.delete:
            stop_recording()

        print('Data saved to data.json')


def stop_recording():
    global recording
    recording = False
    print("Recording stopped")


# Start listening for mouse events
with MouseListener(on_click=on_click) as listener:
    with KeyListener(on_press=on_press) as key_listener:
        listener.join()
        key_listener.join()
