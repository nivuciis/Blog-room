import threading
import socket

HEADER = 64
PORT = 1234
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONECT_MSG = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def clientConect(conection, addr):
    print(f"[NOVA CONEXÃO]{addr} conectado")
    connected = True
    while connected:
        msg_length = conection.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conection.recv(msg_length).decode(FORMAT)
            if msg == DISCONECT_MSG:
                connected = False
            print(f"[{addr}]: {msg}")
    conection.close()

def start():
    server.listen()
    print(f"[ESPERANDO CONEXÕES COM {SERVER}]")
    while True:
        conection, addr = server.accept()
        thread = threading.Thread(target=clientConect, args=(conection, addr))
        thread.start()
        print(f"[CONEXÕES ATIVAS]{threading.active_count() - 1}")

print("Servidor está iniciando...")
start()

