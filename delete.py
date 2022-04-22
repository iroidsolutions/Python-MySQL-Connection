import dbconnection
connection = dbconnection.getconnection()
cursor = connection.cursor()

user_id = input("Enter your user_id: ")
try:
    # cursor = connection.cursor()
    sql = "DELETE FROM tbl_user WHERE user_id = %s"
    cursor.execute(sql, (user_id))
    connection.commit()

finally:
    connection.close()