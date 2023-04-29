import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.filedialog as fdialog
root = tk.Tk()
buffer = tk.Text(root)
root.title("EasyEditGUI")
def opencallback(textobj):
    filename = fdialog.askopenfilename()
    content = ""
    try:
        with open(filename) as readfile:
            content = readfile.read()
    except:
        msgbox.showerror("Error", "Cannot open a file")
    else:
        textobj.delete(1.0, tk.END)
        textobj.insert(1.0, content)
def savecallback(buffer):
    filename = fdialog.asksaveasfilename()
    try:
        with open(filename, mode='w') as savefile:
            savefile.write(buffer)
    except:
        msgbox.showerror("Error", "Cannot save to a file")
def aboutcallback():
    msgbox.showinfo("About", """
EasyEditGUI is a light, simple, cross-platform editor written by Python3.
Project Website:https://github.com/g1thubhack3r/EasyEditGUI
""")
def helpcallback():
    msgbox.showinfo("Help", """
Please contact me at 125267748+g1thubhack3r@users.noreply.github.com.
To report a bug, visit https://github.com/g1thubhack3r/EasyEditGUI/issues.
""")
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=False)
filemenu.add_command(label="Open", command=(lambda: opencallback(buffer)))
filemenu.add_command(label="Save As", command=(lambda: savecallback(buffer.get(1.0, tk.END))))
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="About", command=aboutcallback)
menubar.add_cascade(label="Help", command=helpcallback)
buffer.pack()
root.config(menu=menubar)
root.mainloop()
