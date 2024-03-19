import socket
import json
from client.actions.PostActions import PostActions

class Client:
    MENU_CREATE_POST = 1
    MENU_VIEW_POSTS = 2
    MENU_EXIT = 3

    def __init__(self, host, port):
        # Inicializa o cliente com o host e porta fornecidos
        self.HOST = host
        self.PORT = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def print_post(self, post):
        # Imprime detalhes de um post
        print(f"\nUsuário: {post['username']}\nTítulo: {post['title']}          ID do Post: {post['id']}\n{post['body']}\nData: {post['date']}     Hora: {post['time']}")    

    def select_post(self, id, _socket):
        response_json = PostActions.get_post_by_id(_socket, id)
        # response = json.loads(response_json)
        print(response_json)
        # print(response)
        # self.print_post(response['post'])
    
    def create_post(self, _socket):
        # Solicita ao usuário para criar um novo post
        response = PostActions.create_post(_socket)
        print(response)

    def view_posts(self, _socket):
        # Exibe os posts disponíveis e permite navegar entre as páginas
        page = 1
        while True:
            response_json = PostActions.get_posts(_socket, page)
            response = json.loads(response_json)
            
            if response['status'] == 'ok':
                for post in response['posts']:
                    self.print_post(post)

                print("\n1 - Avançar página      2 - Voltar página      3 - Selecionar Post       4 - Voltar")
                choose_in_page_selection = int(input())

                if choose_in_page_selection == 1:
                    page += 1
                elif choose_in_page_selection == 2:
                    if page > 1:
                        page -= 1
                elif choose_in_page_selection == 3:
                    selected_post_id = input('Qual o id do post a selecionar?')
                    self.select_post(selected_post_id, _socket)
                elif choose_in_page_selection == 4:
                    break
            else:
                print(response)
                break

    def action_menu(self, _socket):
        # Exibe o menu de ações disponíveis para o cliente
        print("Escolha entre as opções: ")
        print("\n1 - Criar novo post      2 - Visualizar posts mais recentes       3 - Sair")
        choose = int(input())

        if choose == self.MENU_CREATE_POST:
            self.create_post(_socket)
        elif choose == self.MENU_VIEW_POSTS:
            self.view_posts(_socket)
        elif choose == self.MENU_EXIT:
            self._socket.close()
            exit()
        else:
            print("Opção inválida")

    def start(self):
        # Inicia o cliente e exibe a interface de usuário
        print(r"""
        ___.   .__                                                        
        \_ |__ |  |   ____   ____           _______  ____   ____   _____  
         | __ \|  |  /  _ \ / ___\   ______ \_  __ \/  _ \ /  _ \ /     \ 
         | \_\ \  |_(  <_> ) /_/  > /_____/  |  | \(  <_> |  <_> )  Y Y  \
         |___  /____/\____/\___  /           |__|   \____/ \____/|__|_|  /
             \/           /_____/                                      \/ 
        """)
        
        self._socket.connect((self.HOST, self.PORT))

        while True:
            self.action_menu(self._socket)
            
        self._socket.close()
