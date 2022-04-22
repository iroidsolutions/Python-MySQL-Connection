import dbconnection
connection = dbconnection.getconnection()
cursor = connection.cursor()

username = input("Enter your username: ")
email = input("Enter your email address: ")
password = input("Enter your password: ")

try:
    # cursor = connection.cursor()
    sql = "INSERT INTO tbl_user (`username`, `email`, `password`) VALUES (%s, %s, %s)"
    cursor.execute(sql, (username, email, password))
    connection.commit()

finally:
    connection.close()