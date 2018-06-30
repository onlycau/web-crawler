import pymysql

db=pymysql.connect(host='localhost',user='test',password='password',port=3306)
cursor=db.cursor()
cursor.execute('select version()')
data=cursor.fetchone()
print('database version:',data)
cursor.execute("create database spiders default character set utf8")
db.close()