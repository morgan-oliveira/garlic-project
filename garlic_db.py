import sqlite3    
from tkinter import *

# criação da database 

def init_db_func():

    db_con = sqlite3.connect('garlic-db.db')

    print("Database is working")

# criação de table para guardar os dados dos funcionários

    db_con.execute(''' CREATE TABLE IF NOT EXISTS FUNC (ID INT PRIMARY KEY      NOT NULL,
                                                        NAME TEXT               NOT NULL,
                                                        AGE INTEGER             PRIMARY KEY,
                                                        FUNC_CODE CHAR(10)      NOT NULL) ''')

# criação da database para guardar os dados dos usuários

 #   db_con.execute(''' CREATE TABLE IF NOT EXISTS USERS(ID INT PRIMARY KEY    NOT NULL,
 #                                                       NAME TEXT             NOT NULL,
 #                                                       AGE INT               NOT NULL,
 #                                                       EMAIL TEXT            NOT NULL,
 #                                                       TYPE INT              NOT NULL)''')
                                                    
# comando INSERT para adicionar valores na table                                                    
                                      
    db_con.execute("INSERT INTO FUNC (ID, NAME, AGE, FUNC_CODE) \
    VALUES        (1, 'Joana Serafina dos Santos', 18, 't$j28x!2/#')")  
    
                     
    db_con.close()                                      
    
    
init_db_func()                              