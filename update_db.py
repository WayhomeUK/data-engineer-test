
import sqlite3
import pandas as pd

def update_db(pandas_df, table, connection):
    """ Upload pandas dataframe to sql database
    """
    pandas_df.to_sql(table, connection, index=False, if_exists='append')
        
