import sqlite3
db_name=r'baza.db'

def add_users(users_yd,first_name,tel_raqam):
    conn=sqlite3.connect(db_name)
    cursor=conn.cursor()
    sql=f"INSERT INTO users(user_id,first_name,tel_raqam)"\
        f"values ({users_id},'{first_name}','{tel_raqam}')"
    cursor.execute(sql)
    conn.commit()