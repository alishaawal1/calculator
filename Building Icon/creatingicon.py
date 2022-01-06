from tkinter import*
from PIL import ImageTk,Image

root=Tk()
root.title("images")
root.iconbitmap('c:/Users/Python/flower.ico')

my_image=ImageTk.PhotoImage(Image.open("python/train.jfif"))

root.mainloop()