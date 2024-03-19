import json
from common.controller.PostController import PostController 

class Controller:
    CREATE_POST_ACTION = "createPost"  # Ação para criar um novo post
    GET_POSTS_ACTION = "getPosts"      # Ação para obter os posts
    GET_POST_BY_ID_ACTION = "getPostById"      # Ação para obter os posts
    LIKE_POST_BY_ID_ACTION = "likePostById"      # Ação para obter os posts
    SERVER_ERROR_MESSAGE = "server error"  # Mensagem de erro genérica para erros do servidor

    def __init__(self):
        self.postController = PostController()  # Inicialização do controlador de postagens

    def handle_request(self, request):
        try:
            request_data = json.loads(request)  # Analisa a solicitação JSON
            action = request_data.get('action')  # Obtém a ação da solicitação

            if action == self.CREATE_POST_ACTION:  # Se a ação for criar um post
                post_data = request_data.get('post')  # Obtém os dados do post da solicitação
                if post_data:
                    # Chama o método para criar um novo post e retorna a resposta
                    response = self.postController.create_post(post_data)
                    return response
                else:
                    return self.SERVER_ERROR_MESSAGE  # Retorna uma mensagem de erro se os dados do post estiverem ausentes

            elif action == self.GET_POSTS_ACTION:  # Se a ação for obter os posts
                page = request_data.get('page')  # Obtém o número da página dos posts
                if page is not None:
                    # Chama o método para obter os posts da página especificada e retorna a resposta
                    response = self.postController.get_posts(page)
                    return response
                else:
                    return self.SERVER_ERROR_MESSAGE  # Retorna uma mensagem de erro se o número da página estiver ausente

            elif action == self.GET_POST_BY_ID_ACTION:
                post_id = request_data.get('post_id')
                # print(post_id)
                response = self.postController.get_post_by_id(post_id)
                return response
                ''' if post_id is not None:
                    
                else:
                    return self.SERVER_ERROR_MESSAGE '''
                    
            elif action == self.LIKE_POST_BY_ID_ACTION:
                post_id = request_data.get('post_id')
                response = self.postController.like_post_by_id(post_id)
                return response
            
            else:
                return f"Invalid action: {action}"  # Retorna uma mensagem de erro se a ação for inválida

        except Exception as error:  # Trata exceções
            print(f'Error: {error}')  # Imprime o erro
            action = {"action": "serverResponse"}
            status = {"status": "server error"}
            response_json = json.dumps(action | status)
            return response_json  
