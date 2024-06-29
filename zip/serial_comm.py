import tkinter as tk
from tkinter import filedialog, Menu, messagebox
import os
import ttkbootstrap as ttk

window = ttk.Window(themename='darkly')
window.geometry('715x600')
window.title('Serial Communication')

window.minsize(715, 600)  # Set minimum window size
window.maxsize(800, 600)  # Set maximum window size

# Creating rows and columns
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# Frame for Logo and Heading
logo_heading_frame = ttk.Frame(window)
logo_heading_frame.grid(row=0, column=0, sticky='nw')

# Logo
logo_image = tk.PhotoImage(file='LOGO.png')
logo_label = ttk.Label(logo_heading_frame, image=logo_image)
logo_label.grid(row=0, column=0, padx=10, pady=10)

# Heading
heading_label = ttk.Label(logo_heading_frame, text='Communication & Computation', font=('Arial', 18, 'bold'))
heading_label.grid(row=0, column=1, padx=10, pady=10)

# Tabs
tabs = ttk.Notebook(window)
tabs.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

# Tab 1: Transfer
transfer_tab = ttk.Frame(tabs)
tabs.add(transfer_tab, text='Transfer')

file_label = ttk.Label(transfer_tab, text='Selected File: ')
file_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

file_name_label = ttk.Label(transfer_tab, text='No file selected')
file_name_label.grid(row=0, column=1, padx=10, pady=10, sticky='w')

progress_bar = ttk.Progressbar(transfer_tab, mode='determinate', length=400)
progress_bar.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

select_button = ttk.Button(transfer_tab, text='Select File', command=lambda: select_file())
select_button.grid(row=1, column=0, padx=10, pady=10)

deselect_button = ttk.Button(transfer_tab, text='Deselect File', state='disabled', command=lambda: deselect_file())
deselect_button.grid(row=3, column=0, padx=10, pady=10)

compute_button = ttk.Button(transfer_tab, text='Compute')
compute_button.grid(row=3, column=2, padx=10, pady=10)

# Frame for Configure button and Port menu
configure_frame = ttk.Frame(transfer_tab)
configure_frame.grid(row=2, column=2, padx=10, pady=10, sticky='e')

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_name = os.path.basename(file_path)
        file_name_label.config(text=file_name)
        deselect_button.config(state='normal')
        simulate_file_loading()

def simulate_file_loading():
    progress = 0
    select_button.config(state='disabled')  # Disable select button during file loading
    while progress < 100:
        progress_bar['value'] = progress
        window.update_idletasks()
        progress += 10
        window.after(500)  # Simulating delay
    progress_bar['value'] = 100
    select_button.config(state='normal')  # Enable select button after file loading

def deselect_file():
    file_name_label.config(text='No file selected')
    progress_bar['value'] = 0

def select_port(port):
    selected_port.set(port)
    messagebox.showinfo('Selected Port', f"You selected {port}")

def open_configure_window():
    configure_window = tk.Toplevel(window)
    configure_window.title('Configure')
    configure_window.geometry('650x380')
    configure_window.minsize(650, 375)
    configure_window.maxsize(650, 375)

    # "Please do necessary configurations here" label
    config_label = ttk.Label(configure_window, text="Please do necessary configurations here")
    config_label.grid(row=0, column=0, padx=10, pady=10)

    # Create a border around the frame
    border_frame = ttk.Frame(configure_window, relief='solid', borderwidth=1)
    border_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    # Frame for Port menu
    port_frame = ttk.Frame(border_frame, borderwidth=2, relief='solid')
    port_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    # Create a "Port" menu
    label = ttk.Label(port_frame, text="Please select a Port")
    label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    port_menu = Menu(port_frame, tearoff=0)

    # Add menu items to the "Port" menu
    ports = ['COM1', 'COM2', 'COM3', 'COM4']
    for port in ports:
        port_menu.add_command(label=port, command=lambda p=port: select_port(p))

    # Create a label for the menu
    port_label = ttk.Label(port_frame, text='Port:', font=('Arial', 14))
    port_label.grid(row=0, column=1, padx=10, pady=10, sticky='e')

    # Create a button to display the menu
    port_button = ttk.Menubutton(port_frame, textvariable=selected_port, menu=port_menu)
    port_button.grid(row=0, column=2, padx=10, pady=10, sticky='w')

    # Label for "Configure Parameters"
    configure_params_label = ttk.Label(border_frame, text="Configure Parameters:")
    configure_params_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')

    # Label and Entry for "BaudRate"
    baud_rate_label = ttk.Label(border_frame, text="BaudRate:")
    baud_rate_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
    baud_rate_entry = ttk.Entry(border_frame)
    baud_rate_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')

    # Label and Entry for "Byte size"
    byte_size_label = ttk.Label(border_frame, text="Byte size:")
    byte_size_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')
    byte_size_entry = ttk.Entry(border_frame)
    byte_size_entry.grid(row=3, column=1, padx=10, pady=5, sticky='w')

    # Label and Radio Buttons for "StopBits"
    stop_bits_label = ttk.Label(border_frame, text="StopBits:")
    stop_bits_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')
    stop_bits_frame = ttk.Frame(border_frame)
    stop_bits_frame.grid(row=4, column=1, padx=10, pady=5, sticky='w')
    stop_bits_var = tk.StringVar()

    one_stop_radio = ttk.Radiobutton(stop_bits_frame, text="ONE STOP", variable=stop_bits_var, value="1")
    one_stop_radio.grid(row=0, column=0, padx=5, pady=5)
    no_stop_radio = ttk.Radiobutton(stop_bits_frame, text="ONE 5 STOPBITS", variable=stop_bits_var, value="0")
    no_stop_radio.grid(row=0, column=1, padx=5, pady=5)

    # Label and Radio Buttons for "Parity"
    parity_label = ttk.Label(border_frame, text="Parity:")
    parity_label.grid(row=5, column=0, padx=10, pady=5, sticky='w')
    parity_frame = ttk.Frame(border_frame)
    parity_frame.grid(row=5, column=1, padx=10, pady=5, sticky='w')
    parity_var = tk.StringVar()

    no_parity_radio = ttk.Radiobutton(parity_frame, text="NO PARITY", variable=parity_var, value="None")
    no_parity_radio.grid(row=0, column=0, padx=5, pady=5)
    yes_parity_radio = ttk.Radiobutton(parity_frame, text="ODD PARITY", variable=parity_var, value="Even")
    yes_parity_radio.grid(row=0, column=1, padx=5, pady=5)


# Configure button
configure_button = ttk.Button(configure_frame, text='Configure', command=open_configure_window)
configure_button.pack()

# Tab 2: Compare
compare_tab = ttk.Frame(tabs)
tabs.add(compare_tab, text='Compare')

# "Please select the two files" label
select_files_label = ttk.Label(compare_tab, text='Please select the two files')
select_files_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# File 1 widgets
file1_label = ttk.Label(compare_tab, text='File 1:')
file1_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')

file1_name_label = ttk.Label(compare_tab, text='No file selected')
file1_name_label.grid(row=1, column=1, padx=10, pady=5, sticky='w')

file1_progress_bar = ttk.Progressbar(compare_tab, mode='determinate', length=400)
file1_progress_bar.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky='w')

file1_select_button = ttk.Button(compare_tab, text='Select File 1', command=lambda: select_file1())
file1_select_button.grid(row=3, column=0, padx=10, pady=5, sticky='w')

file1_deselect_button = ttk.Button(compare_tab, text='Deselect File 1', state='disabled', command=lambda: deselect_file1())
file1_deselect_button.grid(row=3, column=1, padx=10, pady=5, sticky='w')

# File 2 widgets
file2_label = ttk.Label(compare_tab, text='File 2:')
file2_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')

file2_name_label = ttk.Label(compare_tab, text='No file selected')
file2_name_label.grid(row=4, column=1, padx=10, pady=5, sticky='w')

file2_progress_bar = ttk.Progressbar(compare_tab, mode='determinate', length=400)
file2_progress_bar.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky='w')

file2_select_button = ttk.Button(compare_tab, text='Select File 2', command=lambda: select_file2())
file2_select_button.grid(row=6, column=0, padx=10, pady=5, sticky='w')

file2_deselect_button = ttk.Button(compare_tab, text='Deselect File 2', state='disabled', command=lambda: deselect_file2())
file2_deselect_button.grid(row=6, column=1, padx=10, pady=5, sticky='w')

# Compare button
compare_button = ttk.Button(compare_tab, text='Compare')
compare_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Functions for selecting and deselecting files
def select_file1():
    file1_path = filedialog.askopenfilename()
    if file1_path:
        file1_name = os.path.basename(file1_path)
        file1_name_label.config(text=file1_name)
        file1_deselect_button.config(state='normal')
        simulate_file1_loading()

def select_file2():
    file2_path = filedialog.askopenfilename()
    if file2_path:
        file2_name = os.path.basename(file2_path)
        file2_name_label.config(text=file2_name)
        file2_deselect_button.config(state='normal')
        simulate_file2_loading()

def simulate_file1_loading():
    progress = 0
    file1_select_button.config(state='disabled')  # Disable select button during file loading
    while progress < 100:
        file1_progress_bar['value'] = progress
        window.update_idletasks()
        progress += 10
        window.after(500)  # Simulating delay
    file1_progress_bar['value'] = 100
    file1_select_button.config(state='normal')  # Enable select button after file loading

def simulate_file2_loading():
    progress = 0
    file2_select_button.config(state='disabled')  # Disable select button during file loading
    while progress < 100:
        file2_progress_bar['value'] = progress
        window.update_idletasks()
        progress += 10
        window.after(500)  # Simulating delay
    file2_progress_bar['value'] = 100
    file2_select_button.config(state='normal')  # Enable select button after file loading

def deselect_file1():
    file1_name_label.config(text='No file selected')
    file1_progress_bar['value'] = 0
    file1_deselect_button.config(state='disabled')

def deselect_file2():
    file2_name_label.config(text='No file selected')
    file2_progress_bar['value'] = 0
    file2_deselect_button.config(state='disabled')


# Tab 3: Compute
compute_tab = ttk.Frame(tabs)
tabs.add(compute_tab, text='Compute')

# "Compute Checksum" label
compute_label = ttk.Label(compute_tab, text='Compute Checksum')
compute_label.grid(row=0, column=0, padx=10, pady=10)

# File widgets
file_label = ttk.Label(compute_tab, text='Selected File: ')
file_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')

file_name_label = ttk.Label(compute_tab, text='No file selected')
file_name_label.grid(row=1, column=1, padx=10, pady=10, sticky='w')

progress_bar = ttk.Progressbar(compute_tab, mode='determinate', length=400)
progress_bar.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

select_button = ttk.Button(compute_tab, text='Select File', command=lambda: select_file())
select_button.grid(row=3, column=0, padx=10, pady=10)

deselect_button = ttk.Button(compute_tab, text='Deselect File', state='disabled', command=lambda: deselect_file())
deselect_button.grid(row=3, column=1, padx=10, pady=10)

compute_button = ttk.Button(compute_tab, text='Compute')
compute_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Transfer button
transfer_button = ttk.Button(transfer_tab, text='Transfer')
transfer_button.grid(row=4, column=1, padx=10, pady=10)

selected_port = tk.StringVar()

window.mainloop()
