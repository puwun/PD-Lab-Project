from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import subprocess

def run_game1():
    try:
        subprocess.run(['python', r'C:\Users\ASUS\pavan^^\PycharmProjects\finalProject\guess_the_gibberish.py'], check=True)
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

def run_game2():
    try:
        subprocess.run(['python', r'C:\Users\ASUS\pavan^^\PycharmProjects\finalProject\guess_the_country.py'], check=True)
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

def run_game3():
    try:
        subprocess.run(['python', r'C:\Users\ASUS\pavan^^\PycharmProjects\finalProject\guess_the_cartoon.py'], check=True)
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")


root = Tk()
root.geometry('610x604')
root.title('Game Launcher')
root.resizable(False, False)

bg_img = Image.open(r"C:\Users\ASUS\pavan^^\PycharmProjects\finalProject\mainbg.jpg")
set_bg = ImageTk.PhotoImage(bg_img)
Label(image=set_bg).place(x=0, y=0) 

button_game1 = Button(root, width=6,text='PLAY', bd = 0,font='Helvetica 18 bold',bg='#ffd60a',command=run_game1)
button_game1.place(x=402, y=125)

button_game2 = Button(root, text='PLAY', bd = 0,font='Helvetica 18 bold',bg='#ffd60a',command=run_game2)
button_game2.place(x=406, y=282)

button_game3 = Button(root, text='PLAY', bd = 0,font='Helvetica 18 bold',bg='#ffd60a',command=run_game3)
button_game3.place(x=406 , y=462)

root.mainloop()
