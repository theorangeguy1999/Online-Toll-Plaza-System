import mysql.connector
from datetime import datetime
from user_interactions import get_balance,update_balance,reduce_balance

def get_op_name(id):
    DB_connection = mysql.connector.connect(
        host = "localhost",
        user = "tollDB",
        password = "password",
        database = "tollplaza"
    )

    cursor = DB_connection.cursor()
    cursor.execute("select f_name from operator_info where id = {}".format(id))
    result = cursor.fetchone()
    if result == None:
        return ""
    return result[0]

def get_from_it(id):
    if(not id.isnumeric()):
        return None
    DB_connection = mysql.connector.connect(
        host = "localhost",
        user = "tollDB",
        password = "password",
        database = "tollplaza"
    )    

    cursor = DB_connection.cursor()
    cursor.execute("select vehicleno,amount from interim_table where toll_id = {};".format(id))
    result = cursor.fetchone()
    if result == None:
        return None
    return result

def transaction(vehicleno, opid, tid, amount):
    DB_connection = mysql.connector.connect(
        host = "localhost",
        user = "tollDB",
        password = "password",
        database = "tollplaza"
    ) 

    dt = datetime.now()
    dt = str(dt)[:19]
    cursor = DB_connection.cursor()
    cursor.execute("Insert into transactions(vehicleno,op_id,toll_id,amount,date_time) values('{}',{},{},{},'{}');".format(vehicleno,opid,tid,amount,dt))
    DB_connection.commit()
    cursor.execute("Delete from interim_table where vehicleno = '{}' and toll_id = {}".format(vehicleno,tid))
    DB_connection.commit()

    reduce_balance(vehicleno,amount)

    cursor.execute("select max(transaction_id) from transactions")
    new_transaction_id = cursor.fetchone()
    if new_transaction_id == None:
        return None
    return new_transaction_id[0]   

if __name__ == "__main__":
    print(get_from_it(1))
    now = datetime.now()
    print(str(now)[:19])