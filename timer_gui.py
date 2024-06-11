import tkinter as tk
import time
import threading

initial_value = 1111
THRESHOLD = 10

def calc(value):
    return value + 1

def start_timer():
    start_time = time.time()
    start_button.config(state='disabled')

    def count_and_show_result():
        while True:
            elapsed_time = time.time() - start_time
            result_label.config(text=f"Elasped time: {elapsed_time:.2f} seconds")
            time.sleep(.01)
            if elapsed_time > THRESHOLD:
                break
        result = calc(initial_value)
        result_label.config(text=f"Result is: {result}")
        start_button.config(state='normal')

    threading.Thread(target=count_and_show_result).start()



root = tk.Tk()
root.title("Simple Timer GUI")
root.geometry("400x200")

start_button = tk.Button(root, text="Start", command=start_timer, font=("Helvetica", 20))
start_button.pack(pady=10)
result_label = tk.Label(root, text="Press the button to start", font=("Helvetica", 20))
result_label.pack(pady=10)

root.mainloop()
