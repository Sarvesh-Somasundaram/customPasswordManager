import psycopg2
import clipboard

def store_passwords(password, user_email, username, url, app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO manager (password, email, username, url, app_name) VALUES (%s, %s, %s, %s, %s)"""
        record_to_insert = (password, user_email, username, url, app_name)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)

def connect():
    try:
        connection = psycopg2.connect(database='passwordmanager', user = 'postgres', password = 'red123')
        return connection
    except (Exception, psycopg2.Error) as error:
        print(error)

def find_password(app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT password FROM manager WHERE app_name = '""" + app_name + "'"
        cursor.execute(postgres_select_query, app_name)
        connection.commit()
        result = cursor.fetchone()
        clipboard.copy(result[0])
    
    except (Exception, psycopg2.Error) as error:
        print(error)
