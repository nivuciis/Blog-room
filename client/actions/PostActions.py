import json
from common.model.Post import Post

class PostActions:

    def createPost(_socket):
        title = input("Selecione o título do post ")
        body = input("Qual o corpo da mensagem ")
        postObj = Post(id=None, title=title, body=body, likes=None, date=None, time=None, username="Test")
        
        action = {"action": "createPost"}
        status = {"status": "request"}
        
        requestJson = json.dumps(action | status | {'post': postObj.__dict__})
        _socket.send(requestJson.encode())
        
        responseJson = _socket.recv(1024).decode()
        ''' response = json.loads(responseJson)
        
        
        if (response['status'] == 'created'):
            return f"Your was succesfully created with ID #{response['id']}"
        elif (response['status' == 'invalid']):
            return response['errorMsg']
        else:
            return 'Server error' '''
            
        return responseJson

    def getPosts(_socket, _page):
        page = {'page': _page}
        action = {"action": "getPosts"}
        status = {"status": "request"}
        
        requestJson = json.dumps(action | status | page)
        _socket.send(requestJson.encode())
        
        responseJson = _socket.recv(1024).decode()
        
        return responseJson
        
