from tkinter import *
import time
root=Tk()
root.title("Digital Clock")
root.geometry("1350x700+0+0")
root.config(bg="#081923")

def clock():
    h=str(time.strftime("%H"))
    m=str(time.strftime("%M"))
    s=str(time.strftime("%S"))
    # print(h,m,s)
    if int (h)>12 and int(m)>0:
        label_noon.config(text="PM")
    if int(h)>12:
        h=str((int(h)-12))
        
     
    label_hr.config(text=h)
    label_min.config(text=m)
    label_sec.config(text=s)

    label_hr.after(200,clock)
    


label_hr=Label(root,text="12",font=("Times new roman",50,"bold"),bg="#0875B7",fg="white")
label_hr.place(x=350,y=200,width=150,height=150)
              
label_hr2=Label(root,text="HOUR",font=("Times new roman",20,"bold"),bg="#0875B7",fg="white")
label_hr2.place(x=350,y=360,width=150,height=50)

label_min=Label(root,text="12",font=("Times new roman",50,"bold"),bg="#008ea4",fg="white")
label_min.place(x=520,y=200,width=150,height=150)
              
label_min2=Label(root,text="MINUTE",font=("Times new roman",20,"bold"),bg="#008ea4",fg="white")
label_min2.place(x=520,y=360,width=150,height=50)

label_sec=Label(root,text="12",font=("Times new roman",50,"bold"),bg="#0875B7",fg="white")
label_sec.place(x=690,y=200,width=150,height=150)
              
label_sec2=Label(root,text="SECOND",font=("Times new roman",20,"bold"),bg="#0875B7",fg="white")
label_sec2.place(x=690,y=360,width=150,height=50)

label_noon=Label(root,text="AM",font=("Times new roman",50,"bold"),bg="#df002a",fg="white")
label_noon.place(x=860,y=200,width=150,height=150)
              
label_sec2=Label(root,text="NOON",font=("Times new roman",20,"bold"),bg="#df002a",fg="white")
label_sec2.place(x=860,y=360,width=150,height=50)


clock()
root.mainloop()
