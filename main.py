import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *

# Function to filter log entries
def filter_logs():
    keyword = keyword_entry.get()
    level = level_var.get()
    
    log_display.delete(1.0, tk.END)  # Clear previous log entries
    
    with open(log_file, 'r') as file:
        for line in file:
            if keyword in line and (level == 'All' or level in line):
                log_display.insert(tk.END, line)
            elif keyword == 'Failed' and (level == 'All' or level in line):
                log_display.tag_config(background='red')
                log_display.insert(tk.END, line)

# Function to open a log file
def open_log_file():
    global log_file
    log_file = filedialog.askopenfilename(filetypes=[("Log Files", "*.log")])
    filter_logs()

# Create the main window
root = tk.Tk()
root.title("Log Viewer")

# Create a Frame for filters
filter_frame = ttk.LabelFrame(root, text="Filters")
filter_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Keyword filter
keyword_label = ttk.Label(filter_frame, text="Keyword:")
keyword_label.grid(row=0, column=0, padx=5, pady=5)
keyword_entry = ttk.Entry(filter_frame)
keyword_entry.grid(row=0, column=1, padx=5, pady=5)
keyword_entry.bind(root, lambda event=None: filter_logs())

# Log level filter
level_label = ttk.Label(filter_frame, text="Log Level:")
level_label.grid(row=1, column=0, padx=5, pady=5)
level_var = tk.StringVar()
level_var.set('All')
level_combobox = ttk.Combobox(filter_frame, textvariable=level_var, values=['All', 'INFO', 'WARNING', 'ERROR', 'CRITICAL', 'Failed'])
level_combobox.grid(row=1, column=1, padx=5, pady=5)
level_combobox.bind(root, lambda event=None: filter_logs())

# Filter button
filter_button = ttk.Button(filter_frame, text="Filter", command=filter_logs)
filter_button.grid(row=2, columnspan=2, padx=5, pady=10)

# Create a Text widget for displaying log entries
log_display = tk.Text(root, wrap=tk.WORD)
log_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Open log file button
open_button = ttk.Button(root, text="Open Log File", command=open_log_file)
open_button.pack(padx=10, pady=5)

# Main loop
root.mainloop()