import MySQLdb as mdb
import dbconn

def get_shares_for_corp_id(id):
	con = dbconn.get_new_connection()
	with con:
		cur = con.cursor()
		cur.execute("SELECT corporation_id, count(*) as quantity FROM shares WHERE owning_corporation_id = %s GROUP BY corporation_id", id)
		rows = cur.fetchall()
		return rows
