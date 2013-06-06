import MySQLdb as mdb
import dbconn

def get_all_shares_for_corp_id(id):
    con = dbconn.get_new_connection()
    with con:
        cur = con.cursor()
        cur.execute("""SELECT corporation_id, count(*) as quantity, avg(purchase_price) as purchase_price, 
                        c.share_price, (c.share_price - avg(purchase_price)) * count(*) as net_gain
                        FROM shares s
                        JOIN corporation c on c.id = s.corporation_id WHERE owning_corporation_id = %s GROUP BY corporation_id""", id)
        rows = cur.fetchall()
        return rows

def get_corp_shares_for_corp_id(id, corpId):
    con = dbconn.get_new_connection()
    with con:
        cur = con.cursor()
        cur.execute("SELECT count(*) as quantity FROM shares WHERE owning_corporation_id = %s AND corporation_id = %s", (id, corpId))
        row = cur.fetchone()
        return row

