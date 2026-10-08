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
        
def get_item_by_item_id(item_id):
    connection=DatabaseConnection()
    if isinstance(connection, str):
            print(connection)
            return False
    else:
        try:
            cursor=connection.cursor(dictionary=True)
            query="""SELECT items.*, users.name AS owner_name
                    FROM items
                    JOIN users ON items.owner_id = users.user_id
                    WHERE items.item_id = %s"""
            cursor.execute(query,(item_id,))
            result=cursor.fetchone()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            return f"something went wrong in get item by item_id : {e}"
def create_offer(item_id,bidder_id,amount,start_date,end_date,message):
    connection=DatabaseConnection()
    if isinstance(connection, str):
            print(connection)
            return False
    else:
        try:
            cursor=connection.cursor()
            query="""INSERT INTO offers
                    (item_id, bidder_id, amount, start_date,end_date,message)
                    VALUES (%s, %s, %s, %s, %s,%s)"""
            cursor.execute(query,(item_id,bidder_id,amount,start_date,end_date,message))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            return f"something went wrong in create_offer {e}"
    

def get_offer_by_item_id_user_id(item_id,bidder_id):
    connection=DatabaseConnection()
    if isinstance(connection, str):
            print(connection)
            return False
    else:
        try:
            cursor=connection.cursor(dictionary=True)
            query="""select * from offers where item_id=%s and bidder_id=%s"""
            cursor.execute(query,(item_id,bidder_id))
            result=cursor.fetchone()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            return f"Something went wrong in get offer by using item_id and user_id {e}"
    