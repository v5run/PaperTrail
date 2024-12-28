from sk import postgreSQL_user, postgreSQL_pass
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

# user_id should be a primary key
def add_receipt(user_id, shop_name, date, total, items):
    """
    Adds a receipt to the database with associated items.
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
                    "INSERT INTO receipt_items (id, item_name, price) VALUES (%s, %s, %s);",
                    (receipt_id, item["item"], item["price"])
                )

            conn.commit()
            print(f"Receipt added with ID: {receipt_id}")

        except Exception as e:
            print(f"Error adding receipt: {e}")
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
        finally:
            cursor.close()
            conn.close()


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