from tkinter import *
from tkinter import ttk
from core.about import software_details as sd, theme, user
import requests
import json


def get_data():
    l2.config(text='@Checking...')
    l2.update()

    data = {
        'email': user['email'],
        'password': user['password']
    }
    res = requests.post(sd['web_address_login'], data)
    # res = requests.get(sd['web_address'])
    # dt = json.loads(res.text)
    print(res)
    print(res.text)

    l2.config(text='@Ok')
    l2.update()
    return


def students():
    root = Toplevel()
    root.title(f'{a} - {sd["name"]}')

    root.mainloop()


root = Tk()
root.title(sd['name'])
root.geometry('500x400')

f1 = Frame(root, bg=theme['bg'], width=10)
f1.pack(fill=BOTH, expand=True)

f2 = Frame(root, bg=theme['bg'], width=10)
f2.pack(fill=BOTH, expand=True)

f3 = Frame(root, background='white')
f3.pack(fill=X, side=BOTTOM)


style = ttk.Style(f2)
style.configure('TButton', font='calibri 12 bold',
                borderwidth=4, background=theme['bg'])
style.map('TButton', foreground=[
    ('active', 'red'), ('!disabled', 'green')], background=[('active', theme['bg'])])


l1 = Label(f1, text='Student DB', font='Arial 20 italic',
           bg=theme['bg'], fg=theme['fg'])
l1.pack()

l2 = Label(f3, text='@Active', font='calibri 13 bold')
l2.grid(row=1, column=1)

UID = StringVar()
e1 = Entry(f1, textvariable=UID, width=10, font='calibri 12')
e1.pack(padx=2, pady=5, ipadx=50, ipady=5)

b1 = ttk.Button(f1, text='Check', command=get_data)
b1.pack(ipady=5, ipadx=10)

root.mainloop()
