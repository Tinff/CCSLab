import sqlite3
# 连接数据库(如果不存在则创建)
conn = sqlite3.connect('ProcessData.db')
print("Open database successfully")
# 创建游标
cursor = conn.cursor()
# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭连接
conn.close()
