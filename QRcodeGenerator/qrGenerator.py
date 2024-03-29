from tkinter import *
import pyqrcode
from PIL import ImageTk, Image
import png

root = Tk()


def generate():
    name = name_entry.get()
    link = link_entry.get()
    file_name = name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name, scale=5)
    QR = ImageTk.PhotoImage(Image.open(file_name))
    QR_label = Label(image=QR)
    QR_label.image = QR
    canvas.create_window(200, 400, window=QR_label)


canvas = Canvas(root, width=400, height=600)
canvas.pack()


app_label = Label(root, text="QR Code Generator",
                  fg="Blue", font=("Arial", 26))
canvas.create_window(200, 50, window=app_label)

name_label = Label(root, text="Link Name ")
link_label = Label(root, text="Link ")
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 190, window=link_entry)

button = Button(text="Generate QR code", command=generate)
canvas.create_window(200, 230, window=button)

root.mainloop()
