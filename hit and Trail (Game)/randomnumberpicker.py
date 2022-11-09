# Project 5 - random picker to pick values between  1 to 5 using slider
from tkinter import *
app = Tk()
app.title('Picking randomly')
app.geometry('280x180')

inp = Entry(width = 28)
inp.grid(row=0 , column= 0 ,columnspan=3 ,padx=30,pady= 10) # padx = space btw ele. along x axis , and y in pady

num = IntVar()

scl = Scale(app ,from_ = 1 ,to=5, variable= num , orient=HORIZONTAL)
scl.grid(row=1 , column= 0 ,columnspan=2 ,padx=30,pady= 10)

#making function according to check box value 
def rand_val():
    txt = inp.get()
    lis = txt.split(',')
    if num.get() !=1:
        msg = Label(app , text=f"Random : {random.sample(lis,num.get())}")
        msg.grid(row=3 , column= 0,columnspan=2,padx=30,pady= 5)
    else :
        msg = Label(app , text=f"Random : {random.choice(lis)}")
        msg.grid(row=3 , column= 0,columnspan=2,padx=30,pady= 5)
    if quitB['state'] == DISABLED:
        quitB['state'] = NORMAL

B = Button(app, text='Pick' , command=rand_val)
B.grid(row=2 , column= 0 ,padx=30,pady= 5)

quitB = Button(app, text='Cancel' , command=app.quit ,state=DISABLED)
quitB.grid(row=2 , column= 1,padx=30,pady= 5)

app.mainloop()