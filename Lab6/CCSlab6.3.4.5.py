import sqlite3
# 连接数据库(如果不存在则创建)
conn = sqlite3.connect('ProcessData.db')
# 创建游标
cursor = conn.cursor()

# 查询数据
sql = "SELECT * FROM PDATA"
values = cursor.execute(sql)
for d in values:
    print('id:', d[0])
    print('p_data:', d[1])


cursor.execute(sql)
# 提交事务
conn.commit()

print("SELECT successfully")

# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭连接
conn.close()
