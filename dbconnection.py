import pymysql.cursors


def getconnection():
    connection = pymysql.connect(host='localhost', user='root', password='', db='db_python',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    return connection
