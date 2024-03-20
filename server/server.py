import socket
from common.model.Post import *
from common.controller.Controller import Controller
from _thread import *
import threading

class Server:
    """
    Classe para representar o servidor.
    """

    def __init__(self, host, port):
        """
        Inicializa o servidor com o endereço e a porta fornecidos.
        """
        self.HOST = host
        self.PORT = port
        self.threadLock = threading.Lock()
        self.controller = Controller()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        """
        Inicia o servidor, configura o soquete e aguarda conexões.
        """
        print(r"""
        ___.   .__                                                        
        \_ |__ |  |   ____   ____           _______  ____   ____   _____  
         | __ \|  |  /  _ \ / ___\   ______ \_  __ \/  _ \ /  _ \ /     \ 
         | \_\ \  |_(  <_> ) /_/  > /_____/  |  | \(  <_> |  <_> )  Y Y  \
         |___  /____/\____/\___  /           |__|   \____/ \____/|__|_|  /
             \/           /_____/                                      \/ 
        """)

        with self._socket as sock:
            sock.bind((self.HOST, self.PORT))
            print(f"Socket binded to port {self.PORT}")

            sock.listen(100)
            print(f"Socket is listening for 100 connections")

            self._init_all_tables()

            while True:
                conn, addr = sock.accept()

                self.threadLock.acquire()
                print('Connected to:', addr[0], ':', addr[1])

                start_new_thread(self.client_thread, (conn,))
                self.threadLock.release()

    def client_thread(self, _socket):
        """
        Thread para manipular as solicitações dos clientes.
        """
        try:
            while True:
                request = _socket.recv(2048).decode()
                if not request:
                    print("Mensagem vazia recebida")
                print("Mensagem recebida:", request, "\n")

                result = self.controller.handle_request(request)

                _socket.sendall(result.encode())
        except (ConnectionAbortedError, ConnectionResetError):
            print("Conexão encerrada pelo cliente.")
        finally:
            _socket.close()

    def _init_all_tables(self):
        """
        Inicializa as tabelas necessárias.
        """
        Post._init_table()
