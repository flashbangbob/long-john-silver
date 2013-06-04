import MySQLdb as mdb
import corp_api
import shares_api
import dbconn

def buy_stock(userid, quantity, buyingCorpId):
	buyerCorp = corp_api.get_corp_for_user_id(userid)
	buyerMoney = buyerCorp["money"]

	stockCorp = corp_api.get_corp_for_user_id(buyingCorpId)
	sharePrice = stockCorp["share_price"]

	totalAmount = sharePrice * quantity

	if buyerMoney >= totalAmount:
		con = dbconn.get_new_connection()
		with con:
			cur = con.cursor()
			for x in range(0,quantity):
	        	cur.execute("INSERT INTO shares VALUES (%s, %s, NOW())", (buyingCorpId, userId))
	        cur.execute("UPDATE corporation SET money = money - %s WHERE id = %s", (totalAmount, userid))
			cur.execute("UPDATE corporation SET momentum  = momentum + %s WHERE id = %s", (quantity, buyingCorpId))

def sell_stock(userid, quantity, sellingCorpId):
	buyerShares = shares_api.get_shares_for_corp_id(userid)

	shareQuantity = buyerShares[sellingCorpId]["quantity"] 

	stockCorp = corp_api.get_corp_for_user_id(sellingCorpId)
	sharePrice = stockCorp["share_price"]

	totalAmount = sharePrice * quantity

	if shareQuantity >= quantity:
		con = dbconn.get_new_connection()
		with con:
			cur = con.cursor()
			for x in range(0,quantity):
	        	cur.execute("DELETE FROM shares WHERE corporation_id = %s AND owning_corporation_id = %s LIMIT 1", (sellingCorpId, userId))
	        cur.execute("UPDATE corporation SET money = money + %s WHERE id = %s", (totalAmount, userid))
			cur.execute("UPDATE corporation SET momentum = momentum - %s WHERE id = %s", (quantity, sellingCorpId))

		

