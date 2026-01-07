import pymysql

def get_connection():
    return pymysql.connect(
        host="with your db end point",
        user=" your user name",
        password="password",
        database="usersdb"
    )
