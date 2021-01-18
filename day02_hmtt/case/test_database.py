'''
    目标：自动化测试中操作项目数据库
    案例：
        判断用户id（1）是否收藏了id为2的文章
        表格中1表示未收藏   0表示收藏
'''
#导包pymysql
import  pymysql
#获取连接对象
conn=pymysql.connect(host="192.168.0.105",port=3306,user="zhangle",passwd="102325",database="books",charset="utf8")
#获取游标对象
cursor=conn.cursor()
#执行方法 sql
sql='select is_deleted from news_collection where user_id=1 and article_id=2'
cursor.execute(sql)
#获取结果并进行断言 0-收藏
# print(cursor.fetchone())
result=cursor.fetchone()#返回值为元组
assert 0==result[0]
#关闭游标对象
cursor.close()
#关闭连接对象
conn.close()