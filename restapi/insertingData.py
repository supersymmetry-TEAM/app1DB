import sqlite3
import ast
def insert_data(data):
    for i in range(1000):
        bp = data[i]
        c.execute(ap+bp)

  
with open('~/Documents/restApi/restApi/restapi/NEW-000-267.txt', 'r') as f:
    mylist = ast.literal_eval(f.read())

ap = "insert or ignore into api_fooddatas values"
conn = sqlite3.connect("db.sqlite3")
# Autocommit 사용시:
# conn = sqlite3.connect("test.db", isolation_level=None)
print(len(mylist))
# mylist[265][270]= "(562270, '원일 참 맛기름', '혼합식용유', '원일식품', '20070109', '땅콩향키베이스,식용유,참깨향,참깨분말,참깨,참깨추출물,참깨향,참깨추출물,옥수수오일', '20060221842', '2006022184213')"
c = conn.cursor()

# insert into user values (1, 'devakuma', 25, 'Seoul');.
for j in range(len(mylist)):
    for i in range(1000):
        bp = mylist[j][i]
        c.execute(ap+bp)
        print(str(j)+"and"+str(i))

conn.commit()
conn.close()
f.close()