# import sqlite3
#
# conn = sqlite3.connect("pizza2.db")
# cursor = conn.cursor()
#
# cursor.execute("SELECT * FROM Payment")
# row = cursor.fetchall()
#
# for row in row:
#     print(row)
# conn.close()
# import sqlite3
#
# conn = sqlite3.connect("pizza2.db")
# cursor = conn.cursor()
#
# # Retrieve the last customer ID, sorting by numeric part
# cursor.execute("SELECT Customer_ID FROM CustomersInformation ORDER BY CAST(substr(Customer_ID, 4) AS INTEGER) DESC LIMIT 1")
# row = cursor.fetchone()
#
# if row:
#     last_customer_id = row[0]
#     print("Last Customer ID:", last_customer_id)
# else:
#     print("No data in the table")
#
# conn.close()


# import mysql.connector
#
# # Connect to the database
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="password",
#   database="pizza"
# )
# # Perform database operations
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM Items")
# myresult = mycursor.fetchall()
#
# for row in myresult:
#   print(row)
#
# # Close the database connection
# mydb.close()

import hashlib

# Encode the input string as bytes
input_string = '0be64ae89ddd24e225434de95d501711339baeee18f009ba9b4369af27d30d60'
input_bytes = input_string.encode('utf-8')

# Create a SHA256 hash object and update it with the input bytes
hash_object = hashlib.sha256()
hash_object.update(input_bytes)

# Get the hexadecimal representation of the hash value
hash_value = hash_object.hexdigest()

print(hash_value)