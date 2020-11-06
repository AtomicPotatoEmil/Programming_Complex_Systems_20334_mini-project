import socket
import threading
from Game_Server.GameLoop import *

game_loop = GameLoop()
NUMBER_OF_BYTES_TO_ACCEPT = 64
PORT = 80
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_SIGNAL = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)



def client_handling(socket_object, address):
    print(f"[NEW CONNECTION] {address} connected")
    connected = True
    while connected:
        message_length = socket_object.recv(NUMBER_OF_BYTES_TO_ACCEPT).decode(FORMAT)
        if message_length:
            message_length = int(message_length)
            message = socket_object.recv(message_length).decode(FORMAT)
            print(f"[{address}] {message}")
            game_loop.game_loop(message)
            socket_object.send(game_loop.current_command.encode(FORMAT))
    socket_object.close()

    pass

def connection_start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        socket_object, address = server.accept()
        thread = threading.Thread(target=client_handling, args=(socket_object, address))
        thread.start()
    pass

connection_start()