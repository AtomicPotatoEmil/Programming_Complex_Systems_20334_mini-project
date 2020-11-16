import socket
import threading
from Game import *


PORT = 80
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

game = Game()

def client_handling(socket_object, address):
    print(f"[NEW CONNECTION] {address} connected")
    connected = True
    while connected:
        message = socket_object.recv(1000).decode(FORMAT)
        print(f"[{address}] {message}")
        game.game(socket_object, FORMAT, message)
    socket_object.close()

def connect_clients():
    try:
        server.listen()
        print(f"Server is waiting for connection on: {SERVER}")
        while True:
            socket_object, address = server.accept()
            thread = threading.Thread(target=client_handling, args=(socket_object, address))
            thread.start()
    except:
        thread.join()
        print("connection lost or could not be established")
def debug(command):
    pass

def test(socket_object, command, bool):
    '''
    Do this to send multiple lines to client

        if command == "count":
        message = ""
        for i in range(10):
            message += str(i)+"\n"
        socket_object.send(str(message).encode(FORMAT))
        message = "" '''

connect_clients()