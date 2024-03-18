import sys
from server.server import Server
from client.client import Client

def startServer(host, port):
    server = Server(host, port)
    server.start()

def startClient(host, port):
    client = Client(host, port)
    client.start()

def Main():
    
    # Checks if args are passed
    argsSize = len(sys.argv)

    if (argsSize != 4):
        sys.exit("Correct usage of program: python y.py EXEC_TYPE IP_ADDR PORT")

    # Checks the type of execution

    execType = sys.argv[1]
    
    host = sys.argv[2]
    port = int(sys.argv[3])

    if (execType == "-s"):
        startServer(host, port)
    elif (execType == "-c"):
        startClient(host, port)
    else:
        sys.exit("EXEC_TYPE must be -s for server or -c for client")
    
    

if __name__ == '__main__':
    Main()