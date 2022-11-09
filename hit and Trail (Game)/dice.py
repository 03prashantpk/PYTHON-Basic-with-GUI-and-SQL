from tkinter import *
import random

dic = {0 : '🎲', 1 : '⚀', 2 : '⚁', 3 : '⚂', 4 : '⚃', 5 : '⚄', 6 : '⚅'}

app = Tk()
app.title('Dice Roller')
app['background'] = 'black'

dice = Label(app, text= dic[0],font=('Times' ,110),background='black',foreground='white')
dice.grid(row=0 , column=0,columnspan=2, padx= 50 , pady= 5)
def roll():
    rand = random.randint(1,6)
    msg = Label(app,text=dic[rand] , font=('Times' ,110),width=2,background='black',foreground='white')
    msg.grid(row=0 , column=0,columnspan=2, padx= 30 , pady= 5) # giving same position as initial die so that it overlaps that

B = Button(app,text='Roll' , command=roll , relief='ridge' ,width=10,background='orange',foreground='black')
B.grid(row=2 , column=0,columnspan=2, padx= 30 , pady= 5)

app.mainloop()