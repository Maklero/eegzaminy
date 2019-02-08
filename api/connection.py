import mysql.connector
from data.data import data


def connect():
    try:
        return mysql.connector.connect(
            host=data['host'],
            user=data['user'],
            passwd=data['passwd'],
            database=data['database']
        )
    except Exception as err:
        print(err)


try:
    def mysqlQuery(query, dictionary=True):
        mydb = connect()
        con = mydb.cursor(dictionary=dictionary)
        con.execute(query)
        res = con.fetchall()
        con.close()
        return res


    def mysqlExecute(query):
        mydb = connect()
        con = mydb.cursor()
        con.execute(query)
        mydb.commit()
        con.close()
        return

except Exception as error:
    print(error)
