import mysql.connector

def search_results(column, value):
    DB_connection = mysql.connector.connect(
        host = "localhost",
        user = "tollDB",
        password = "password",
        database = "tollplaza"
    )
    
    cursor = DB_connection.cursor()
    cursor.execute("select * from transactions where {} = '{}'".format(column,value))
    results = cursor.fetchall()
    return results

if __name__ == "__main__":
    print(search_results('vehicleno','trial'))    