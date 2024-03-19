import select
import socket
import json
import sys
import threading

from client.actions.PostActions import PostActions
from common.model.Post import *


class Client:

    
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def printPost(self, post):
        print(f"\nUsuário: {post['username']}\nTítulo: {post['title']}\n{post['body']}\nData: {post['date']}     Hora: {post['time']}")    
    
    def actionMenu(self, _socket):
        print("Escolha entre as opções: ")
        print("\n1 - Criar novo post      2 - Visualizar posts mais recentes       3 - Sair")
        choose = int(input())
        
        match choose:
            case 1:
                response = PostActions.createPost(_socket)
                print(response)
            case 2:
                page = 1
                responseJson = PostActions.getPosts(_socket, page)
                response = json.loads(responseJson)
                
                
                if (response['status'] == 'ok'):
                    for post in response['posts']:
                        self.printPost(post)
                
                while True:
                    print("\n1 - Avançar página      2 - Voltar página       3 - Voltar")
                    choose_in_page_selection = int(input())
                    
                    if (choose_in_page_selection == 1):
                        page = page + 1
                        response = PostActions.getPosts(_socket, page)
                        print(response)
                    elif (choose_in_page_selection == 2):
                        page = page - 1
                        response = PostActions.getPosts(_socket, page)
                        print(response)
                    elif (choose_in_page_selection == 3):
                        break       
            case 3:
                self._socket.close()
                exit()
    
    def start(self):
        
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
            self.actionMenu(self._socket)
            
        self._socket.close()
        
        