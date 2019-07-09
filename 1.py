import tkinter as tk
import os
from  PIL import ImageTk
from tkinter import *
from tkinter import messagebox
win = tk.Tk() 
win.title("HMML Games") 
win.resizable(0, 0)
win.configure(bg='turquoise1')
label1=tk.Label(win,text="fun games",fg="white",bg="turquoise1",font=("Showcard Gothic",50))
label1.config(width=200)
def helloCallBack():
 os.system('Python brickblock.py')
photo1 = tk.PhotoImage(file="C:\\Users\\mimi\\Desktop\\Games\\New folder (3)\\unnamed.png")
button1=tk.Button(win,text="uuuu",fg="black",command=helloCallBack,image=photo1) 
def helloCall():
 os.system('Python four_in_row.py')
photo2 = tk.PhotoImage(file="C:\\Users\\mimi\\Desktop\\Games\\New folder (3)\\1.png") 
button2=tk.Button(win,text="uuuu",fg="black",command=helloCall,image=photo2)
def hello():
 os.system('Python snake.py')
photo3 = tk.PhotoImage(file="C:\\Users\\mimi\\Desktop\\Games\\New folder (3)\\11.png")
button3=tk.Button(win,text="uuuu",fg="black",command=hello,image=photo3)
def hell():
 os.system('Python jewlery.py')
photo4 = tk.PhotoImage(file="C:\\Users\\mimi\\Desktop\\Games\\New folder (3)\\jewelry.png")
button4=tk.Button(win,text="uuuu",fg="black",command=hell,image=photo4)
def hel():
 os.system('Python memorypuzzle.py')
photo5 = tk.PhotoImage(file="C:\\Users\\mimi\\Desktop\\Games\\New folder (3)\\memory-puzzle.png")
button5=tk.Button(win,text="uuuu",fg="black",command=hel,image=photo5)
win.geometry("1000x700")
label1.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button1.place(x=100,y=150)
button2.place(x=700,y=150)
button3.place(x=100,y=450)
button4.place(x=700,y=450)
button5.place(x=400,y=300)

win.mainloop()
