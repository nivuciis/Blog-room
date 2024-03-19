import socket
import json
from common.model.Post import *
from common.controller.Controller import Controller

from _thread import *
import threading

class Server:
    
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.threadLock = threading.Lock()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.controller = Controller()
        
        
    
    def start(self):
        print(r"""
___.   .__                                                        
\_ |__ |  |   ____   ____           _______  ____   ____   _____  
 | __ \|  |  /  _ \ / ___\   ______ \_  __ \/  _ \ /  _ \ /     \ 
 | \_\ \  |_(  <_> ) /_/  > /_____/  |  | \(  <_> |  <_> )  Y Y  \
 |___  /____/\____/\___  /           |__|   \____/ \____/|__|_|  /
     \/           /_____/                                      \/ 
     
     """)
        
        self._socket.bind((self.HOST, self.PORT))
        print(f"Socket binded to port {self.PORT}")
        
        self._socket.listen(100)
        print(f"Socket is listening for 100 conn")
        
        self._initAllTables()
        
        while True:
            conn, addr = self._socket.accept()
            
            self.threadLock.acquire()
            print('Connected to :', addr[0], ':', addr[1])
            
            start_new_thread(self.clientThread, (conn,))
            self.threadLock.release()
            
        self._socket.close()
            
    
    def clientThread(self, _socket):
        
        while True:
            try:
                request = _socket.recv(1024).decode()
                if not request:
                    print("Empty message received, closing connection.")
                    break
                print("Mensagem recebida:", request, "\n")
                
                result = self.controller.handleRequest(request)
                
                _socket.send(result.encode())
            except ConnectionAbortedError:
                print("Conexão encerrada pelo servidor.")
                break
        
    def _initAllTables(self):
        Post._initTable()
        
