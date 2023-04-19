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
        msgbox.showerror("Error", "File not found")
    else:
        textobj.delete(1.0, tk.END)
        textobj.insert(1.0, content)
def savecallback(buffer):
    filename = fdialog.asksaveasfilename()
    try:
        with open(filename, mode='w') as savefile:
            savefile.write(buffer)
    except:
        msgbox.showerror("Error", "File name invalid")
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=False)
filemenu.add_command(label="Open", command=(lambda: opencallback(buffer)))
filemenu.add_command(label="Save As", command=(lambda: savecallback(buffer.get(1.0, tk.END))))
menubar.add_cascade(label="File", menu=filemenu)
buffer.pack()
root.config(menu=menubar)
root.mainloop()
