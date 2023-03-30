#Copyright ©IndianGPT
#Hyperlink: https://www.linkedin.com/in/megnush/

#The above Python GUI tool, which includes the code to find missing series, is the intellectual property of ©IndianGPT. Any unauthorized reproduction, modification, or distribution of this tool, in whole or in part, is strictly prohibited without the written permission of ©IndianGPT.

#To use this tool, please contact ©IndianGPT at https://www.linkedin.com/in/megnush/.

import tkinter as tk
from tkinter import filedialog

app = tk.Tk()
app.title("Missing Series Finder")
app.geometry("300x200") # Set the size of the window
# Set the icon of the menu
app.iconbitmap('icon.ico')

def process_and_export():
    input_file_path = filedialog.askopenfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')], title='Select Input File')
    if not input_file_path:
        return

    with open(input_file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()]

    numbers.sort()

    missing_series_list = []

    for i in range(len(numbers) - 1):
        gap = numbers[i + 1] - numbers[i] - 1
        if gap > 0:
            missing_series_list.append((numbers[i], numbers[i] + 1, numbers[i + 1] - 1, gap))

    output_file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')], title='Save Output File (Summary)')
    if not output_file_path:
        return

    with open(output_file_path, 'w') as file:
        file.write("Start Series, From, To, Count, Remarks\n")
        for start_series, start, end, count in missing_series_list:
            if count <= 14:
                file.write(f"{start_series}, {start}, {end}, {count}, Found in Whitelist\n")

    all_missing_series_file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')], title='Save Output File (All Missing Series)')
    if not all_missing_series_file_path:
        return

    with open(all_missing_series_file_path, 'w') as file:
        file.write("Start Series, From, To, Count, Remarks\n")
        for start_series, start, end, count in missing_series_list:
            file.write(f"{start_series}, {start}, {end}, {count}, Found in Whitelist\n")

    missing_series_file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')], title='Save Output File (Missing Series)')
    if not missing_series_file_path:
        return

    with open(missing_series_file_path, 'w') as file:
        file.write("Series, Remarks\n")
        for start_series, start, end, count in missing_series_list:
            if count <= 12:
                for i in range(start, end + 1):
                    file.write(f"{i}, Not found in whitelist\n")

    found_series_file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')], title='Save Output File (Found Series)')
    if not found_series_file_path:
        return

    with open(found_series_file_path, 'w') as file:
        file.write("Series, Remarks\n")
        for number in numbers:
            file.write(f"{number}, Found in whitelist\n")

def open_linkedin(event):
    webbrowser.open_new(r"https://www.linkedin.com/in/megnush/")


process_export_button = tk.Button(app, text='Process and Export', command=process_and_export)
process_export_button.pack(pady=10)

copyright_label = tk.Label(app, text="Copyright 2023")
link_label = tk.Label(app, text="©IndianGPT", fg="Green", cursor="hand2")
link_label.bind("<Button-1>", open_linkedin)
link_label.pack(side="bottom")
copyright_label.pack(side="bottom")
process_export_button.pack(side="top")


# Packing the labels
copyright_label.pack()
link_label.pack()

app.mainloop()
