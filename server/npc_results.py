import dbconn

#UPDATE STOCKS
con = dbconn.get_new_connection()
with con:
    cur = con.cursor()
    cur.execute("UPDATE corporation SET share_price = round(share_price * (1 + ((RAND() - .5) / 10)), 2) where is_npc = 1")
