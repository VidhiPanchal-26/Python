from tkinter import *

root = Tk()
root.geometry("655x333")
root.title("Dance Academy Form")

def save():
    fp = open("form.txt" , "w")
    fp.write(f"Name: {name_value.get()}\n")
    fp.write(f"DOB: {dob_value.get()}\n")
    fp.write(f"Age: {age_value.get()}\n")
    fp.write(f"Contact: {contact_value.get()}\n\n")
    fp.close()

Label(text="Application Form" , font="Helvetica 15 bold" ,pady=10).grid(column=1)
full_name = Label(root , text="Full name: " , padx=8 , pady=3 ).grid()
dob = Label(root , text="DOB: ", padx=8 , pady=3).grid()
age = Label(root , text="Age: ", padx=8 , pady=3).grid()
contact = Label(root , text="Contact: ", padx=8 , pady=3).grid()

name_value = StringVar()
dob_value = StringVar()
age_value = StringVar()
contact_value = StringVar()

name_entry = Entry(root , textvariable=name_value).grid(row=1 , column=1)
dob_entry = Entry(root , textvariable=dob_value).grid(row=2 , column=1)
age_entry = Entry(root , textvariable=age_value).grid(row=3 , column=1)
contact_entry = Entry(root , textvariable=contact_value).grid(row=4 , column=1)

Button(text="Submit" , command=save ,padx=5 ,pady=5,border=2).grid(column=1)

root.mainloop()