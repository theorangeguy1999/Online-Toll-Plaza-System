import mysql.connector
from tkinter import messagebox

def register_admin(f_name,l_name,phno,password):
    DB_connection = mysql.connector.connect(
        host = "localhost",
        user = "tollDB",
        password = "password",
        database = "tollplaza"
    )
    if(not phno.isnumeric() or len(phno) != 10):
        messagebox.showerror("Phone number error","Phone number should be of CHANGEHERE 10 \n and should only contain digits")
        return 0
    
    if(not( len(password) > 4 and len(password) < 15)):
        messagebox.showerror("Password error","Size of password should be more than 4\nand less than 15")
        return 0

    cursor = DB_connection.cursor()
    cursor.execute("insert into admin_info(f_name,l_name,phno,password) values('{}','{}','{}','{}')".format(f_name,l_name,phno,password))#insert into admininfo() values())
    DB_connection.commit()
    cursor.execute("select max(id) from admin_info")
    return cursor.fetchone()[0]

def register_op(f_name,l_name,phno,password):
    if(not phno.isnumeric() or len(phno) != 10):
        messagebox.showerror("Phone number error","Phone number should be of CHANGEHERE 10 \n and should only contain digits")
        return 0
    
    if(not( len(password) > 4 and len(password) < 15)):
        messagebox.showerror("Password error","Size of password should be more than 4\nand less than 15")
        return 0

    DB_connection = mysql.connector.connect(
        host = "localhost",
        user = "tollDB",
        password = "password",
        database = "tollplaza"
    )

    cursor = DB_connection.cursor()
    cursor.execute("insert into operator_info(f_name,l_name,phno,password) values('{}','{}','{}','{}');".format(f_name,l_name,phno,password))#insert into admininfo() values())
    DB_connection.commit()

    cursor.execute("select max(id) from operator_info")
    return cursor.fetchone()[0]

def register_customer(vno,f_name,l_name,phno,password):
    if not vno.isalnum():
        messagebox.showerror("Vehicle Number error","Vehicle number can not contain special characters")
        return False

    if(not phno.isnumeric() or len(phno) != 10):
        messagebox.showerror("Phone number error","Phone number should be of CHANGEHERE 10 \n and should only contain digits")
        return False
    
    if(not( len(password) > 4 and len(password) < 15)):
        messagebox.showerror("Password error","Size of password should be more than 4\nand less than 15")
        return False

    DB_connection = mysql.connector.connect(
        host = "localhost",
        user = "tollDB",
        password = "password",
        database = "tollplaza"
    )

    cursor = DB_connection.cursor()
    cursor.execute("select exists(select * from cust_info where vehicleno = '{}');".format(vno))
    if cursor.fetchone()[0] != 0:
        return False
    
    cursor.execute("insert into cust_info values('{}','{}','{}','{}','{}');".format(vno,f_name,l_name,phno,password))#insert into admininfo() values())
    DB_connection.commit()
    cursor.execute("insert into balance_table(vehicleno) values('{}');".format(vno))
    DB_connection.commit()

    return True

def register_tollstation(ow_cost, tw_cost):
    if (not ow_cost.isnumeric()) or (not tw_cost.isnumeric()):
        return None
    DB_connection = mysql.connector.connect(
        host = "localhost",
        user = "tollDB",
        password = "password",
        database = "tollplaza"
    )

    cursor = DB_connection.cursor()
    cursor.execute("insert into tollstations(one_way_cost,two_way_cost) values({},{}));".format(ow_cost,tw_cost))  
    DB_connection.commit()

    cursor.execute("select max(id) from tollstations")
    return cursor.fetchone()[0]

if __name__ == "__main__":
    print(register_customer("MP04SR2690","Testing_fname","Testing_lname","8827999765","password"))
    pass
