# ssteps to install mysql:
# install from mysql official site
#  pip install mysql
# pip install mysql-connector or
# pip install mysql-connector-python
import mysql
import mysql.connector

dataBase= mysql.connector.connect(
    host="localhost",
    user= 'root',
    passwd='Priyanshi123!!',
    # default is caching_sha2_password, which is not supported by the connector
    auth_plugin='mysql_native_password'
)

#prepare a cursor object

cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE userDB")

print("All Done!")