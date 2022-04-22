import dbconnection
connection = dbconnection.getconnection()
cursor = connection.cursor()

username = input("Enter your username: ")
email = input("Enter your email address: ")
password = input("Enter your password: ")
user_id = input("Enter your user_id: ")

try:
    # cursor = connection.cursor()
    sql = "UPDATE tbl_user SET `username`= %s , `email`= %s , `password`= %s WHERE user_id = %s"
    cursor.execute(sql, (username, email, password, user_id))
    connection.commit()

finally:
    connection.close()