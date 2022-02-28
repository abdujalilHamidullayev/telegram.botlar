import sqlite3
db_name=r'shop.db'
bogla=sqlite3.connect(db_name)
cursor=bogla.cursor()
sql2=f"SELECT  category_name FROM category"
cursor.execute(sql2)
malumot=cursor.fetchall()
print(malumot)