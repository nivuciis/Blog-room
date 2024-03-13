import socket

HEADER = 64
PORT = 1234
FORMAT = 'utf-8'
DISCONECT_MSG = "!DISCONNECT"
SERVER = "" #MODIFICAR ESSE CAMPO PARA ENCAIXAR COM IP DO SERVIDOR
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
message = input("")
while(message != "exit"):
    message = input("")
    send(message)
send(DISCONECT_MSG)