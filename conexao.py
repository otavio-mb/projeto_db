import mysql
import mysql.connector
 
conn = mysql.connector.connect(
    username = 'otavio',
    host = 'localhost',
    password = 'projeto123',
    db = 'projeto_crud'
)