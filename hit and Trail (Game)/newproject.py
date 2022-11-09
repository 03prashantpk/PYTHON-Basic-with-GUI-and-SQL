# now decorating above project
import datetime
from tkinter import*
app = Tk()
app.title('Length Converter')
app.geometry('360x130')

app['background'] ='silver'

ch1 = StringVar()
opt1 = OptionMenu(app,ch1,'Meters','Inches','Foot')
opt1.grid(row=0 , column = 0,padx= 15 , pady =5)

msg1 = Label(app,text='convert to',background='silver')
msg1.grid(row=0 , column = 1,padx= 15 , pady =5)

ch2 = StringVar()
opt2ch2 = OptionMenu(app,ch2,'Meters','Inches','Foot')
opt2ch2.grid(row=0 , column = 2,padx= 15 , pady =5)

msg2 = Label(app,text='Enter the number :',background='silver')
msg2.grid(row=1 , column = 0,padx= 15 , pady =5)

inp1 = Entry(width=12,background='silver')
inp1.grid(row=1 , column = 1,padx= 15 , pady =5)

def convert():
    # meters to others
    if ch1.get() == 'Meters' and ch2.get() == 'Meters':
        num = float(inp1.get())
        msg2 = Label(app,text=round(float(num),2),background='cyan')
        msg2.grid(row=1 , column = 2,padx= 15 , pady =5)
    if ch1.get() == 'Meters' and ch2.get() == 'Inches':
        num = float(inp1.get())
        msg2 = Label(app,text=round(float(num*39.3701),2),background='cyan')
        msg2.grid(row=1 , column = 2,padx= 15 , pady =5)
    if ch1.get() == 'Meters' and ch2.get() == 'Foot':
        num = float(inp1.get())
        msg2 = Label(app,text=round(float(num*3.28084),2),background='cyan')
        msg2.grid(row=1 , column = 2,padx= 15 , pady =5)
    # inches to others
    if ch1.get() == 'Inches' and ch2.get() == 'Meters':
        num = float(inp1.get())
        msg2 = Label(app,text=round(float(num*0.0254),2),background='cyan')
        msg2.grid(row=1 , column = 2,padx= 15 , pady =5)
    if ch1.get() == 'Inches' and ch2.get() == 'Inches':
        num = float(inp1.get())
        msg2 = Label(app,text=round(float(num),2),background='cyan')
        msg2.grid(row=1 , column = 2,padx= 15 , pady =5)
    if ch1.get() == 'Inches' and ch2.get() == 'Foot':
        num = float(inp1.get())
        msg2 = Label(app,text=round(float(num*0.0833333),2),background='cyan')
        msg2.grid(row=1 , column = 2,padx= 15 , pady =5)
    # foot to others
    if ch1.get() == 'Foot' and ch2.get() == 'Meters':
        num = float(inp1.get())
        msg2 = Label(app,text=round(float(num*0.3048),2),background='cyan')
        msg2.grid(row=1 , column = 2,padx= 15 , pady =5)
    if ch1.get() == 'Foot' and ch2.get() == 'Inches':
        num = float(inp1.get())
        msg2 = Label(app,text=round(float(num*12),2),background='cyan')
        msg2.grid(row=1 , column = 2,padx= 15 , pady =5)
    if ch1.get() == 'Foot' and ch2.get() == 'Foot':
        num = float(inp1.get())
        msg2 = Label(app,text=round(float(num),2),background='cyan')
        msg2.grid(row=1 , column = 2,padx= 15 , pady =5)

B = Button(app,text='Convert',command=convert,relief='raised',width=7,background='orange')
B.grid(row=2 , column = 1,padx= 15 , pady =5)

app.mainloop()