from tkinter import *
import datetime

window = Tk()
window.geometry("1200x500")
window.config(bg="#FC8E00")
window.resizable(width=False,height=False)
window.title('Age Calculator!')

current_year = datetime.date.today().year
age_month = datetime.date.today().month
age_day = datetime.date.today().day

 
def get_age():
    d=int(e1.get())
    m=int(e2.get())
    y=int(e3.get())
    leap=0
    for i in range(y,2022):
    	if i%4==0:
    		leap=leap+1
    if y%4==0 and m<3:
    	leap = leap - 1

    age = current_year - y
    total_months = abs(age_month - m)
    total_days = abs(age_day - d)

    months=(age*12)+age_month
    days=(age*365)+leap+(age_day)
    hour= (age*365*24)+(leap*24)+(age_day*24)
    mins= (age*365*24*60)+(leap*24*60)+(age_day*24*60)
    secs= (age*365*24*60*60)+(leap*24*60*60)+(age_day*24*60*60)
    t1.config(state='normal')
    t1.delete('1.0', END)
    t1.insert(END,age)
    t1.config(state='disabled')
    t2.config(state='normal')
    t2.delete('1.0', END)
    t2.insert(END,months)
    t2.config(state='disabled')
    t3.config(state='normal')
    t3.delete('1.0', END)
    t3.insert(END,days)
    t3.config(state='disabled')
    t4.config(state='normal')
    t4.delete('1.0', END)
    t4.insert(END,hour)
    t4.config(state='disabled')
    t5.config(state='normal')
    t5.delete('1.0', END)
    t5.insert(END,mins)
    t5.config(state='disabled')
    t6.config(state='normal')
    t6.delete('1.0', END)
    t6.insert(END,secs)
    t6.config(state='disabled')
    


def exit():
    window.destroy()    

 
lt = Label(window,text="The Age Calculator!",font=("Arial", 40,'bold','underline'),fg="#000000",bg="#FC8E00").pack()
ls = Label(window,font=("Arial",30,'italic'),text="Enter your birthday which includes the day-month-year.",fg="#000000",bg="#FC8E00").pack()
    
frame0 = Frame(window,bg="#FC8E00")
frame0.pack(pady=10)
 
l_d=Label(frame0,text="Date: ",font=('Arial',20,"bold"),fg="#00FCF9",bg="#FC8E00").pack(side='left',pady=10)
e1=Entry(frame0,width=5,font=('Arial',15,))
e1.pack(side='left',pady=10,padx=10)

l_m=Label(frame0,text="Month: ",font=('Arial',20,"bold"),fg="#00FCF9",bg="#FC8E00").pack(side='left',pady=10,padx=10)
e2=Entry(frame0,width=5,font=('Arial',15,))
e2.pack(side='left',pady=10,padx=0)

l_y=Label(frame0,text="Year: ",font=('Arial',20,"bold"),fg="#00FCF9",bg="#FC8E00").pack(side='left',pady=10,padx=10)
e3=Entry(frame0,width=5,font=('Arial',15,))
e3.pack(side='left',pady=10,padx=0)
 
b1=Button(window,text="Calculate Age!",font=("Arial",20,'bold'),bg='#2700FF',fg='#FFFFFF',bd=5,command=get_age)
b1.pack(pady=10,padx=10)
 
l1 = Label(window,text="The time you have spent on Earth",font=('Arial',20,"bold"),fg="#DBF9C9",bg="#FC8E00").place(x=10,y=310)
t1=Text(window,width=5,height=0,state="disabled",font=('Arial',15,"bold"))
t1.place(x=470,y=318)

l2 = Label(window,text="in years,",font=('Arial',20,"bold"),fg="#DBF9C9",bg="#FC8E00").place(x=530,y=310)
t2=Text(window,width=7,height=0,state="disabled",font=('Arial',15,"bold"))
t2.place(x=670,y=318)

l3 = Label(window,text="in months,",font=('Arial',20,"bold"),fg="#DBF9C9",bg="#FC8E00").place(x=750,y=310)
t3=Text(window,width=8,height=0,state="disabled",font=('Arial',15,"bold"))
t3.place(x=900,y=318)

l4 = Label(window,text="in days,",font=('Arial',20,"bold"),fg="#DBF9C9",bg="#FC8E00").place(x=1000,y=310)
t4=Text(window,width=8,height=0,state="disabled",font=('Arial',15,"bold"))
t4.place(x=270,y=380)

l5 = Label(window,text="in hours,",font=('Arial',20,"bold"),fg="#DBF9C9",bg="#FC8E00").place(x=370,y=375)
t5=Text(window,width=8,height=0,state="disabled",font=('Arial',15,"bold"))
t5.place(x=520,y=380)

l6 = Label(window,text="in minutes and",font=('Arial',20,"bold"),fg="#DBF9C9",bg="#FC8E00").place(x=620,y=375)
t6=Text(window,width=8,height=0,state="disabled",font=('Arial',15,"bold"))
t6.place(x=850,y=380)

l7 = Label(window,text="in seconds.",font=('Arial',20,"bold"),fg="#DBF9C9",bg="#FC8E00").place(x=950,y=375)

b2=Button(window,text="Exit Application!",font=("Arial",20),width=15,bd=5,bg='#FF0400',fg='#FFFFFF',relief=RIDGE,command=exit)
b2.pack(side='bottom',anchor=CENTER,pady=10)
 

 
window.mainloop()