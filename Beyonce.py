import tkinter as tk
from PIL import ImageTk, Image

def show_pic():
    image = Image.open("answer.png")
    root.photo = ImageTk.PhotoImage(image)
    w1.configure(image = root.photo)
    myButton.configure(text="WHAT?")

root = tk.Tk()
w1 = tk.Label(root)
w2 = tk.Label(root, justify=tk.LEFT , padx=50 ,pady=18 ,text="who run the world ?").pack(side="top")

myButton = tk.Button(root, text="Look at the answer ...", command=show_pic)
myButton.pack(side="top")
w1.pack(side="top")


root.mainloop()


