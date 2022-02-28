import sqlite3
db_name=r'Store_db.db'
bogla=sqlite3.connect(db_name)
curs=bogla.cursor()
sql3=f"SELECT product_name,price FROM products WHERE product_name like '%p%'"
curs.execute(sql3)
