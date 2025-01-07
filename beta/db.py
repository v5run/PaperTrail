from beta.sk import postgreSQL_user, postgreSQL_pass
import psycopg2

# Database connection
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="papertrail",
            user=postgreSQL_user,
            password=postgreSQL_pass,
            host="localhost",
            port="5432"
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None
    
def userID(email):
    """
    Checks if a user exists in the users table.
    """
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT user_id FROM users WHERE email = %s;", (email,))
            user_id = cursor.fetchone()
            if user_id:
                print(f"User exists with ID: {user_id[0]}")
                return user_id[0]
            else:
                print("User does not exist.")
                return None
        except Exception as e:
            print(f"Error checking if user exists: {e}")
            print(f"Email: {email}")
        finally:
            cursor.close()
            conn.close()

def add_user(name, email, password):
    """
    Adds a user to the users table.
    """
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s) RETURNING user_id;", (name, email, password))
            user_id = cursor.fetchone()[0]
            conn.commit()
            print(f"User added with ID: {user_id}")
            return user_id
        except Exception as e:
            print(f"Error adding user: {e}")
            print(f"Username: {name}, Email: {email}, Password: {password}")
        finally:
            cursor.close()
            conn.close()

# user_id should be a primary key
def add_receipt(user_id, shop_name=None, date=None, total=None, items=[]):
    """
    Adds a receipt to receipts and receipts items.
    """
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()

            # Insert the receipt
            cursor.execute(
                "INSERT INTO receipts (user_id, shop_name, date, total) VALUES (%s, %s, %s, %s) RETURNING id;",
                (user_id, shop_name, date, total)
            )
            receipt_id = cursor.fetchone()[0]

            # Insert the receipt items
            for item in items:
                cursor.execute(
                    "INSERT INTO receipt_items (receipt_id, item_name, price) VALUES (%s, %s, %s);",
                    (receipt_id, item["item"], item["price"])
                )

            conn.commit()
            print(f"Receipt added with ID: {receipt_id}")

        except Exception as e:
            print(f"Error adding receipt: {e}")
            print(f"UserID: {user_id}, Shop: {shop_name}, Date: {date}, Total: {total}, Items: {items}")
        finally:
            cursor.close()
            conn.close()


# READ: Get All Receipts for a User
def get_receipts_for_user(user_id):
    """
    Fetches all receipts and associated items for a specific user.
    """
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()

            # Fetch receipts
            cursor.execute("SELECT * FROM receipts WHERE user_id = %s;", (user_id,))
            receipts = cursor.fetchall()

            # Fetch receipt items
            for receipt in receipts:
                receipt_id = receipt[0]
                cursor.execute("SELECT item_name, price FROM receipt_items WHERE id = %s;", (receipt_id,))
                items = cursor.fetchall()

                print(f"Receipt ID: {receipt_id}, Shop: {receipt[2]}, Date: {receipt[3]}, Total: {receipt[4]}")
                for item in items:
                    print(f"    Item: {item[0]}, Price: {item[1]}")

        except Exception as e:
            print(f"Error fetching receipts: {e}")
            print(f"UserID: {user_id}")
        finally:
            cursor.close()
            conn.close()

#   Testing
if __name__ == "__main__":
    items = [
        {"item": "Milk", "price": 2.50},
        {"item": "Bread", "price": 1.80},
        {"item": "Eggs", "price": 3.00}
    ]
    add_receipt(user_id=1, shop_name="Walmart", date="2024-12-25", total=7.60, items=items)

    # READ: Get receipts for a user
    print("\nReceipts for User ID 1:")
    get_receipts_for_user(user_id=1)