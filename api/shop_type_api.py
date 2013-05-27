import MySQLdb as mdb

con = mdb.connect('localhost', 'flashbangbob', '5022', 'main')

def get_shop_types():
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT * FROM shop_type")
		rows = cur.fetchall()
		return rows
