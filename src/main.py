from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

# file ar function


def new_file():
    global file
    root.title("Untitled-Notepad")
    file = None
    text_area.delete(1.0, END)           


def open_file():
    global file
    file = askopenfilename(defaultextension=".text", filetypes=[("All Files", "*.*"), ("Text Documents", "*.text")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        text_area.delete(1.0, END)
        f = open(file, "r")
        text_area.insert(1.0, f.read())
        f.close()


def save_file():
    global file
    if file == None :
        file= asksaveasfilename(initialfile="Untitled.text", defaultextension=".text", filetypes=[("All Files", "*.*"), ("Text Documents", "*.text")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(text_area.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
    else:
        f = open(file, "w")
        f.write(text_area.get(1.0, END))
        f.close()




def saveas_file():
    global file

    file = asksaveasfilename(initialfile="Untitled.text", defaultextension=".text",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.text")])
    f = open(file, "w")
    f.write(text_area.get(1.0, END))
    f.close()


def exit_file():
    root.destroy()


# edit ar function

def cut_edit():
    text_area.event_generate("<<Cut>>")


def copy_edit():
    text_area.event_generate("<<Copy>>")


def paste_edit():
    text_area.event_generate("<<Paste>>")


def selectall_edit():
    text_area.event_generate("<<SelectAll>>")


# help ar function


def help_article_help():
    t1 = Toplevel()
    t1.title("Help Article")
    article = """You can use it for makeing your important file.You can make HTML file. Do you want to know, How to use it?
                Please, search on Google. Write how to use notepad on the Google search bar. Yow will have seen  
                many article about notepad. You can also use Youtube for the solution of your problem"""
    msg = Label(t1, text=article, height=15, font="lucida 12" )
    msg.pack(fill=BOTH)


def aboutnotepad_help():
    tkinter.messagebox.showinfo("About notepad", "It is created by Nafis Iqbal")

# rateus ar funtion

def rateus_rateus():
    tkinter.messagebox.askyesno("Rateus_Notify", "Do you want to Rateus?")
    if YES==True:
        tkinter.messagebox.showinfo("Gredding", "Thanks for want to rate us,Please,rate us in online.\n Do you want?")




# software window
root = Tk()
# software title
root.title("Untitled-Notepad")
#root.wm_iconbitmap("write herw the currect path of icon")
root.geometry("835x520")
# add a label
label = Label(text="Created By Nafis Iqbal", bg="powder blue")
label.pack(side=BOTTOM, fill=X)
# add text area
text_area = Text(root, font="lucida 16", undo=TRUE)
file = None
text_area.pack(expand=True, fill=BOTH)
# add scroll bar
scrollbar = Scrollbar(text_area, cursor="arrow")
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=text_area.yview)
text_area.config(yscrollcommand=scrollbar.set)
# add menu
menubar = Menu(root)
# add file menu and sub menu in file
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save as", command=saveas_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_file)
menubar.add_cascade(label="File", menu=filemenu)
# add_edit_menu_and_sub_menu_in_edit
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=text_area.edit_undo)
editmenu.add_command(label="Redo", command=text_area.edit_redo)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=cut_edit)
editmenu.add_command(label="Copy", command=copy_edit)
editmenu.add_command(label="Paste", command=paste_edit)
editmenu.add_separator()
editmenu.add_command(label="Select All", command=selectall_edit)
menubar.add_cascade(label="Edit", menu=editmenu)
# add help menu and sub menu in help
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Article", command=help_article_help)
helpmenu.add_separator()
helpmenu.add_command(label="About Notepad", command= aboutnotepad_help)
menubar.add_cascade(label="Help", menu=helpmenu)
# rateus menu and rateus way in rate us
rateusmenu = Menu(menubar, tearoff=0)
rateusmenu.add_command(label="Rateus", command=rateus_rateus)
menubar.add_cascade(label="Rateus", menu=rateusmenu)
# showing menubar
root.config(menu=menubar)
# software loop
root.mainloop()
