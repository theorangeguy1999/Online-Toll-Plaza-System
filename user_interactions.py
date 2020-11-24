import mysql.connector

def get_balance(vehicleno):
    DB_connection = mysql.connector.connect(
        host = "localhost",
        user = "tollDB",
        password = "password",
        database = "tollplaza"
    )  

    cursor = DB_connection.cursor()
    cursor.execute("select curr_balance from balance_table where vehicleno = '{}'".format(vehicleno))
    balance = cursor.fetchone()
    if balance == None:
        return -1
    else:
        return balance[0]


def update_balance(vehicleno,update_amount):
    if not update_amount.isnumeric():
        return False
    if int(update_amount) <= 0:
        return False
    current_balance = get_balance(vehicleno)
    
    if current_balance == -1:
        return False
    
    new_balance = current_balance + int(update_amount)
    DB_connection = mysql.connector.connect(
        host = "localhost",
        user = "tollDB",
        password = "password",
        database = "tollplaza"
    ) 
    cursor = DB_connection.cursor()
    cursor.execute("update balance_table set curr_balance = {} where vehicleno = '{}';".format(new_balance,vehicleno))
    DB_connection.commit()

    return True

def reduce_balance(vehicleno,amount):
    current_balance = get_balance(vehicleno)
    new_balance = current_balance - int(amount)
    DB_connection = mysql.connector.connect(
        host = "localhost",
        user = "tollDB",
        password = "password",
        database = "tollplaza"
    ) 
    cursor = DB_connection.cursor()
    cursor.execute("update balance_table set curr_balance = {} where vehicleno = '{}';".format(new_balance,vehicleno))
    DB_connection.commit()

    return True    

def history(vehicleno):
    DB_connection = mysql.connector.connect(
        host = "localhost",
        user = "tollDB",
        password = "password",
        database = "tollplaza"
    ) 

    cursor = DB_connection.cursor()
    cursor.execute("select * from transactions where vehicleno = '{}';".format(vehicleno))
    return cursor.fetchall()

def get_name(vno):
    DB_connection = mysql.connector.connect(
        host = "localhost",
        user = "tollDB",
        password = "password",
        database = "tollplaza"
    )

    cursor = DB_connection.cursor()
    cursor.execute("select f_name from cust_info where vehicleno = '{}'".format(vno))
    result = cursor.fetchone()
    if result == None:
        return ""
    return result[0]    

def get_toll_amount(toll_id , toll_type):
    DB_connection = mysql.connector.connect(
        host = "localhost",
        user = "tollDB",
        password = "password",
        database = "tollplaza"
    )   

    cursor = DB_connection.cursor()
    cursor.execute("select {} from tollstations where toll_id = {}".format(toll_type,toll_id))
    result = cursor.fetchone()
    if result == None:
        return -1
    return result[0] 

def enter_into_it(vehicleno , toll_id , amount):
    DB_connection = mysql.connector.connect(
        host = "localhost",
        user = "tollDB",
        password = "password",
        database = "tollplaza"
    )  

    cursor = DB_connection.cursor()
    cursor.execute("select exists(select * from interim_table where vehicleno = '{}' and toll_id = {} and amount = {} )".format(vehicleno,toll_id,amount))
    if cursor.fetchone()[0] != 0:
        return False

    cursor.execute("insert into interim_table values('{}',{},{})".format(vehicleno,toll_id,amount))
    DB_connection.commit()

    return True

def check_status_from_it(vehicleno , toll_id , amount):
    DB_connection = mysql.connector.connect(
        host = "localhost",
        user = "tollDB",
        password = "password",
        database = "tollplaza"
    )  

    cursor = DB_connection.cursor()
    cursor.execute("select exists(select * from interim_table where vehicleno = '{}' and toll_id = {} and amount = {} )".format(vehicleno,toll_id,amount))
    if cursor.fetchone()[0] != 0:
        return False
    return True

if __name__ == '__main__':
    print(check_status_from_it('trial_no',1,60))