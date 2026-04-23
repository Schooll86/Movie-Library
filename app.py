import tkinter as tk, json, os
from tkinter import messagebox

file="movies.json"; data=[]

def load():
    global data
    if os.path.exists(file): data=json.load(open(file))
    show()

def save(): json.dump(data,open(file,"w"),indent=4)

def add():
    n,g,y,r=e1.get(),e2.get(),e3.get(),e4.get()
    if not y.isdigit() or not r.replace('.','').isdigit() or float(r)>10:
        return messagebox.showerror("Ошибка","Проверь ввод")
    data.append({"name":n,"genre":g,"year":int(y),"rating":float(r)})
    show()

def show(arr=None):
    lb.delete(0,tk.END)
    for m in (arr or data):
        lb.insert(tk.END,f"{m['name']} {m['year']} {m['rating']}")

def filt():
    g,y=f1.get(),f2.get()
    arr=[m for m in data if (g in m['genre'] or not g) and (m['year']==int(y) if y else True)]
    show(arr)

root=tk.Tk()
e1,e2,e3,e4=[tk.Entry(root) for _ in range(4)]
[e.pack() for e in [e1,e2,e3,e4]]
tk.Button(root,text="Добавить",command=add).pack()

lb=tk.Listbox(root); lb.pack()
f1,f2=tk.Entry(root),tk.Entry(root)
f1.pack(); f2.pack()
tk.Button(root,text="Фильтр",command=filt).pack()

root.protocol("WM_DELETE_WINDOW",lambda:(save(),root.destroy()))
load(); root.mainloop()
