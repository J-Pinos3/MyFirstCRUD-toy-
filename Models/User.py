class User():
    def __init__(self, conn):
        self.conn=conn
        with self.conn.cursor() as cursor:
            sql=""" CREATE TABLE IF NOT EXISTS user
                (
                    user_name VARCHAR(30) NOT NULL PRIMARY KEY,
                    user_password VARCHAR(20) NOT NULL
                )
                """
            cursor.execute(sql)
            self.conn.commit()

    def getUser(self,user,password):
        with self.conn.cursor() as cursor:
            sql="""SELECT user_name FROM user WHERE user_name = %s AND user_password = %s"""
            cursor.execute(sql,(user,password))
            result=cursor.fetchone()
            return result
