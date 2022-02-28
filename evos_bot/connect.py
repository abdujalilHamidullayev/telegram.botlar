import sqlite3

db_name=r'baza.db'

def add_users(user_id,first_name,tel_number):
    # conn=sqlite3.connect(db_name)
    # cursor=conn.cursor()
    # sql=f"INSERT INTO users('user_id','first_name','tel_number')"\
    #     f"values ({user_id},'{first_name}','{tel_number}')"
    # cursor.execute(sql)
    # conn.commit()
    pass

def get_menu1():
    connect=sqlite3.connect(db_name)
    cursor=connect.cursor()
    sql=f"SELECT * FROM Category"
    cursor.execute(sql)
    malumot=cursor.fetchall()
    return malumot

def get_lavash(category_id):
    connect=sqlite3.connect(db_name)
    cursor=connect.cursor()
    sql=f"SELECT * FROM products WHERE cotegory_id={category_id}"
    cursor.execute(sql)
    malumot=cursor.fetchall()