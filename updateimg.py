import tkinter 
from PIL import Image, ImageTk 
 
im = Image.open('testplot.png')
 
root = tkinter.Tk()
tkimage = ImageTk.PhotoImage(im)
 
tkinter.Label(root, image=tkimage).pack()
 
def update_image():
    im = None
    tkimage = None
    tkinter.Label.destroy()
    im =Image.open('temp.png')
    tkimage =ImageTk.PhotoImage(im)
    tkinter.Label(root, image=tkimage).pack()
    root.geometry('%dx%d' % (im.size[0],im.size[1]))
    root.after(1000, update_image)
root.after(1000, update_image)
root.mainloop()
 
 