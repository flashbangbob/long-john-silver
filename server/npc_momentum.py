import dbconn

#UPDATE STOCKS
con = dbconn.get_new_connection()
with con:
    cur = con.cursor()
    cur.execute("UPDATE corporation SET momentum = momentum + (CASE WHEN (RAND() * 10 >= 9) THEN 1 WHEN (RAND() * 10 <= 1) THEN -1 ELSE 0 END) WHERE is_npc = 1")