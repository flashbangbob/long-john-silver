import MySQLdb as mdb
import shop_api

con = mdb.connect('localhost', 'flashbangbob', '5022', 'main')

def get_corp_for_user_id(id):
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT id, name, ticker, money, share_price FROM corporation WHERE id = %s", id)
		rows = cur.fetchone()
		rows['shops'] = shop_api.get_shops_by_corp_id(rows['id'])
		return rows
