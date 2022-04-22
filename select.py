import dbconnection
connection = dbconnection.getconnection()
cursor = connection.cursor()

sql = "SELECT * FROM tbl_user"
cursor.execute(sql)

rows = cursor.fetchall()

for row in rows:
    print(row)
    print(" ----------- ")
    print("ID: " , row['user_id'])
    print("username: ", row["username"])
    print("email: ", row["email"])
    print("password: ", row["password"])

connection.commit()