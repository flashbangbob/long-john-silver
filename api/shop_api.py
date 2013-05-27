import MySQLdb as mdb
import product_api

con = mdb.connect('localhost', 'flashbangbob', '5022', 'main')

def get_shops_by_corp_id(id):
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT corporation_id, name, shop_type_id, product_id, product_start, product_complete FROM shop WHERE corporation_id = %s", id)
		rows = cur.fetchall()
		for row in rows:
			if row['product_id']:
				row['product'] = product_api.get_product_by_id(row['product_id'])
			else:
				row['product'] = None
		return rows
