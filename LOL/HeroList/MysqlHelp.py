#coding=utf-8
import MySQLdb

try:
    connect = MySQLdb.connect(host='localhost',port=3306,db='LOL',user='root',passwd='123456789',charset='utf8')
    con = connect.cursor()
    sql_insert = 'insert into HeroList_heroinfo values (0,"诺克萨斯之手",1,"旋风斧",6)'
    con.execute(sql_insert)
    connect.commit()
    con.close()
    connect.close()


except Exception,e:
    e.message
