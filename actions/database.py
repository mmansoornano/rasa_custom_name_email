import mysql.connector

def DataUpdate(Name, Email):
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Myhomieno=1',
        database='rasa_feedback',
        auth_plugin='mysql_native_password'
    )

    mycursor = mydb.cursor()
    #sql = 'CREATE TABLE nameEmail (name VARCHAR(255), email VARCHAR(255));'
    sql = f'INSERT INTO nameemail (name,email) VALUES ("{Name}","{Email}");'

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, 'record inserted')

if __name__=='__main__':
    DataUpdate('Mansoor', 'dfsdf@dgd.com')