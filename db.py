import pymysql

def get_connection():
    return pymysql.connect(
        host="db-flask-server.cpgcgoyqc8fb.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="admin123",
        database="usersdb"
    )
