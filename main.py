import json 
import customtkinter as ctk

app = ctk.CTk()
app.geometry('600x600')

try:
    with open('data.json', 'r') as f:
        a = json.load(f)
except:
    a = 0

lbl = ctk.CTkLabel(app,text=a)
lbl.place(relx=0.5,rely=0.5,anchor='center')

def up():
    a +=1
    lbl.configure(text=a)
    with open('data.json', 'w') as f:
        json.dump(a, f)

btn=ctk.CTkButton(app,text='',command=up)
btn.place(relx=0.5,rely=0.3,anchor='center')

app.mainloop()