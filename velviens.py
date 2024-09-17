from tests import Human, Woman
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

visi_cilveki = []

# root window
root = tk.Tk()
root.title('Temperature Converter')
root.geometry('300x300')
root.resizable(False, False)


# def fahrenheit_to_celsius(f):
#     """ Convert fahrenheit to celsius
#     """
#     return (f - 32) * 5/9


# frame
frame = ttk.Frame(root)


# field options
options = {'padx': 5, 'pady': 5}

# temperature label
#temperature_label = ttk.Label(frame, text='Fahrenheit')
#temperature_label.grid(column=0, row=0, sticky='W', **options)

# temperature entry
#temperature = tk.StringVar()
#temperature_entry = ttk.Entry(frame, textvariable=temperature)
#temperature_entry.grid(column=1, row=0, **options)
#temperature_entry.focus()
# vards label
vards_label = ttk.Label(frame, text="vards")
vards_label.grid(column=0, row=0, sticky="W",**options)
# dzimums label
dzimums_label = ttk.Label(frame, text="dzimums")
dzimums_label.grid(column=0,row=1, sticky="W",**options)
# vecums label
vecums_label = ttk.Label(frame, text="vecums")
vecums_label.grid(column=0,row=2, sticky="W",**options)
# vards entry
vards = tk.StringVar()
vards_entry = ttk.Entry(frame,textvariable=vards)
vards_entry.grid(column=1, row=0,**options)
vards_entry.focus()
#dzimums entry
dzimums = tk.StringVar()
dzimums_entry = ttk.Entry(frame, textvariable=dzimums)
dzimums_entry.grid(column=1,row=1, **options)
#vecums entry
vecums = tk.StringVar()
vecums_entry = ttk.Entry(frame, textvariable=vecums)
vecums_entry.grid(column=1,row=2, **options)
vecums_entry.focus()
# ražošana button

def razot_button_clicked():
    cilveku_vards = vards.get()
    cilveku_dzimums = dzimums.get()
    cilveku_vecums = vecums.get()
    visi_cilveki.append(Human(cilveku_vards,cilveku_vecums,cilveku_dzimums))
    result_label.config(text=(cilveku_vards, cilveku_dzimums,cilveku_vecums))


razot_button = ttk.Button(frame, text="Veidot")
razot_button.grid(column=3, row=0, sticky="W",**options)
razot_button.configure(command=razot_button_clicked)

# button label
result_label = ttk.Label(frame)
result_label.grid(row=3, columnspan=3, **options)

# convert button



# def convert_button_clicked():
#     """  Handle convert button click event 
#     """
#     try:
#         f = float(temperature.get())
#         c = fahrenheit_to_celsius(f)
#         result = f'{f} Fahrenheit = {c:.2f} Celsius'
#         result_label.config(text=result)
#     except ValueError as error:
#         showerror(title='Error', message=error)


# convert_button = ttk.Button(frame, text='Convert')
# convert_button.grid(column=2, row=0, sticky='W', **options)
# convert_button.configure(command=convert_button_clicked)

# result label
#result_label = ttk.Label(frame)
#result_label.grid(row=3, columnspan=3, **options)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)


# start the app
root.mainloop()

