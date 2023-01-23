from tkinter import *
import mysql.connector
from tabulate import tabulate

window = Tk()
order_number_val = StringVar()
order_date_val = StringVar()
customer_code_val = StringVar()

global SEARCHENTRIES

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "G@n@p@t11")
mycursor = mydb.cursor()
mycursor.execute("use shop")

def Register():
        def Submit():
                it = "insert into customer values ( %s, %s)"
                val = (t3.get(), t4.get())
                mycursor.execute(it, val)
                mydb.commit()
                reg.destroy()
        

        reg = Toplevel()
        reg.title("Registration Window")
        l3 = Label(reg, text = "Name: ")
        l4 = Label(reg, text = "Password: ")
        t3 = Entry(reg)
        t4 = Entry(reg)
        b3 = Button(reg, text = "Submit", command = Submit)

        l3.grid(row = 0, column = 0)
        l4.grid(row = 2, column = 0)
        t3.grid(row = 0, column = 2)
        t4.grid(row = 2, column = 2)
        b3.grid(row = 4, column = 0)

def Login():
        sel = "select * from customer where name = %s and password = %s"
        val1 = (t1.get(), t2.get())
        mycursor.execute(sel, val1)
        temp = mycursor.fetchall()
        if temp:
                #root1.destroy()
                def submitform():
                    global SEARCHENTRIES,result,secondframe
                    SEARCHENTRIES = [order_number_val.get(), order_date_val.get(), customer_code_val.get()]
                    print(SEARCHENTRIES)
                    mydb = mysql.connector.connect(host="localhost", user="root", password="G@n@p@t11")
                    mycursor = mydb.cursor()
                    mycursor.execute('use shop;')

                    print('OrderNumber :' + order_number_val.get())
                    print('Order Date:' + order_date_val.get())
                    print('Customer Code:'+customer_code_val.get())
                    if val_1.get() == 1:
                        print('Order Number: YES')
                    else:
                        print('Order Number: NO')
                    if val_2.get() == 1:
                        print('Order Date: YES')
                    else:
                        print('Order Date: NO')
                    if val_3.get() == 1:
                        print('Customer Code: YES')
                    else:
                        print('Customer Code: NO')
                    print('submit')



                    if val_1.get()==1 and val_2.get()==1 and val_3.get()==1:
                        query = 'select * from orders where ORD_NUM = {} AND ORD_DATE= \'{}\' AND CUST_CODE = \'{}\';'.format(*SEARCHENTRIES)
                    
                    elif val_1.get()==1 and val_2.get()==1 and val_3.get()!=1:
                        query = 'select * from orders where ORD_NUM = {} AND ORD_DATE= \'{}\';'.format(SEARCHENTRIES[0],SEARCHENTRIES[1])
                    
                    elif val_1.get()==1 and val_2.get()!=1 and val_3.get()==1:
                        query = 'select * from orders where ORD_NUM = {} AND CUST_CODE = \'{}\';'.format(SEARCHENTRIES[0],SEARCHENTRIES[2])
                    
                    elif val_1.get()!=1 and val_2.get()==1 and val_3.get()==1:
                        query = 'select * from orders where ORD_DATE= \'{0}\' AND CUST_CODE = \'{1}\';'.format(SEARCHENTRIES[1], SEARCHENTRIES[2])
                    
                    elif val_1.get()==1 and val_2.get()!=1 and val_3.get()!=1:
                        query = 'select * from orders where ORD_NUM = {0};'.format(SEARCHENTRIES[0])
                    
                    elif val_1.get()!=1 and val_2.get()==1 and val_3.get()!=1:
                        query = 'select * from orders where ORD_DATE= \'{0}\';'.format(SEARCHENTRIES[1])
                    
                    elif val_1.get()!=1 and val_2.get()!=1 and val_3.get()==1:
                        query = 'select * from orders where CUST_CODE = \'{0}\';'.format(SEARCHENTRIES[2])

                    print(query)
                    try:
                        mycursor.execute(query)
                        print ('data SELECTED')
                        result = mycursor.fetchall()
                        for i in result:
                            print(i)
                    except Exception as e :
                        print(e)


                # Labels
                label_order_number = Label(window, text='Order Number :').pack(
                    padx=15, pady=5, anchor=W)
                order_number = Entry(window, textvariable=order_number_val).pack(anchor=W)
                label_order_date = Label(window, text='Order date :').pack(
                    padx=15, pady=5, anchor=W)
                order_date = Entry(window, textvariable=order_date_val).pack(anchor=W)
                label_customer_code = Label(window, text='customer code :').pack(
                    padx=15, pady=5, anchor=W)
                customer_code = Entry(window, textvariable=customer_code_val).pack(anchor=W)



                # checkboxes
                val_1 = IntVar()
                val_2 = IntVar()
                val_3 = IntVar()
                checkbox_1 = Checkbutton(window, text='Order Number',
                                        variable=val_1).pack(anchor=W)
                checkbox_1 = Checkbutton(window, text='Order Date',
                                        variable=val_2).pack(anchor=W)
                checkbox_1 = Checkbutton(window, text='Customer Code',
                                        variable=val_3).pack(anchor=W)


                submit = Button(window, text='submit', command=submitform).pack(anchor=W)


                window.mainloop()
        else:
                inva = Toplevel()
                l6 = Label(inva, text = "Invalid Username and Password")
                l6.grid(row = 0, column = 0)
                

root1 = Tk()
root1.title("Login")
l1 = Label(root1, text = "Name: ")
l2 = Label(root1, text = "Password: ")
t1 = Entry(root1)
t2 = Entry(root1, show = "*")
b1 = Button(root1, text = "Register", command = Register)
b2 = Button(root1, text = "Login", command = Login)

l1.grid(row = 0, column = 0)
l2.grid(row = 2, column = 0)
t1.grid(row = 0, column = 2)
t2.grid(row = 2, column = 2)
b1.grid(row = 4, column = 0)
b2.grid(row = 4, column = 2)

root1.mainloop()