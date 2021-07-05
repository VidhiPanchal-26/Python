from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    #print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()

    elif text =="C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + str(text))
        screen.update()


root = Tk()
root.geometry("400x550")
root.minsize(400,550)
root.maxsize(400,550)
root.title("Calculator")
root.wm_iconbitmap(r"C:\Users\worth\OneDrive\Desktop\vidhi\my_python_projects\tkinter__tutorial\Calulator_Project\Calculator.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root , textvar=scvalue , font="lucida 14 bold")
screen.pack(fill=X , ipadx=8 , pady=10 , padx=10)

frame1 = Frame(root , bg="grey" )
num_keys = 9
while True:
    button1 = Button(frame1 , text=num_keys , padx=28 , pady=5 , font="lucida 19 bold")
    button1.pack(side=LEFT , padx=18 , pady=5)
    button1.bind("<Button-1>" , click)
    num_keys-=1
    if num_keys<7:
        break
frame1.pack()

frame2 = Frame(root , bg="grey")
while True:
    button2 = Button(frame2 , text=num_keys , padx=28 , pady=5 , font="lucida 19 bold")
    button2.pack(side=LEFT , padx=18 , pady=5)
    button2.bind("<Button-1>" , click)
    num_keys-=1
    if num_keys<4:
        break
frame2.pack()

frame3 = Frame(root , bg="grey")
while True:
    button3 = Button(frame3 , text=num_keys , padx=28 , pady=5 , font="lucida 19 bold")
    button3.pack(side=LEFT , padx=18 , pady=12)
    button3.bind("<Button-1>" , click)
    num_keys-=1
    if num_keys<1:
        break
frame3.pack()

frame4 = Frame(root , bg="grey")
num_keys = ["0" , "+" , "-" ]
for key in num_keys:
    button4 = Button(frame4 , text=key ,  padx=28.5 , pady=5 , font="lucida 19 bold")
    button4.pack(side=LEFT , padx=18 , pady=12)
    button4.bind("<Button-1>" , click)
frame4.pack()

frame5 = Frame(root , bg="grey")
num_keys = ["*" , "/" , "=" ]
for key in num_keys:
    button5 = Button(frame5 , text=key ,  padx=29.5, pady=5 , font="lucida 19 bold")
    button5.pack(side=LEFT , padx=18 , pady=12)
    button5.bind("<Button-1>" , click)
frame5.pack()

frame6 = Frame(root , bg="grey")
num_keys = ["%" , "." , "C"]
for key in num_keys:
    button6 = Button(frame6 , text=key ,  padx=28 , pady=5 , font="lucida 19 bold")
    button6.pack(side=LEFT , padx=18 , pady=12)
    button6.bind("<Button-1>" , click)
frame6.pack()

root.mainloop()