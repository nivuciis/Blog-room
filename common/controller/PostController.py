from common.model.Post import Post
import datetime as dt
import sqlite3


class PostController:
    def __init__(self):
        self.dictActionFunction = {"createPost": self.createPost}
        self.dbConn = sqlite3.connect(":memory:")
        
    
    def postMapping(self, obj):
        post = Post(
            id = None,
            title = obj["title"],
            body = obj["body"],
            likes = 0,
            date = f'{dt.datetime.now().date()}',
            time = f'{dt.datetime.now().hour}:{dt.datetime.now().minute}',
            username = obj["username"]
        )
        
    
    # action: createPost 
    def createPost(self, post):
        post = self.postMapping(post)
        
        # validates
        if (len(post.title) == 0 or len(post.title) > 50):
            return "Post title len invalid (must be into 1-50 chars)"
        
        if (len(post.body) == 0 or len(post.body) > 255):
            return "Post body len invalid (must be into 1-255 chars)"
        
        
        
        