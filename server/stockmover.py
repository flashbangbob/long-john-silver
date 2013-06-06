import dbconn
import time

#UPDATE STOCKS
con = dbconn.get_new_connection()
for x in range(0,12):
    with con:
        cur = con.cursor()
        cur.execute("UPDATE corporation SET share_price = round(share_price * (1 + (((RAND() - 0.5) + (momentum / 250)) / 1000)), 2)")
    time.sleep(5)