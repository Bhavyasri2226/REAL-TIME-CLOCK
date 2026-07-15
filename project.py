import tkinter as tk
import time

# Function to update the clock
def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title("Real-Time Digital Clock")
root.geometry("400x200")
root.resizable(False, False)

# Clock Label
clock_label = tk.Label(
    root,
    font=("Arial", 40, "bold"),
    fg="blue"
)
clock_label.pack(expand=True)

# Start updating the clock
update_time()

# Run the application
root.mainloop()