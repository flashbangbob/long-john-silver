import MySQLdb as mdb
import shop_api
import dbconn

def get_corp_by_id (id):
    con = dbconn.get_new_connection()
    with con:
        cur = con.cursor()
        cur.execute("SELECT id, name, ticker, money, share_price FROM corporation WHERE id = %s", id)
        rows = cur.fetchone()
        rows['shops'] = shop_api.get_shops_by_corp_id(rows['id'])
        return rows
