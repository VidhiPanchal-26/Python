from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename , asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0 , END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt" , filetypes=[("All Files","*.*") , ("Text Documents" ,"*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+ "- Notepad")
        TextArea.delete(1.0 , END)
        f = open(file , "r")
        TextArea.insert(1.0 , f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file = asksaveasfilename(initialfile='Untitled.txt' , defaultextension=".txt" , filetypes=[("All Files","*.*") , ("Text Documents" ,"*.txt")])
        if file=="":
            file = None
        else:
            f = open(file , "w")
            f.write(TextArea.get(1.0 , END))
            f.close()

            root.title(os.path.basename(file)+ "- Notepad")
            
    else:
        f = open(file , "w")
        f.write(TextArea.get(1.0 , END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad" , "Notepad by Vidhi")

if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap(r"C:\Users\worth\OneDrive\Desktop\vidhi\my_python_projects\tkinter__tutorial\Notepad_project\note.ico")
    root.geometry("644x788")

    # Add Textarea
    TextArea = Text(root , font="lucida 13")
    TextArea.pack(expand=True , fill=BOTH)
    file = None

    # menu bar
    menuBar = Menu(root)

    #............File Menu............
    fileMenu = Menu(menuBar , tearoff=0)
    fileMenu.add_command(label="New" , command=newFile)    #open new file
    fileMenu.add_command(label="Open",  command=openFile)   #open existing file
    fileMenu.add_command(label="Save" , command=saveFile)    #save file
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit" , command=quitApp)
    menuBar.add_cascade(label="File" , menu=fileMenu) 

    #............Edit Menu...........
    editMenu = Menu(menuBar , tearoff=0)
    editMenu.add_command(label="Cut" , command=cut)
    editMenu.add_command(label="Copy" , command=copy)
    editMenu.add_command(label="Paste" , command=paste)
    menuBar.add_cascade(label="Edit" , menu=editMenu)
    
    #............Help Menu............
    helpMenu  = Menu(menuBar , tearoff=0)
    helpMenu.add_command(label="About" , command=about)
    menuBar.add_cascade(label="Help" , menu=helpMenu)

    root.config(menu=menuBar)

    scroll = Scrollbar(TextArea)
    scroll.pack(side=RIGHT , fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand = scroll.set)

    root.mainloop()
