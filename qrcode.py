from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

# Create the root window
root = Tk()

# Function that generates the QR code
def command1():
    link_name = nameentry.get()
    link = linkentry.get()
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200, 450, window=image_label)

# Create a canvas for placing GUI elements
canvas = Canvas(root, width=400, height=500)
canvas.pack()

# Create a label for the application title
app_label = Label(root, text="QR Code Generator", fg="blue", font=("Arial", 30))
canvas.create_window(200, 50, window=app_label)

# Create labels and entry fields for link name and link
namelabel = Label(root, text="Link name")
link = Label(root, text="Link")
canvas.create_window(200, 100, window=namelabel)
canvas.create_window(200, 160, window=link)

nameentry = Entry(root)
linkentry = Entry(root)
canvas.create_window(200, 130, window=nameentry)
canvas.create_window(200, 180, window=linkentry)

# Create a button for generating the QR code
button = Button(text="Generate QR code", command=command1)
canvas.create_window(200, 230, window=button)

# Start the Tkinter event loop
root.mainloop()
