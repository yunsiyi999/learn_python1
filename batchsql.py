#coding=utf8
import pymysql



database=pymysql.connect(host='192.168.4.13',port=3308,user='sit_nono_app',passwd='csstbnonobank@2016',charset='utf8')
cursor=database.cursor() #游标

#sql="update nonobank_app.user_buy_product set end_date='2018-04-24' where pay_amount='600.000000' and product_id='37430'" #招财卡资产到期批量改时间
sql="update nonobank_app.user_product set status='1' where product_code='NN0018' and created_date='2018-04-20 21:00:00'"
sql="update"
#invest_end_date='2018-04-24 19:00:00'
try:
    cursor.execute(sql)

    database.commit()
    results=cursor.fetchall()

except Exception as e:
    database.rollback()
else:
    print("pass")
finally:
    database.close()
