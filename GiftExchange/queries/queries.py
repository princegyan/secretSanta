import psycopg2
import psycopg2.extrasimport os
# DATABASE_URL = os.environ['DATABASE_URL']
# connection = psycopg2.connect(DATABASE_URL, sslmode='require')
connection = psycopg2.connect("dbname=kwikly user=postgres")



def insertuser(name):
    try:
        with connection.cursor() as cursor:
            query = "insert into users(username) values(%s)"
            cursor.execute(sql, (name,))
            connection.commit()

def getnumbers():
    try:
        with connection.cursor() as cursor:
            query= "select userid from users where removed=0;"
            cursor.execute(query)
            results = cursor.fetchall()
            print(results)
        finally:
            return results

def removeuser(number):
    try:
        with connection.cursor() as cursor:
            query = "update users set removed=1 where userid=%s"
            cursor.execute(query, (int(number),))
            connection.commit()
            

def getnamebynumber(number):
    try:
        with connection.cursor() as cursor:
            query= "select username from users where removed=0 and userid=%s;"
            cursor.execute(query, (int(number),))
            results = cursor.fetchall()
            print(results)
        finally:
            return results
    