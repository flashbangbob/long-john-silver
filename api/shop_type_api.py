import dbconn

def get_shop_types():
	con = dbconn.get_new_connection()
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT * FROM shop_type")
		rows = cur.fetchall()
		return rows
