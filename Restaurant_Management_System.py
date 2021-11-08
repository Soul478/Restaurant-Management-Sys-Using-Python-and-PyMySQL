import tkinter as tk
from tkinter import Label, Button
from tkinter import *
from tkinter import ttk
import random
import time
import tkinter.messagebox
import pymysql

localtime = time.asctime(time.localtime(time.time()))


class Appl:
    def __init__(self, top):
        self.top = top
        top.title("Restaurant Management")
        top.geometry("1028x500")
        top.configure(background="#091832")

        def btnClick(numbers):
            global operator
            operator=operator + str(numbers)
            text_Input.set(operator)

        def btnClearDisplay():
            global operator
            operator=""
            text_Input.set("")

        def btnEqualsInput():
            global operator
            sumup = str(eval(operator))
            text_Input.set(sumup)
            operator=""

        def qExit():
            qExit = tkinter.messagebox.askyesno("MySQL Connection","Confirm if you want to exit")
            if qExit > 0:
                root.destroy()
                return

        def Reset():
            rand.set("")
            fries.set("0")
            Chk_Burger.set("0")
            Big_King.set("0")
            Chk_Royal.set("0")
            Veg_Salade.set("0")
            Drinks.set("0")
            Cost.set("")
            Service_Charge.set("")
            Tax.set("")
            SubTotal.set("")
            Total.set("")

        def Save():
            if rand.get() == "" or Cost.get() == "" or Total.get() == "" :
                tkinter.messagebox.showerror("MySQL Connection", "Enter Correct Details")
            else:
                sqlCon = pymysql.connect(host="localhost", user="root", password="", database="trainee")
                cur = sqlCon.cursor()
                cur.execute("INSERT INTO trainee VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                    rand.get(),
                    fries.get(),
                    Chk_Burger.get(),
                    Big_King.get(),
                    Chk_Royal.get(),
                    Veg_Salade.get(),
                    Drinks.get(),
                    Cost.get(),
                    Service_Charge.get(),
                    Tax.get(),
                    SubTotal.get(),
                    Total.get()
                    ) )
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("MySQL Connection", "Record Entered Successfully")

        def Ref():
            x = random.randint(10400, 400789)
            randomRef= str(x)
            rand.set(randomRef)

            CoF = float(fries.get())
            CoD = float(Drinks.get())
            CoChKing = float(Chk_Burger.get())
            CoChR = float(Chk_Royal.get())
            CoBigKing = float(Big_King.get())
            CoVegSal = float(Veg_Salade.get())

            CostOfFries = CoF * 10
            CostOfDrinks = CoD * 10
            CostOfChkKing = CoChKing * 30
            CostOfChkRoyal = CoChR * 40
            CostOfBgKing = CoBigKing * 55
            CostOfVegSal = CoVegSal * 25

            CostOfMeal = str('%.2f' % (CostOfFries + CostOfDrinks + CostOfChkKing + CostOfBgKing + CostOfChkRoyal + CostOfVegSal)), "DH"

            PayTax = ((CostOfFries + CostOfDrinks + CostOfChkKing + CostOfBgKing + CostOfChkRoyal + CostOfVegSal) * 0.2)

            TotalCost = (CostOfFries + CostOfDrinks + CostOfChkKing + CostOfBgKing + CostOfChkRoyal + CostOfVegSal)

            Serv_Charge = ((CostOfFries + CostOfDrinks + CostOfChkKing + CostOfBgKing + CostOfChkRoyal + CostOfVegSal)/99)

            Service = str('%.2f' % Serv_Charge), "DH"

            OverAllCost = str('%.2f' % (PayTax + TotalCost + Serv_Charge)), "DH"

            PaidTax = str('%.2f' % PayTax), "DH"

            Service_Charge.set(Service)
            Cost.set(CostOfMeal)
            Tax.set(PaidTax)
            SubTotal.set(CostOfMeal)
            Total.set(OverAllCost)


        font10 = "{Courier New} 10 normal"
        font11 = "{U.S. 101} 25 bold"
        font12 = "Al-Aramco 11 bold"
        font13 = "{Courier New} 10 bold"
        font14 = "{Segoe} 15 bold"
        font15 = "Arial 13 bold" 
        font16 = "{Segoe UI} 13 bold"


        self.Label1 = tk.Label(master=top, text='Restaurant Management System', background="#091833", font=font11, foreground="#f2a343")
        self.Label1.place(relx= 0.275, rely=0.02, height=51, width=607)
    
        localtime1 = Label(master=top, text=localtime, background="#091833", font=font16, fg="steel blue")
        localtime1.place(relx= 0.420, rely=0.12)



        self.Label12 = tk.Label(master=top, text='Reference :', foreground='#bac8bd', font=font12, background="#091833", anchor='w')
        self.Label12.place(relx=0.054, rely=0.20)
        self.Label12 = tk.Label(master=top, text='Frite Botato :', foreground='#bac8bd', font=font12, background="#091833")
        self.Label12.place(relx=0.048, rely=0.32)
        self.Label12 = tk.Label(master=top, text='Chk Burger :', foreground='#bac8bd', font=font12, background="#091833")
        self.Label12.place(relx=0.050, rely=0.4)
        self.Label12 = tk.Label(master=top, text='Chk Royal :', foreground='#bac8bd', font=font12, background="#091833")
        self.Label12.place(relx=0.059, rely=0.48)
        self.Label12 = tk.Label(master=top, text='Big King :', foreground='#bac8bd', font=font12, background="#091833")
        self.Label12.place(relx=0.069, rely=0.56)
        self.Label12 = tk.Label(master=top, text='Veg Salad :', foreground='#bac8bd', font=font12, background="#091833")
        self.Label12.place(relx=0.059, rely=0.64)
        self.Label12 = tk.Label(master=top, text='Drinks :', foreground='#1812c6', font=font12, background="#091833")
        self.Label12.place(relx=0.082, rely=0.71)


        self.entry1 = tk.Entry(master=top, background="powder blue", bd=5, textvariable=rand, foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.18, rely=0.20)
        self.entry2 = tk.Entry(master=top, background="#d9d9d9", bd=5, textvariable=fries, foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry2.place(relx=0.18, rely=0.32)
        self.entry3 = tk.Entry(master=top, background="#d9d9d9", bd=5, textvariable=Chk_Burger, foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry3.place(relx=0.18, rely=0.4)
        self.entry4 = tk.Entry(master=top, background="#d9d9d9", bd=5, textvariable=Chk_Royal, foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry4.place(relx=0.18, rely=0.48)
        self.entry5 = tk.Entry(master=top, background="#d9d9d9", bd=5, textvariable=Big_King, foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry5.place(relx=0.18, rely=0.56)
        self.entry6 = tk.Entry(master=top, background="#d9d9d9", bd=5, textvariable=Veg_Salade, foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry6.place(relx=0.18, rely=0.64)
        self.entry7 = tk.Entry(master=top, background="#d9d9d9", bd=5, textvariable=Drinks, foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry7.place(relx=0.18, rely=0.71)



        # ____ Cost _____
        self.Label12 = tk.Label(master=top, text='Cost :', foreground='#e16740', font=font12, background="#091833")
        self.Label12.place(relx=0.43, rely=0.32)

        self.Label12 = tk.Label(master=top, text='Service Charge :', foreground='#bac8bd', font=font12, background="#091833")
        self.Label12.place(relx=0.38, rely=0.4)
        self.Label12 = tk.Label(master=top, text='Tax :', foreground='#bac8bd', font=font12, background="#091833")
        self.Label12.place(relx=0.43, rely=0.48)
        self.Label12 = tk.Label(master=top, text='Subtotal :', foreground='#bac8bd', font=font12, background="#091833")
        self.Label12.place(relx=0.40, rely=0.56)
        self.Label12 = tk.Label(master=top, text='Total :', foreground='#bac8bd', font=font12, background="#091833")
        self.Label12.place(relx=0.42, rely=0.64)



        TxtCost = self.entry9 = tk.Entry(master=top, background="powder blue", bd=5, textvariable=Cost, foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry9.place(relx=0.494, rely=0.32, relwidth=0.155)
        TxtS_C = self.entry10 = tk.Entry(master=top, background="powder blue", bd=5, textvariable=Service_Charge, foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry10.place(relx=0.519, rely=0.40, relwidth=0.130)
        TxtTax = self.entry11 = tk.Entry(master=top, background="powder blue", bd=5, textvariable=Tax,foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry11.place(relx=0.488, rely=0.480)
        TxtSubTotal = self.entry12 = tk.Entry(master=top, background="powder blue", bd=5, textvariable=SubTotal, foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry12.place(relx=0.487, rely=0.56)
        TxtTotal = self.entry13 = tk.Entry(master=top, background="powder blue", bd=5, textvariable=Total, foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.488, rely=0.64)


        self.Button2 = tk.Button(master=top, text="SAVE", command=Save, background='#e16740', font=font16)
        self.Button2.place(relx=0.039, rely=0.86, height=34, width=107)
        self.Button2 = tk.Button(master=top, text="TOTAL", command=Ref, background='#e16740', font=font16)
        self.Button2.place(relx=0.156, rely=0.86, height=34, width=107)
        self.Button2 = tk.Button(master=top, text="RESET", command=Reset, background='#e16740', font=font16)
        self.Button2.place(relx=0.272, rely=0.86, height=34, width=107)
        self.Button2 = tk.Button(master=top, text="EXIT", command=qExit, background='#e16740', font=font16)
        self.Button2.place(relx=0.389, rely=0.86, height=34, width=107)



        #______ Calc _______    
        
        textDisplay = self.entry8 = tk.Entry(master=top, background="powder blue", bd=10,insertwidth=2,foreground="#c60000", selectbackground="#f2a343", font=font13, textvariable=text_Input)
        self.entry8.place(relx=0.705, rely=0.24, height=35, relwidth=0.255)

        btn7 = self.Button1 = tk.Button(master=top, text= '''7''', background='#122c63', command=lambda:btnClick(7), font=font14, foreground='#ffffff', borderwidth='0')
        self.Button1.place(relx=0.705, rely=0.34, height=44, width=67)
        btn8 = self.Button2 = tk.Button(master=top, text= '''8''', background='#122c63', command=lambda:btnClick(8), font=font14, foreground='#ffffff', borderwidth='0')
        self.Button2.place(relx=0.780, rely=0.34, height=44, width=67)
        btn9 = self.Button3 = tk.Button(master=top, text= '''9''', background='#122c63', command=lambda:btnClick(9), font=font14, foreground='#ffffff', borderwidth='0')
        self.Button3.place(relx=0.855, rely=0.34, height=44, width=67)
        div = self.Button4 = tk.Button(master=top, text= '''/''', background='#122c63', command=lambda:btnClick("/"), font=font14, foreground='#ffffff', borderwidth='0')
        self.Button4.place(relx=0.930, rely=0.34, height=44, width=32)

        btn4 = self.Button5 = tk.Button(master=top, text= '''4''', background='#122c63', command=lambda:btnClick(4) ,font=font14, foreground='#ffffff', borderwidth='0')
        self.Button5.place(relx=0.705, rely=0.44, height=44, width=67)
        btn5 = self.Button6 = tk.Button(master=top, text= '''5''', background='#122c63', command=lambda:btnClick(5 ),font=font14, foreground='#ffffff', borderwidth='0')
        self.Button6.place(relx=0.780, rely=0.44, height=44, width=67)
        btn6 = self.Button7 = tk.Button(master=top, text= '''6''', background='#122c63', command=lambda:btnClick(6), font=font14, foreground='#ffffff', borderwidth='0')
        self.Button7.place(relx=0.855, rely=0.44, height=44, width=67)
        Multiply = self.Button8 = tk.Button(master=top, text= '''*''', background='#122c63', command=lambda:btnClick("*"), font=font14, foreground='#ffffff', borderwidth='0')
        self.Button8.place(relx=0.930, rely=0.44, height=44, width=32)
        
        btn1 = self.Button9 = tk.Button(master=top, text= '''1''', background='#122c63', command=lambda:btnClick(1), font=font14, foreground='#ffffff', borderwidth='0')
        self.Button9.place(relx=0.705, rely=0.54, height=44, width=67)
        btn2 = self.Button10 = tk.Button(master=top, text= '''2''', background='#122c63', command=lambda:btnClick(2), font=font14, foreground='#ffffff', borderwidth='0')
        self.Button10.place(relx=0.780, rely=0.54, height=44, width=67)
        btn3 = self.Button11 = tk.Button(master=top, text= '''3''', background='#122c63', command=lambda:btnClick(3), font=font14, foreground='#ffffff', borderwidth='0')
        self.Button11.place(relx=0.855, rely=0.54, height=44, width=67)
        Substraction = self.Button12 = tk.Button(master=top, text= '''-''', background='#122c63', command=lambda:btnClick("-"), font=font14, foreground='#ffffff', borderwidth='0')
        self.Button12.place(relx=0.930, rely=0.54, height=44, width=32)


        btn0 = self.Button13 = tk.Button(master=top, text= '''0''', background='#122c63', command=lambda:btnClick(0), font=font14, foreground='#ffffff', borderwidth='0')
        self.Button13.place(relx=0.705, rely=0.64, height=34, width=144)
        point = self.Button14 = tk.Button(master=top, text= '''.''', background='#122c63', command=lambda:btnClick("."), font=font14, foreground='#ffffff', borderwidth='0')
        self.Button14.place(relx=0.855, rely=0.64, height=34, width=67)
        Addition = self.Button15 = tk.Button(master=top, text= '''+''', background='#122c63', command=lambda:btnClick("+"), font=font14, foreground='#ffffff', borderwidth='0')
        self.Button15.place(relx=0.930, rely=0.64, height=34, width=32)

        Equal = self.Button16 = tk.Button(master=top, text= '''=''', background='#f2a343', command=btnEqualsInput,font=font14, foreground='#ffffff', borderwidth='0')
        self.Button16.place(relx=0.705, rely=0.72, height=34, width=200)
        Clear = self.Button16 = tk.Button(master=top, text= '''C''', background='#f2a343', command=btnClearDisplay, font=font14, foreground='#ffffff', borderwidth='0')
        self.Button16.place(relx=0.911, rely=0.72, height=34, width=51)


if __name__=='__main__':
        root = tk.Tk()
        operator=""
        text_Input = StringVar()

        rand = StringVar()
        fries = StringVar()
        Chk_Burger = StringVar()
        Big_King = StringVar()
        Chk_Royal = StringVar()
        Veg_Salade = StringVar()
        Drinks = StringVar()
        Cost = StringVar()
        Service_Charge = StringVar()
        Tax = StringVar()
        SubTotal = StringVar()
        Total = StringVar()

        my_gui = Appl(root)
        root.mainloop()