import json
from common.model.Post import Post

class PostActions:

    @staticmethod
    def create_post(socket):
        try:
            title = input("Selecione o título do post: ")
            body = input("Qual o corpo da mensagem: ")
            
            post_obj = Post(id=None, title=title, body=body, likes=None, date=None, time=None, username="Test")
            
            action = {"action": "createPost"}
            status = {"status": "request"}
            
            request_json = json.dumps(action | status | {'post': post_obj.__dict__})
            socket.send(request_json.encode())
            
            response_json = socket.recv(1024).decode()
            
            return response_json
        except Exception as e:
            return str(e)

    @staticmethod
    def get_posts(socket, page):
        try:
            page_data = {'page': page}
            action = {"action": "getPosts"}
            status = {"status": "request"}
            
            request_json = json.dumps(action | status | page_data)
            socket.send(request_json.encode())
            
            response_json = socket.recv(1024).decode()
            
            return response_json
        except Exception as e:
            return str(e)
    
    @staticmethod
    def get_post_by_id(socket, id):
        try:
            action = {"action": "getPostById"}
            status = {"status": "request"}
            post_id = {'post_id': id}
            
            request_json = json.dumps(action | status | post_id)
            socket.send(request_json.encode())
            
            response_json = socket.recv(1024).decode()
            
            return response_json
        except Exception as e:
            return str(e)