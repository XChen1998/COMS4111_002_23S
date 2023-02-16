import pymysql


class StudentResource:

    def __init__(self):
        pass

    @staticmethod
    def get_connection():

        conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="dbuserdbuser",
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn

    @staticmethod
    def get_students():

        conn = StudentResource.get_connection()
        cur = conn.cursor()

        sql = "select * from db_book.student"
        res = cur.execute(sql)
        result = cur.fetchall()

        return result
