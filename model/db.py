import pymysql
class DbConnection:
    def __init__(self):
        self.conn=None
        self.cursor=None

    def connect(self):
        self.conn=pymysql.connect(
                        host='127.0.0.1',
                        user='root',
                        password='root',
                        port=3306,
                        database='sc',
                        charset='utf8'
                    )
        self.cursor=self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

