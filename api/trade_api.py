import MySQLdb as mdb
import corp_api
import shares_api
import dbconn

def buy_stock(buyingCorpId, targetCorpId, quantity):
    buyerCorp = corp_api.get_corp_by_id(buyingCorpId)
    buyerMoney = buyerCorp['money']

    targetCorp = corp_api.get_corp_by_id(targetCorpId)
    targetCorpSharePrice = targetCorp['share_price']

    totalAmount = targetCorpSharePrice * int(quantity)

    if buyerMoney >= totalAmount:
        con = dbconn.get_new_connection()
        with con:
            cur = con.cursor()
            for x in range(0,quantity):
                cur.execute("INSERT INTO shares VALUES (null, %s, %s, %s, NOW())", (targetCorpId, buyingCorpId, targetCorpSharePrice))
            cur.execute("UPDATE corporation SET money = money - %s WHERE id = %s", (totalAmount, buyingCorpId))
            cur.execute("UPDATE corporation SET momentum = momentum - %s WHERE id = %s", (quantity, targetCorpId))

def sell_stock(sellingCorpId, targetCorpId, quantity):
    sellerCorp = corp_api.get_corp_by_id(sellingCorpId)
    sellerMoney = sellerCorp['money']

    sellerShares = shares_api.get_corp_shares_for_corp_id(sellingCorpId, targetCorpId)
    quantityOfShares = sellerShares['quantity']

    targetCorp = corp_api.get_corp_by_id(targetCorpId)
    targetCorpSharePrice = targetCorp['share_price']

    totalAmount = targetCorpSharePrice * int(quantity)

    if quantityOfShares >= quantity:
        con = dbconn.get_new_connection()
        with con:
            cur = con.cursor()
            cur.execute("DELETE FROM shares WHERE corporation_id = %s AND owning_corporation_id = %s LIMIT %s", (targetCorpId, sellingCorpId, quantity))
            cur.execute("UPDATE corporation SET money = money + %s WHERE id = %s", (totalAmount, sellingCorpId))
            cur.execute("UPDATE corporation SET momentum = momentum + %s WHERE id = %s", (quantity, targetCorpId))
        

