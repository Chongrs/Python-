# Project Sistem Home Loan Calculator
# Nama : CHONG RONG SHENG
# Tingkatan : 3 RED

import tkinter as tk
from tkinter import*
from tkinter.ttk import*
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = Tk()
window.title("HOME LOAN CALCULATOR")
window.geometry('750x535')
bg = PhotoImage(file=('bg.png'))
c_bg = Label(image=bg)
c_bg.place(x=0, y=0)
window.resizable(0,0)

lbl_title = Label(window,text="HOME LOAN CALCULATOR",font=("Arial Bold",30))
lbl_title.pack(pady=45)

lbl_1 = Label(window,text="Insert Property Price(RM)  :",font=("Arial Bold",15))
lbl_1.place(x=150,y=160)
lbl_2 = Label(window,text="Insert Down Payment(%)   :",font=("Arial Bold",15))
lbl_2.place(x=150,y=210)
lbl_3 = Label(window,text="Insert Interest Rate(%)      :",font=("Arial Bold",15))
lbl_3.place(x=150,y=260)
lbl_4 = Label(window,text="Insert Period(year)            :",font=("Arial Bold",15))
lbl_4.place(x=150,y=310)

price = StringVar()
text_1 = tk.Entry(window,textvariable=price,font=("Arial Bold",20),width=10)
text_1.config({"background": "#D8E5FF"})
text_1.place(x=430,y=155)

down_pay = StringVar()
text_2 = tk.Entry(window,textvariable=down_pay,font=("Arial Bold",20),width=10)
text_2.config({"background": "#D8E5FF"})
text_2.place(x=430,y=205)

rate = StringVar()
text_3 = tk.Entry(window,textvariable=rate,font=("Arial Bold",20),width=10)
text_3.config({"background": "#D8E5FF"})
text_3.place(x=430,y=255)

period = StringVar()
text_4 = tk.Entry(window,textvariable=period,font=("Arial Bold",20),width=10)
text_4.config({"background": "#D8E5FF"})
text_4.place(x=430,y=305)

def next_t(x,y):
    x.focus()
    x.bind("<Return>",lambda funct1:y.focus())

next_t(text_1,text_2)
next_t(text_2,text_3)
next_t(text_3,text_4)

text_1.focus()

def clear():
    text_1.delete(0,'end')
    text_2.delete(0,'end')
    text_3.delete(0,'end')
    text_4.delete(0,'end')
    
    text_1.focus()
    

error = 0
def error_i(x):
    global error
    try :
        x = int(x)
        if x <= 0 :
            error = error + 1
            return
    except :
        error = error + 1
        return
        
def error_f(x):
    global error
    try :
        x = float(x)
        if x <= 0 :
            error = error + 1
            return
    except :
        error = error + 1
        return


def check():
    global error
    error_f(price.get())
    error_i(down_pay.get())
    error_f(rate.get())
    error_i(period.get())
    
    
    if error >= 1 :
        messagebox.showerror("Invalid Input","Please Enter Again")
        clear()
        return
    
def go_back(x,y):
    x.focus()
    clean(y)
    
def clean(x):
    x.destroy()

def window_2():
    check()
    if error > 0 :
        return
 
    window_2 = tk.Toplevel(window)
    window_2.geometry('750x650')
    window_2.resizable(0,0)
    window_2.config(bg="white")
    window_2.focus()
    
    price_a = float(price.get())
    down_pay_a = int(down_pay.get())
    rate_a = float(rate.get())
    period_a = int(period.get())
    
    balance = (100 - down_pay_a)
    balance = price_a * (balance/100)
    principal = balance
    rate_a = (rate_a/100)
    month_rate = (rate_a/12)
    month = (period_a * 12)

    month_pay = (balance * month_rate)/(1 - ((1 + month_rate)**-(month)))
    interest = (month_pay * month) - balance
    total_int = interest
    total_pay = price_a + total_int

    w2_lbl_t = Label(window_2,text="Result",font=("Arial Bold",30))
    w2_lbl_t.pack(pady=20)
    
    w2_lbl_1 = Label(window_2,text="Total Payment(RM):",font=("Arial Bold",15))
    w2_lbl_1.place(x=180,y=105)    
    w2_lbl_11 = Label(window_2,text=format(total_pay,".2f"),font=("Arial Bold",15))
    w2_lbl_11.place(x=470,y=105)
    
    w2_lbl_2 = Label(window_2,text="Balance(RM):",font=("Arial Bold",15))
    w2_lbl_2.place(x=180,y=155)
    w2_lbl_22 = Label(window_2,text=format(balance,".2f"),font=("Arial Bold",15))
    w2_lbl_22.place(x=470,y=155)
    
    w2_lbl_3 = Label(window_2,text="Total Interest(RM):",font=("Arial Bold",15))
    w2_lbl_3.place(x=180,y=205)
    w2_lbl_33 = Label(window_2,text=format(total_int,".2f"),font=("Arial Bold",15))
    w2_lbl_33.place(x=470,y=205)
    
    w2_lbl_4 = Label(window_2,text="Monthly Repayment(RM):",font=("Arial Bold",15))
    w2_lbl_4.place(x=180,y=255)
    w2_lbl_44 = Label(window_2,text=format(month_pay,".2f"),font=("Arial Bold",15))
    w2_lbl_44.place(x=470,y=255)
    
    balance_pie = (balance/total_pay)*100
    down_pay_pie = (down_pay_a/total_pay)*100
    total_int_pie = (total_int/total_pay)*100
    
    pie_l = [(balance_pie), (down_pay_a), (total_int_pie)]
    pie_lbl = ["Balance", "Down Payment", "Total Interest"]
    explode = [0.1, 0.1, 0.1]
    
    fig = Figure(figsize=(4.5,3))
    plt = fig.add_subplot()
    plt.pie(pie_l,labels=pie_lbl,startangle=90,explode=explode,autopct="%0.1f%%")
    pie_c = FigureCanvasTkAgg(fig,window_2)
    pie_c.get_tk_widget().place(x=145,y=320)

   
    button_2 = tk.Button(window_2,text="<",height=3,width=10,command=lambda:[go_back(window,window_2)])
    button_2.config(bg="#A3C1EE",font=80)
    button_2.place(x=90,y=320)
    
    button_3 = tk.Button(window_2,text=">",height=3,width=10,command=lambda:[window_3(),clean(window_2)])
    button_3.config(bg="#A3C1EE",font=80)
    button_3.place(x=580,y=320)
   

    
def window_3():
    window_3 = tk.Toplevel(window)
    window_3.geometry("750x450")
    window_3.resizable(0,0)
    window_3.focus()
    
    price_a = float(price.get())
    down_pay_a = int(down_pay.get())
    rate_a = float(rate.get())
    period_a = int(period.get())
    
    balance = (100 - down_pay_a)
    balance = price_a * (balance/100)
    principal = balance
    rate_a = (rate_a/100)
    month_rate = (rate_a/12)
    month = (period_a * 12)

    month_pay = (balance * month_rate)/(1 - ((1 + month_rate)**-(month)))
    interest = (month_pay * month) - balance
    total_int = interest
    total_pay = price_a + total_int
    
    w3_lbl_t = Label(window_3,text="Analysis",font=("Arial Bold",30))
    w3_lbl_t.pack(pady=20)
    
    table = ttk.Treeview(window_3)
    table['column'] = ("Month","Principal","Interest","Balance")
    table.column("#0",width=0,stretch=0)
    table.column("Month",anchor=CENTER,width=60)
    table.column("Principal",anchor=CENTER,width=130)
    table.column("Interest",anchor=CENTER,width=130)
    table.column("Balance",anchor=CENTER,width=130)
    
    table.heading("#0")
    table.heading("Month",text="Month",anchor=CENTER)
    table.heading("Principal",text="Principal(RM)",anchor=CENTER)
    table.heading("Interest",text="Interest(RM)",anchor=CENTER)
    table.heading("Balance",text="Balance(RM)",anchor=CENTER)
    
    x = 0
    for i in range(int(month)) :
        x = x + 1
        interest = balance * month_rate
        principal = month_pay - interest
        balance = balance - principal
        if balance <= 0 :
            balance = 0.00
        table.insert(parent='',index='end',iid=i,text="",values=(x,format(principal,".2f"),format(interest,".2f"),format(balance,".2f")))
        
    style = ttk.Style()
    style.configure("Treeview.Heading", font=(None, 13))
    style.configure("Treeview", font=(None, 13))
    table.pack(pady=10)
    
    button_4 = tk.Button(window_3,text="<",height=2,width=8,command=lambda:[window_2(),clean(window_3)])
    button_4.config(bg="#A3C1EE",font=80)
    button_4.place(x=120,y=360)
    
    button_5 = tk.Button(window_3,text="Home Page",height=2,width=12,command=lambda:[go_back(window,window_3),clear()])
    button_5.config(bg="#A3C1EE",font=80)
    button_5.place(x=320,y=360)
    
    
b1_image = PhotoImage(file=('r_button.png'))    
button_1 = Button(window,image=b1_image,command=window_2)
button_1.place(x=600,y=400)


window.mainloop()