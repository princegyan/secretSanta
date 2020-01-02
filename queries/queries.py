import psycopg2
import psycopg2.extras
import os
DATABASE_URL = os.environ['DATABASE_URL']
connection = psycopg2.connect(DATABASE_URL, sslmode='require')
# connection = psycopg2.connect("dbname=secretsanta user=postgres")



def insertuser(name):
    try:
        with connection.cursor() as cursor:
            query = "insert into users(username) values(%s)"
            cursor.execute(sql, (name,))
            connection.commit()
    finally:
        pass

def getnumbers():
    try:
        numbers = []
        with connection.cursor() as cursor:
            query= "select userid from users where removed=0;"
            cursor.execute(query)
            results = cursor.fetchall()
            for i in results:
                numbers.append(i[0])
                
    finally:
            return numbers

def removeuser(number):
    try:
        with connection.cursor() as cursor:
            query = "update users set removed=1 where userid=%s"
            cursor.execute(query, (int(number),))
            connection.commit()
    finally:
        pass
        
def getnamebynumber(number):
    try:
        with connection.cursor() as cursor:
            query= "select username from users where removed=0 and userid=%s;"
            cursor.execute(query, (int(number),))
            results = cursor.fetchone()
    finally:
            return results


if __name__ == "__main__":
    getnamebynumber(3)