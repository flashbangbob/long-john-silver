import MySQLdb as mdb

con = mdb.connect('localhost', 'flashbangbob', '5022', 'main')

def get_products():
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT * FROM product")
		rows = cur.fetchall()
		return rows

def get_product_by_id(id):
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT * FROM product WHERE id = %s", id)
		rows = cur.fetchone()
		return rows
