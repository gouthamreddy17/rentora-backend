from database.connection import DatabaseConnection

def get_email_from_db(email):
    connection=DatabaseConnection()
    if isinstance(connection, str):
        print(connection)
        return None
    else:
        try:
            cursor=connection.cursor(dictionary=True)
            query="""select * from users where email=%s"""
            cursor.execute(query,(email,))
            result=cursor.fetchone()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            return f"SOMETHING WENT WRONG IN GET EAMIL FROM DB {e}"

def insert_user_to_db(name,email,phone,city,password):
    connection=DatabaseConnection()
    if isinstance(connection, str):
            print(connection)
            return False
    else:
        try:
            cursor=connection.cursor()
            query="""INSERT INTO users
                    (name, email, password,  phone, city)
                    VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(query,(name,email,phone,city,password))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            return f"SOMETHING WENT WRONG IN INSERT USER INTO DATABASE {e}"
    
def get_user_by_email(email):
    connection=DatabaseConnection()
    if isinstance(connection, str):
            print(connection)
            return False
    else:
        try:
            cursor=connection.cursor(dictionary=True)
            query="""select * from users where email=%s"""
            cursor.execute(query,(email,))
            result=cursor.fetchone()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            return f"Something went wrong in get user by email {e}"
        
def get_items_from_db():
    connection=DatabaseConnection()
    if isinstance(connection, str):
            print(connection)
            return False
    else:
        try:
            cursor=connection.cursor(dictionary=True)
            query="""select * from items"""
            cursor.execute(query)
            result=cursor.fetchall()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            return f"something went wrong in get items from db: {e}"
        
        