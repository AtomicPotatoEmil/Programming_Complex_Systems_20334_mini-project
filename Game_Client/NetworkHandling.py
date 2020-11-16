import socket

PORT = 80
CLIENT = input("Type server id: ")
ADDRESS = (CLIENT, PORT)
FORMAT = "utf-8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

start_of_game = True

def send_message_to_server(message):
    msg = message.encode(FORMAT)
    client.send(msg)

    print(client.recv(1000).decode(FORMAT))

while True:
    print("\n Type info to see your command options")
    send_message = input("Type command: ")
    if send_message == "":
        send_message = " "
    send_message_to_server(send_message)