import mysql.connector

def admin_login(id,password):
    if not id.isnumeric():
        return False

    DB_connection = mysql.connector.connect(
        host = "localhost",
        user = "tollDB",
        password = "password",
        database = "tollplaza"
    )

    cursor = DB_connection.cursor()
    
    cursor.execute("select password from admin_info where id = {}".format(id))
    db_pass = cursor.fetchone()
    if db_pass == None:
        return False
    if password == db_pass[0]:
        return True

    else:
        return False


def op_login(id,password):
    if not id.isnumeric():
        return False

    DB_connection = mysql.connector.connect(
        host = "localhost",
        user = "tollDB",
        password = "password",
        database = "tollplaza"
    )

    cursor = DB_connection.cursor()
    cursor.execute("select password from operator_info where id = {}".format(id))
    db_pass = cursor.fetchone()
    if db_pass == None:
        return False
    if password == db_pass[0]:
        return True

    else:
        return False

def customer_login(vno,password):
    DB_connection = mysql.connector.connect(
        host = "localhost",
        user = "tollDB",
        password = "password",
        database = "tollplaza"
    )

    cursor = DB_connection.cursor()
    cursor.execute("select password from cust_info where vehicleno = '{}'".format(vno))
    db_pass = cursor.fetchone()
    if db_pass == None:
        return False
    if password == db_pass[0]:
        return True

    else:
        return False

if __name__ == "__main__":
    if(op_login("1",'password')):
        print("Log in successful")
    else:
        print("Log in unsuccessful")