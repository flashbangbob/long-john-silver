import MySQLdb as mdb

con = mdb.connect('localhost', 'flashbangbob', '5022', 'main')

def get_corp_for_user_id(id):
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT id, name, ticker, money, share_price FROM corporation WHERE id = %s", id)
		rows = cur.fetchone()
		return rows
