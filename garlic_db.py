import sqlite3    

# criação da database 

db_con = sqlite3.connect('garlic-db.db')

print("Database is working")

# criação da database para guardar os dados dos usuários

db_con.execute(''' CREATE TABLE IF NOT EXISTS USERS(ID INT PRIMARY KEY    NOT NULL,
                                                    NAME TEXT             NOT NULL,
                                                    AGE INT               NOT NULL,
                                                    EMAIL TEXT            NOT NULL,
                                                    TYPE INT(1)           NOT NULL)''')
                                                    
# comando INSERT para adicionar valores na table                                                    
                                      
db_con.execute("INSERT INTO USERS (ID, NAME, AGE, EMAIL, TYPE) \
    VALUES (1, 'Joana Serafina dos Santos', 18, 'joanadossantos@edu.br', 1)")  

# comando SELECT para criar variável e guardar esses valores na forma de row 

db_cursor = db_con.execute("SELECT ID, NAME, AGE, EMAIL, TYPE from USERS") 

# rodamos o for-in na row 'db_cursor' e printamos os valores para teste (primeiro indice = indice 0)

for row in db_cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
                                      
db_con.close()                                      
                                      