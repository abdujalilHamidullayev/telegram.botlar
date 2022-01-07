'''import sqlite3
db_name=r'Store_db.db'
bogla=sqlite3.connect(db_name)
cur=bogla.cursor()
sql=f"INSERT INTO products(c_id,product_name, price)"
    f"VALUES (5, 'baliq_goshti',180000)"
cur.execute(sql)
bogla.commit()
print("Tugadi!")'''
'''import sqlite3
db_name=r'Store_db.db'
bogla=sqlite3.connect(db_name)
cur=bogla.cursor()
sql=f"UPDATE products SET price=4000 where product_name='lactel' "
cur.execute(sql)
bogla.commit()
print("Tugadi!")
'''
"""  
import sqlite3
db_name=r'Store_db.db'
bogla=sqlite3.connect(db_name)
cur=bogla.cursor()
sql=f"DELETE FROM products WHERE product_name"
cur.execute(sql)
bogla.commit()
print("Tugadi!")
"""
"""
import sqlite3
db=r'Store_db.db'
conn=sqlite3.connect(db)
curs=conn.cursor()
sql=f"SELECT p_id , c_id , product_name , MAX (price) FROM products"
curs.execute(sql)
malumot = curs.fetchall()

for product in malumot:
    print(f"{product[0]} {product[1]} {product[3]}")
"""

import sqlite3
db=r'Store_db.db'
conn=sqlite3.connect(db)
curs=conn.cursor()
sql=f"SELECT count(c_id) from products where c_id=1"
curs.execute(sql)
malumot=curs.fetchall()
print(malumot)