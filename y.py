import sys
from server.server import Server
from client.client import Client

def start_server(host, port):
    server = Server(host, port)
    server.start()

def start_client(host, port):
    client = Client(host, port)
    client.start()

def main():
    # Verifica se há argumentos passados
    args_size = len(sys.argv)

    if args_size != 4:
        sys.exit("Uso correto do programa: python y.py TIPO_EXEC IP_ADDR PORTA")

    # Verifica o tipo de execução
    exec_type = sys.argv[1]
    host = sys.argv[2]
    
    try:
        port = int(sys.argv[3])
    except ValueError:
        sys.exit("A PORTA deve ser um número inteiro válido")

    if exec_type == "-s":
        start_server(host, port)
    elif exec_type == "-c":
        start_client(host, port)
    else:
        sys.exit("TIPO_EXEC deve ser -s para servidor ou -c para cliente")

if __name__ == '__main__':
    main()
