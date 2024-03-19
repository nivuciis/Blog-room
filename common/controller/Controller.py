import json
from common.controller.PostController import PostController 

class Controller:
    
    def __init__(self):
        self.POST_ACTIONS = ["createPost", "likePost"]
        self.postController = PostController()
        
    
    def handleRequest(self, request):
        request = json.loads(request)
        
        if (request['action'] == 'createPost'):
            print(request['post'])
            try:
                response = self.postController.createPost(request['post'])
                return response
            
            except Exception as error:
                print(f'error: {error}')
                return 'server error'
            
        elif (request['action'] == 'getPosts'):
            print(request['page'])
            try:
                response = self.postController.getPosts(request['page'])
                return response
            
            except Exception as error:
                print(f'error: {error}')
                return 'server error'
                
    
      