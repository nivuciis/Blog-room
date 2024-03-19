from common.model.Post import Post
import datetime as dt
import sqlite3
import json

class PostController:
    ITEMS_PER_PAGE = 10
    DATABASE_FILE = "database.db"

    def __init__(self):
        self.dict_action_function = {"createPost": self.create_post}
        self.db_driver = sqlite3.connect(self.DATABASE_FILE, check_same_thread=False)
    
    def post_mapping(self, obj):
        post = Post(
            id=None,
            title=obj["title"],
            body=obj["body"],
            likes=0,
            date=f'{dt.datetime.now().date()}',
            time=f'{dt.datetime.now().hour:02}:{dt.datetime.now().minute:02}',
            username=obj["username"]
        )
        return post

    def create_post(self, post_data):
        post = self.post_mapping(post_data)
        # Validations
        if not 0 < len(post.title) <= 50:
            return "Post title length invalid (must be between 1-50 chars)"
        if not 0 < len(post.body) <= 255:
            return "Post body length invalid (must be between 1-255 chars)"
        
        try:
            cursor = self.db_driver.cursor()
            cursor.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?, ?, ?, ?)",
                           [post.title, post.body, post.likes, post.date, post.time, post.username])
            self.db_driver.commit()
            post_id = cursor.lastrowid
            cursor.close()

            action = {"action": "serverResponse"}
            status = {"status": "created"}
            response_json = json.dumps(action | status | {'post_id': post_id})
            return response_json
        except sqlite3.Error as e:
            return f"Error: {e}"
        
    def get_posts(self, page_number):
        try:
            offset = (page_number - 1) * self.ITEMS_PER_PAGE
            cursor = self.db_driver.cursor()
            cursor.execute("SELECT * FROM posts ORDER BY id DESC LIMIT ? OFFSET ?", [self.ITEMS_PER_PAGE, offset])
            rows = cursor.fetchall()
            posts = [dict(zip([col[0] for col in cursor.description], row)) for row in rows]
            cursor.close()

            action = {"action": "serverResponse"}
            status = {"status": "ok"}
            response_json = json.dumps(action | status | {'posts': posts})
            return response_json
        except sqlite3.Error as e:
            action = {"action": "serverResponse"}
            status = {"status": "server error"}
            response_json = json.dumps(action | status)
            return response_json

    def get_post_by_id(self, post_id):
        try:
            cursor = self.db_driver.cursor()
            cursor.execute("SELECT * FROM posts WHERE id = ?", (int(post_id),))
            row = cursor.fetchone()
            post = dict(zip([col[0] for col in cursor.description], row))
            
            action = {"action": "serverResponse"}
            status = {"status": "ok"}
            response_json = json.dumps(action | status | {'post': post})
            return response_json
        
        except Exception as e:
            print(e)
            action = {"action": "serverResponse"}
            status = {"status": "server error"}
            response_json = json.dumps(action | status)
            return response_json    
        
    def like_post_by_id(self, post_id):
        try:
            cursor = self.db_driver.cursor()
            cursor.execute("UPDATE posts SET likes = likes + 1 WHERE id = ?", (int(post_id),))
            
            action = {"action": "serverResponse"}
            status = {"status": "updated"}
            response_json = json.dumps(action | status)
            return response_json
        
        except Exception as e:
            print(e)
            action = {"action": "serverResponse"}
            status = {"status": "server error"}
            response_json = json.dumps(action | status)
            return response_json