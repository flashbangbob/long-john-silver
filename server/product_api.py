import dbconn

def get_products():
	con = dbconn.get_new_connection()
	with con:
		cur = con.cursor()
		cur.execute("SELECT * FROM product")
		rows = cur.fetchall()
		return rows

def get_product_by_id(id):
	con = dbconn.get_new_connection()
	with con:
		cur = con.cursor()
		cur.execute("SELECT * FROM product WHERE id = %s", id)
		rows = cur.fetchone()
		return rows
