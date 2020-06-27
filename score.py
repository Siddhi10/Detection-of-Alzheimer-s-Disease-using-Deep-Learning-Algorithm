from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

def show_entry_fields():
    counter=0
    if(entry_1.get()=='2020'):
        counter=counter+2
    if(entry_2.get()=='Summer'):
        counter=counter+3
    if(entry_4.get()=='Mumbai'):
        counter=counter+2
    if(entry_5.get()=='Maharashtra'):
        counter=counter+2
    if(entry_6.get()=='India'):
        counter=counter+1
    if(str(var.get())=='1'):
        counter=counter+5
    if(str(var1.get())=='1'):
        counter=counter+1 
    if(str(var2.get())=='1'):
        counter=counter+2
    if(str(var3.get())=='1'):
        counter=counter+6
    if(str(var4.get())=='1'):
        counter=counter+3
    if(str(var5.get())=='1'):
        counter=counter+1
    if(str(var6.get())=='1'):
        counter=counter+1
    if(str(var7.get())=='1'):
        counter=counter+1
    print(counter)
    #label1=tk.Label(master, text="%s /30" % counter,font=("bold", 20), bg='brown',fg='white',height=4, width=10)
    #label1.place(x=200, y=700)
    label = tk.Label(master, text = "",font=("bold", 17), bg='brown',fg='white',height=3, width=70)
    if(counter<18):
        label.configure(text =  "The score is %s /30. The patient has SEVERE COGNITIVE IMPAIRMENT" % counter)
    else:
        if(counter<24):
            label.configure(text = "The score is %s /30. The patient has MILD COGNITIVE IMPAIRMENT" % counter)
        else:
            label.configure(text = "The score is %s /30.  The patient has NO COGNITIVE IMPAIRMENT" % counter)
    label.place(x=200, y=700)
    #return counter
 

#print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))


master = tk.Tk()
var=IntVar()
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()

path='coolbrain1.jpg'

canvas=tk.Canvas(master, height=600, width=1000)
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(master, image = img)
panel.place(x=0, y=0)
canvas.pack()

label_0 = Label(master, text="Mini Mental State Exam ",width=20,borderwidth="1",relief="solid",font=("bold", 20),bg="gray6", fg="white")
label_0.place(x=150,y=53)
#label_0.pack()

label_1 = Label(master, text="1. What year is it?     ",width=20,font=("bold", 13),bg="gray6", fg="white")
#label_1.place(x=60,y=130)
label_1.place(x=80,y=130)

entry_1 = Entry(master)
#entry_1.place(x=60,y=160)
entry_1.place(x=350,y=130)
    
    
label_2 = Label(master, text="2. What season is it? ",width=20,font=("bold", 13),bg="gray6", fg="white")
#label_2.place(x=30,y=190)
label_2.place(x=80,y=170)

entry_2 = Entry(master)
#entry_2.place(x=60,y=220)
entry_2.place(x=350,y=170)

label_3 = Label(master, text=" 3. Where are we now?",width=20,font=("bold", 13),bg="gray6", fg="white")
#label_3.place(x=30,y=250)
label_3.place(x=80,y=210)

label_4 = Label(master, text="City",width=15,font=("bold", 13),bg="gray6", fg="white")
#label_4.place(x=30,y=280)
label_4.place(x=300,y=210)

entry_4 = Entry(master)
#entry_4.place(x=60,y=310)
entry_4.place(x=350,y=250)

label_5 = Label(master, text="State",width=15,font=("bold", 13),bg="gray6", fg="white")
#label_5.place(x=30,y=340)
label_5.place(x=440,y=210)

entry_5 = Entry(master)
#entry_5.place(x=60,y=370)
entry_5.place(x=490,y=250)

label_6 = Label(master, text="Country",width=15,font=("bold", 13),bg="gray6", fg="white")
#lael_6.place(x=30,y=400)
label_6.place(x=590,y=210)

entry_6 = Entry(master)
#enry_6.place(x=60,y=430)
entry_6.place(x=630,y=250)

label_7 = Label(master, text="4. Count backwards from               \n100 from sevens                    ",width=30,font=("bold", 13),bg="gray6", fg="white")
#label_7.place(x=-30,y=460)
label_7.place(x=80,y=290)

label_8 = Label(master, text="Done? ",width=10,font=("bold", 13),bg="gray6", fg="white")
#label_8.place(x=-110,y=490)
label_8.place(x=330,y=290)

#Radiobutton(frame, text="Yes",padx = 5, variable=var, value=1).place(x=160,y=490)
#Radiobutton(frame, text="No",padx = 20, variable=var, value=2).place(x=220,y=490)

w1=Radiobutton(master, text="Yes",padx = 5, variable=var, value=1,font=("bold", 13),bg="gray6", fg="white", selectcolor="gray")
w1.place(x=410,y=290)

w2=Radiobutton(master, text="No",padx = 5, variable=var, value=2,font=("bold", 13),bg="gray6", fg="white", selectcolor="gray")
w2.place(x=480,y=290)
 
label_9 = Label(master, text="5.Repeat the phrase    ",width=20,font=("bold", 13),bg="gray6", fg="white")
#label_9.place(x=-95,y=540)
label_9.place(x=80,y=345)

label_10 = Label(master, text="Done? ",width=10,font=("bold", 13),bg="gray6", fg="white")
#label_10.place(x=-110,y=570)
label_10.place(x=330,y=345)
    
#Radiobutton(frame, text="Yes",padx = 5, variable=var1, value=1).place(x=160,y=570)
#Radiobutton(frame, text="No",padx = 20, variable=var1, value=2).place(x=220,y=570)
Radiobutton(master, text="Yes",padx = 5, variable=var1, value=1,font=("bold", 13),bg="gray6", fg="white", selectcolor="gray").place(x=410,y=345)
Radiobutton(master, text="No",padx = 5, variable=var1, value=2,font=("bold", 13),bg="gray6", fg="white", selectcolor="gray").place(x=480,y=345)
    
label_11 = Label(master, text="6. Guess the 2 objects  ",width=20,font=("bold", 13),bg="gray6", fg="white")
label_11.place(x=80,y=385)

#label_111 = Label(master, text="Done? ",width=10,font=("bold", 13),bg="gray6", fg="white")
#label_10.place(x=-110,y=570)
#label_111.place(x=330,y=385)

Radiobutton(master, text="Correct",padx = 5, variable=var2, value=1,font=("bold", 13),bg="gray6", fg="white", selectcolor="gray").place(x=350,y=385)
Radiobutton(master, text="Incorrect",padx = 5, variable=var2, value=2,font=("bold", 13),bg="gray6", fg="white", selectcolor="gray").place(x=460,y=385)


label_12 = Label(master, text="7. Repeat the 3 words I told    \n you in the beginning       ",width=25,font=("bold", 13),bg="gray6", fg="white")
label_12.place(x=80,y=425)

Radiobutton(master, text="Correct",padx = 5, variable=var3, value=1,font=("bold", 13),bg="gray6", fg="white", selectcolor="gray").place(x=350,y=425)
Radiobutton(master, text="Incorrect",padx = 5, variable=var3, value=2,font=("bold", 13),bg="gray6", fg="white", selectcolor="gray").place(x=460,y=425)

label_13 = Label(master, text="  8. Take a paper with your         \n right hand, fold it in half,   \n put in on the table.            ",width=25,font=("bold", 13),bg="gray6", fg="white")
label_13.place(x=80,y=485)

label_10 = Label(master, text="Done? ",width=10,font=("bold", 13),bg="gray6", fg="white")
#label_10.place(x=-110,y=570)
label_10.place(x=330,y=485)
    
#Radiobutton(frame, text="Yes",padx = 5, variable=var1, value=1).place(x=160,y=570)
#Radiobutton(frame, text="No",padx = 20, variable=var1, value=2).place(x=220,y=570)
Radiobutton(master, text="Yes",padx = 5, variable=var4, value=1,font=("bold", 13),bg="gray6", fg="white", selectcolor="gray").place(x=410,y=485)
Radiobutton(master, text="No",padx = 5, variable=var4, value=2,font=("bold", 13),bg="gray6", fg="white", selectcolor="gray").place(x=480,y=485)

label_14 = Label(master, text="        9. Close your eyes                 ",width=20,font=("bold", 13),bg="gray6", fg="white")
label_14.place(x=80,y=555)

label_10 = Label(master, text="Done? ",width=10,font=("bold", 13),bg="gray6", fg="white")
#label_10.place(x=-110,y=570)
label_10.place(x=330,y=555)
    
#Radiobutton(frame, text="Yes",padx = 5, variable=var1, value=1).place(x=160,y=570)
#Radiobutton(frame, text="No",padx = 20, variable=var1, value=2).place(x=220,y=570)
Radiobutton(master, text="Yes",padx = 5, variable=var5, value=1,font=("bold", 13),bg="gray6", fg="white", selectcolor="gray").place(x=410,y=555)
Radiobutton(master, text="No",padx = 5, variable=var5, value=2,font=("bold", 13),bg="gray6", fg="white", selectcolor="gray").place(x=480,y=555)

label_15 = Label(master, text="10. Make up and write      \na sentence           ",width=20,font=("bold", 13),bg="gray6", fg="white")
label_15.place(x=80,y=585)

Radiobutton(master, text="Correct",padx = 5, variable=var6, value=1,font=("bold", 13),bg="gray6", fg="white", selectcolor="gray").place(x=350,y=585)
Radiobutton(master, text="Incorrect",padx = 5, variable=var6, value=2,font=("bold", 13),bg="gray6", fg="white", selectcolor="gray").place(x=460,y=585)

label_16 = Label(master, text="11. Copy this picture        \n shown to you         ",width=20,font=("bold", 13),bg="gray6", fg="white")
label_16.place(x=80,y=635)

Radiobutton(master, text="Correct",padx = 5, variable=var7, value=1,font=("bold", 13),bg="gray6", fg="white", selectcolor="gray").place(x=350,y=635)
Radiobutton(master, text="Incorrect",padx = 5, variable=var7, value=2,font=("bold", 13),bg="gray6", fg="white", selectcolor="gray").place(x=460,y=635)

#label_11.place(x=-90,y=610)


tk.Button(master, text='Get Score',height=4, width=10,font=("bold", 13), bg='brown',fg='white', command=show_entry_fields).place(x=80,y=700)
tk.Button(master, text='Upload MRI',height=4, width=10,font=("bold", 13), bg='brown',fg='white', command=master.destroy).place(x=1130,y=700)

tk.mainloop()