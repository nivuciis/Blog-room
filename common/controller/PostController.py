from common.model.Post import Post
import datetime as dt
import sqlite3
import json


class PostController:
    
    def __init__(self):
        self.dictActionFunction = {"createPost": self.createPost}
        self.dbDriver = sqlite3.connect("database.db", check_same_thread=False)
             
    
    def postMapping(self, obj):
        post = Post(
            id = None,
            title = obj["title"],
            body = obj["body"],
            likes = 0,
            date = f'{dt.datetime.now().date()}',
            time = f'{dt.datetime.now().hour:02}:{dt.datetime.now().minute:02}',
            username = obj["username"]
        )
        
        return post
        
    
    # action: createPost 
    def createPost(self, post):
        post = self.postMapping(post)
        print(post.__dict__)
        
        # validates
        if (len(post.title) == 0 or len(post.title) > 50):
            return "Post title len invalid (must be into 1-50 chars)"
        
        if (len(post.body) == 0 or len(post.body) > 255):
            return "Post body len invalid (must be into 1-255 chars)"
        
        cursor = self.dbDriver.cursor()
        
        cursor.execute("INSERT INTO posts VALUES(?, ?, ?, ?, ?, ?, ?)",
                       [None, post.title, post.body, post.likes, post.date,
                       post.time, post.username])
        
        self.dbDriver.commit()
        
        post_id = cursor.lastrowid
        
        action = {"action": "serverResponse"}
        status = {"status": "created"}
        
        responseJson = json.dumps(action | status | {'post_id': post_id})
        
        return responseJson
        
    def getPosts(self, page_number):
        ITEMS_PER_PAGE = 10
        
        cursor = self.dbDriver.cursor()
        
        offset = (page_number - 1) * ITEMS_PER_PAGE
        
        cursor.execute(f"SELECT * FROM posts LIMIT {ITEMS_PER_PAGE} OFFSET {offset}")
        
        rows = cursor.fetchall()
        posts = []
        
        for row in rows:
            # Obtendo os nomes das colunas
            columns = [col[0] for col in cursor.description]

            # Criar um dicionário usando os nomes das colunas como chaves
            row = dict(zip(columns, row))
            posts.append(row)
        
        print(posts)
        
        cursor.close()
        
        action = {"action": "serverResponse"}
        status = {"status": "ok"}
        
        responseJson = json.dumps(action | status | {'posts': posts})
        
        return responseJson
        
        
        
        
        
        
        