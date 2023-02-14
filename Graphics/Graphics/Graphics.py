from tkinter import*
from tkinter import ttk
k=0
def klikker(event):
    global k
    k+=1
    lbl.configure(text=k)
def klikker1(event):
    global k
    if k>0:
        k-=1
    lbl.configure(text=k)
def entry_to_label(event):
    text=ent.get()
    lbl.configure(text=text)
    ent.delete(0,END)
def valik():
    text=var.get()
    ent.insert(END, text)
def uus_aken(ind:int):
    def tab_valik(ind:int):
        uusaken.config(title=texts[ind])
    uusaken=Toplevel()
    tabs=ttk.Notebook(uusaken)
    texts=["Esimene", "Teine", "Kolmas", "Neljas"]
    tab=[]
    for i in range(len(texts)):
        tab.append("tab"+str(i)) #tab0,tab1,tab2,tab3
        tab[i]=Frame(tabs)
        tabs.add(tab[i], text=texts[i])
        tab[i].bind("<Button-1>", tab_valik(i))
    tabs.grid(row=0, column=0)
    tabs.select(ind)

    uusaken.title(texts[ind])
    uusaken.mainloop()


window=Tk()#respond for formation
window.title('The first window')
window.geometry('600x200')# change size
m=Menu(window)
window.config(menu=m)
m1=Menu(m)
m.add_cascade(label="Tabs",menu=m1)
m1.add_command(label="1 Tab", accelerator="Command+A", command=lambda:uus_aken(0))
m1.add_command(label="2 Tab", accelerator="Command+B", command=lambda:uus_aken(1))
m1.add_command(label="3 Tab", accelerator="Command+C", command=lambda:uus_aken(2))
m1.add_command(label="4 Tab", accelerator="Command+D", command=lambda:uus_aken(3))

lbl=Label(window, text="...", font="Arial 20")
btn=Button(window, text='press',font='Arial 20', fg='blue', bg='#148038', width=30,height=5, relief=RAISED) #SUNKEN,GROOVE,RAISED (relief)
ent=Entry(window, fg='blue', bg='#148038', font="Arial 20", width=30, justify=CENTER)
var=IntVar()#stringVar()
r1=Radiobutton(window, text="Esimene", font='Arial 20',width=30, variable=var, value=1, command=valik)
r2=Radiobutton(window, text="Teine", font='Arial 20',width=30, variable=var, value=2, command=valik)
btn.bind("<Button-1>", klikker)
btn.bind("<Button-3>", klikker1)
#1- left click, 2- mouse wheel, 3- right click
ent.bind("<Return>", entry_to_label) #ENTER
btn.pack()
lbl.pack()
ent.pack()
r1.pack(side=LEFT)
r2.pack(side=LEFT)
window.mainloop() # start the window