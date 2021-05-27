import sqlite3

conn = sqlite3.connect('wayhome_db.sqlite')
  
cur = conn.cursor()

cur.execute("SELECT * from address_transaction")

rows = cur.fetchall()
print("All the transaction and address of the sold property:")
for row in rows:
    print(row)

cur.execute("SELECT * from average_transaction_city")
rows = cur.fetchall()

print("Daily Average for each City of all transactions in the country:")
for row in rows:
    print(row)

conn.close()