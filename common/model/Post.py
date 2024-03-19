import sqlite3

'''
    PostJson structure:
'''


class Post:
    def __init__(self, id, title, body, likes, date, time, username):
        self.id = id
        self.title = title
        self.body = body
        self.likes = likes
        self.date = date
        self.time = time
        self.username = username
    
    def _initTable():
        dbConn = sqlite3.connect("database.db", check_same_thread=False)
        cur = dbConn.cursor()
              
        try:
            cur.execute("CREATE TABLE posts(id INTEGER PRIMARY KEY, title TEXT, body TEXT, likes INT, date TEXT, time TEXT, username TEXT)")
            cur.close()
            dbConn.close()
        except:
            print("Post table already exists or cannot create")
            
            
        
        
        
    
    
            