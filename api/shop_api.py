import MySQLdb as mdb

con = mdb.connect('localhost', 'flashbangbob', '5022', 'main')

def get_shops_by_corp_id(id):
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT corporation_id, name, shop_type_id, product_id, product_start, product_complete FROM shop WHERE corporation_id = %s", id)
		rows = cur.fetchall()
		return rows
