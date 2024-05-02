import tkinter as tk
import json
import os

def back():
    root.destroy()
    os.system('Page_one.py')
def run():
    root.destroy()
    os.system('move.py')
class DictionaryGUI:
    def __init__(self, master):
        self.master = master
        master.title("B.A.B.Y")

        # Calculate the position to center the window
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width - 300) // 2
        y = (screen_height - 300) // 2

        # Set the window size and position
        master.geometry(f"300x300+{x}+{y}")

        self.label = tk.Label(master, text="Task List")
        self.label.pack()

        self.keys_text = tk.Text(master, height=10, width=50, font=("Arial", 12))
        self.keys_text.pack()

        self.load_dictionary()  # Automatically load dictionary when the app starts

        # Button to refresh the dictionary
        self.refresh_button = tk.Button(master, text="Run Task", command=run, width=30, bg="lightblue")
        self.refresh_button.pack(side=tk.TOP, padx=10, pady=5)  # Position the button at the top with some padding

        # Button to go back
        self.back_button = tk.Button(master, text="Back", command=back, width=30, bg="yellow")
        self.back_button.pack(side=tk.TOP, padx=10, pady=5)  # Position the button above the refresh button with some padding

    def load_dictionary(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                self.keys_text.delete('1.0', tk.END)  # Clear previous content
                keys = list(data.keys())
                for key in keys:
                    key_centered = key.center(50)  # Center the text within 50 characters
                    self.keys_text.insert(tk.END, key_centered + '\n')  # Insert key followed by a line break
                    self.keys_text.insert(tk.END, '-' * 50 + '\n')  # Insert a line of dashes
        except FileNotFoundError:
            self.keys_text.delete('1.0', tk.END)  # Clear previous content
            self.keys_text.insert(tk.END, "Error: File 'data.json' not found")

    def button_clicked(self):
        print("Button clicked!")

def main():
    global root
    root = tk.Tk()
    app = DictionaryGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
