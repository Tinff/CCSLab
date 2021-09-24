import sqlite3
# 连接数据库(如果不存在则创建)
conn = sqlite3.connect('ProcessData.db')
# 创建游标
cursor = conn.cursor()

# 写入数据
sql = "INSERT INTO PDATA(p_data) VALUES('1234567')"
cursor.execute(sql)
# 提交事务
conn.commit()
print("INSERT INTO PDATA successfully")

# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭连接
conn.close()
