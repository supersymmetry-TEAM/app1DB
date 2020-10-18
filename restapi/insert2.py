import sqlite3
import ast
import data

data=data.d()
print(len(data))


#################################################
# # insert into user values (1, 'devakuma', 25, 'Seoul');.
ap = "insert or ignore into api_kitostandard values"
def insert_data(data):
    for i in range(len(data)):
        bp = str(data[i])
        c.execute(ap+bp)
conn = sqlite3.connect("/home/kms/Documents/restApi/restapi/db.sqlite3")
c = conn.cursor()

insert_data(data)

conn.commit()
conn.close()
