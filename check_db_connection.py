import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='addressbook')

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()
