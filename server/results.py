import dbconn
import time

#UPDATE STOCKS
con = dbconn.get_new_connection()
for x in range(0,6):
    with con:
        cur = con.cursor()
        cur.execute("UPDATE corporation SET share_price = share_price * (1 + ((RAND() - .5) / 1000))")
    time.sleep(10)


'''
SELECT corporation_id, COUNT( * ) AS count_owned, MAX( share_price ) AS current_share_price, COUNT( * ) * MAX( share_price ) AS wealth
FROM shares
INNER JOIN corporation ON corporation.id = shares.corporation_id
WHERE shares.owning_corporation_id =1
GROUP BY shares.corporation_id
LIMIT 0 , 30
'''