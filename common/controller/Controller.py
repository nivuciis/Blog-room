import json
from common.controller.PostController import PostController 

class Controller:
    def __init__(self):
        self.POST_ACTIONS = ["createPost", "likePost"]
        self.postControler = PostController()
    
    def handleRequest(self, request):
        request = json.loads(request)
        
        if (request['action'] == 'createPost'):
            print(request['post'])
            self.postControler.createPost(request['post'])
    
      