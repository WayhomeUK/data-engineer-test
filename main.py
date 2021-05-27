from create_db import create_DB_connection, close_connection
from collect_data_to_df import  convert_dict_dif,replace_city_code, load_data_api2, load_data_api1
from update_db import update_db
from datetime import time
from time import time
import sqlalchemy

"""5 mins = 300 seconds
"""
END_TIME = time() + 300 

DATABASE_LOCATION = "sqlite:///wayhome_db.sqlite"
SQL_TABLE_NAME_1 = "address_transaction"
SQL_TABLE_NAME_2 = "average_transaction_city"


def start():
    import time

    api1_data = {}
    api2_data = {}
    data_dict = convert_dict_dif(load_data_api1(api1_data))
    data2_dict = replace_city_code(convert_dict_dif(load_data_api2(api2_data)))


    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    returned_connection = create_DB_connection()

    update_db(data_dict,SQL_TABLE_NAME_1,engine)
    update_db(data2_dict,SQL_TABLE_NAME_2,engine)

    close_connection(returned_connection)
    time.sleep(30)


"""Pipeline will run for 5 mins
"""
while time() < END_TIME:
    start()      
    print("New Data added!!")

    