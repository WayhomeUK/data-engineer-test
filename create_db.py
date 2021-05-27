import sqlite3


def create_DB_connection():
    """ Connect to a database and create cursor object for executing SQL statements.
    """
    
    conn = sqlite3.connect('wayhome_db.sqlite')
    print("Connection with database established ..........")
    cursor = conn.cursor()    

    #create tables for variables
    sql_query1 = """
    CREATE TABLE IF NOT EXISTS address_transaction(
        address VARCHAR(200),
        city VARCHAR(200),
        date VARCHAR(200),
        price VARCHAR(200)
    )
    """
    sql_query2 = """
    CREATE TABLE IF NOT EXISTS average_transaction_city(
        city VARCHAR(200),
        date VARCHAR(200),
        price VARCHAR(200)
    )
    """

    cursor.execute(sql_query1) 
    cursor.execute(sql_query2)    
    return conn

def close_connection(conn):
    """ Close connection with the database.
    """
    conn.commit()
    conn.close()

print('database name --wayhome_db.sqlite-- and tables --address_trasaction, average_transaction_city -- created!')



    

    