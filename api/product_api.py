import MySQLdb as mdb

con = mdb.connect('localhost', 'flashbangbob', '5022', 'main')

def get_products():
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT * FROM product")
		rows = cur.fetchall()
		return rows
