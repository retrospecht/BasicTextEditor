from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Text Editor")

text = Text(root)
text.grid()

def saveas():
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if savelocation:
        with open(savelocation, "w+", encoding="utf-8") as file1:
            file1.write(t)

button = Button(root, text="Save", command=saveas)
button.grid()
button.config(width=10, height=2)

font = Menubutton(root, text="Font")
font.grid()

font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu

font_choice = StringVar(value="Courier")

def set_font():
    text.config(font=font_choice.get())

font.menu.add_radiobutton(label="Courier", variable=font_choice, value="Courier", command=set_font)
font.menu.add_radiobutton(label="Helvetica", variable=font_choice, value="Helvetica", command=set_font)
font.menu.add_radiobutton(label="Times", variable=font_choice, value="Times", command=set_font)
font.menu.add_radiobutton(label="Arial", variable=font_choice, value="Arial", command=set_font)

root.mainloop()

