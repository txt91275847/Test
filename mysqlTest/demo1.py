# 导入pymysql模块
import pymysql
# 连接database
conn = pymysql.connect("localhost", "root","1234","mytest")
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
# 定义要执行的SQL语句
sql = """
select * from aaa
"""
# 执行SQL语句
cursor.execute(sql)
# 关闭光标对象
ret = cursor.fetchone()
print(ret)
cursor.close()
# 关闭数据库连接
conn.close()