import os #if you want to save files
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import Menu

class NewWindow():
    def __init__(self,new_window,title):
        self.new_window = new_window
        new_window = Toplevel(window)
        new_window.title = self.title
        new_window.geometry("400x400")

def desc():
    
    
    new_window = Toplevel(window)
    new_window.title("New Window")
    new_window.geometry("400x400")
    label = Label(new_window, text="This Game is about a farming simulator")
    label.pack()

def tuto():
    pass

    

window = tk.Tk()
window.geometry("500x600")

menu_bar = Menu(window)
window.config(menu=menu_bar)

explaination_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="About",menu=explaination_menu)
explaination_menu.add_command(label="Description",command=desc)
explaination_menu.add_command(label="What to do?",command=None)
explaination_menu.add_command(label="Useful Tips",command=None)
explaination_menu.add_separator()
explaination_menu.add_command(label="Exit",command=window.quit())




img = Image.open("C:\\Users\\david\\OneDrive\\Desktop\\hotdog.png") #placeholder
photo = ImageTk.PhotoImage(img)

button = Button(window,
                
                image=photo

                )
button.pack()



window.mainloop()
