import mysql.connector

#host, database, username , password

conn = mysql.connector.connect(host = 'localhost',database = 'PythonAutomation',
                        user = 'root', password = 'root')
print(conn.is_connected())