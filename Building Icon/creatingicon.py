from tkinter import *
from PIL import Image, ImageTk
window = Tk()
window.geometry("500x500")
image1 = ImageTk.PhotoImage(Image.open("python/image1.jpg").resize((500,500)))
image2 = ImageTk.PhotoImage(Image.open("python/image2.jpg").resize((500,500)))
image3 = ImageTk.PhotoImage(Image.open("python/image3.jpg").resize((500,500)))
image4 = ImageTk.PhotoImage(Image.open("python/image4.jpg").resize((500,500)))
image5 = ImageTk.PhotoImage(Image.open("python/image5.jpg").resize((500,500)))

count = 1
label = Label()
label.pack()

def show():
    if count == 1:
        label.config(image=image1)
    elif count == 2:
        label.config(image=image2)
    elif count == 3:
        label.config(image=image3)
    elif count == 4:
        label.config(image=image4)
    elif count == 5:
        label.config(image=image5)
    else:
        print()
        
def Previous():
    global count
    count  = count - 1
    if count >= 5:
        nex['state']='disabled'
    else:
        nex['state']='normal'
    if count <= 1:
        pre['state']='disabled'
    else:
        pre['state']='normal'
    print(count)
    show()
    
def Next():
    global count
    count  = count + 1
    if count >= 5:
        nex['state']='disabled'
    else:
        nex['state']='normal'
    if count <= 1:
        pre['state']='disabled'
    else:
        pre['state']='normal'
    print(count)
    show()
    
pre = Button(window,text="Previous",command=Previous,)
pre.place(x = 0,y = 480)
nex = Button(window,text="Next",command=Next)
nex.place(x = 460,y = 480)
exi = Button(window,text="Exit",command=window.quit)
exi.place(x = 230,y=480)

if count >= 5:
    nex['state'] = 'disabled'
else:
    nex['state'] = 'normal'
if count <= 1:
    pre['state'] = 'disabled'
else:
    pre['state'] = 'normal'
show()

window.mainloop()