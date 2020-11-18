import socket

PORT = 80
CLIENT = input("Type server id: ")
ADDRESS = (CLIENT, PORT)
FORMAT = "utf-8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


def send_and_receive(message):
    msg = message.encode(FORMAT)
    client.send(msg)

    print(client.recv(1000).decode(FORMAT))

while True:
    print("\n Type info to see your command options")
    send_message = input("Type command: ")
    if send_message == "":
        send_message = " "
    send_and_receive(send_message)