
from tkinter import *
from math import sqrt
def reshenie(a,b,c):
    D = b*b - 4 * a * c
    if D>=0:
        x1= (-b + sqrt(D)) / (2*a)
        x2= (-b - sqrt(D)) / (2*a)
        text = "Дискриминант: %s \n X1 : %s \n X2 : %s \n" % (D, x1, x2)
    else:
        text = "Дискриминант: %s \n Невозможно решить уравнение" % D
    return text


#def konec():
#    try:
#        a_chislo = float(a.get())
#        b_chislo = float(b.get())
#        c_chislo = float(c.get())
#        vstavka(reshenie(a_chislo, b_chislo, c_chislo))
#    except ValueError:
#        vstavka("Вы точно ввели 3 цифры?")
        
def lahenda(): 
    global D,t,graf
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        if (float(a.get())==0 and float(b.get())==0 and float(c.get())==0):
            a.configure(text=f"Тут не можеть быть 0")
            a.configure(bg="red")
            b.configure(bg="red")
            c.configure(bg="red")
        elif float(a.get())==0 and float(b.get())!=0 and float(c.get())!=0:
            a.configure(text=f"Тут не можеть быть 0")
            a.configure(bg="red")
            graf=False
        else:
            a_=float(a.get())
            b_=float(b.get())
            c_=float(c.get())
            D=b_*b_-4*a_*c_
            if D>0:
                x1_=round((-1*b_+sqrt(D))/(2*a_),2)
                x2_=round((-1*b_-sqrt(D))/(2*a_),2)
                t=f"X1={x1_}, \nX2={x2_}"
                graf=True
            elif D==0:
                x1_=round((-1*b_)/(2*a_),2)
                t=f"X1={x1_}"
                graf=True
            else:
                t="Корней нет"
                graf=False
            a.configure(text=f"D={D}\n{t}")
            a.configure(bg="lightblue")
            b.configure(bg="lightblue")
            c.configure(bg="lightblue")   
    else:
        if a.get()=="":
            a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")
        else:
            a.configure(bg="lightblue")
            b.configure(bg="lightblue")
            c.configure(bg="lightblue")
        graf=False
    return graf,D,t





def vstavka(value):
    output.delete("0.0", "end")
    output.insert("0.0", value)

root = Tk()
root.title("Квадратное уравнение")


frame = Frame(root)
frame.grid()
uravnenie = Label(frame, text="Решение квадратного уравнения", bg="Red", font="Arial 12", width=35, height=2).grid(row=0,column=0, columnspan=8)
a= Entry(frame, width=3)
a.grid(row=1,column=1,padx=(10,0))
a_lab = Label(frame,text="x**2+").grid(row=1,column=2)
b = Entry(frame,width=3)
b.grid(row=1,column=3)
b_lab = Label(frame, text="x+").grid(row=1,column=4)
c = Entry(frame,width=3)
c.grid(row=1,column=5)
c_lab = Label(frame, text="=0").grid(row=1,column=6)
btn = Button(frame, text="Решить",font="Arial 20", fg="blue", bg="#148037",relief=GROOVE, command=lahenda).grid(row=3,column=2,padx=(10,0))
output = Text(frame,bg="Green", font="Arial 12", width=35, height=5)
output.grid(row=4, columnspan=8)
root.mainloop()
    