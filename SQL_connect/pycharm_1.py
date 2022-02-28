import sqlite3
db_name=r'magazin.db'
connect=sqlite3.connect(db_name)
cursor=connect.cursor()
sql1=f"SELECT * FROM products WHERE price<1000"
cursor.execute(sql1)
xabar=cursor.fetchall()


for product in xabar:
    print(product)