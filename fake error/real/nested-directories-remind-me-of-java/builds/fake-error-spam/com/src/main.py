import tkinter as tk
import threading
import random
import winsound
import screeninfo
import time

start_time = time.time()
windows = 500   # The amount of "Error"s that will appear

def create_error():
    winsound.MessageBeep(winsound.MB_ICONHAND)  # Play Windows error sound

    screen = screeninfo.get_monitors()[0]  # Get primary screen size
    screen_width, screen_height = screen.width, screen.height

    root = tk.Tk()
    root.withdraw()

    # Create a pop-up error
    error = tk.Toplevel(root)
    error.title("Error")
    error.geometry(f"250x60+{random.randint(0, screen_width-300)}+{random.randint(0, screen_height-150)}")  # Spread all over screen

    tk.Label(error, text="An unexpected error has occurred!", fg="red", font=("Arial", 12)).pack(pady=20)
    #tk.Button(error, text="OK", command=error.destroy).pack()

    error.attributes('-topmost', True)  # Keep on top
    error.mainloop()

# Spam multiple error messages using threads
for _ in range(windows):
    threading.Thread(target=create_error, daemon=True).start()

while True:
    print(f"it took your pc: {time.time() - start_time} seconds to load {windows} error windows!")
    if input("> ").lower() == 'stop':
        break