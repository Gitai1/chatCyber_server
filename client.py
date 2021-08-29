import socket
import protocol

IP = "127.0.0.1"
PORT = 8888


def handle_server_response(my_socket):
    """
    Receive the response from the server and handle it, according to the request
    """
    valid, response = protocol.get_msg(my_socket)
    if not valid:
        print('There was an error')
        return
    print(response)


def main():
    # open socket with the server
    my_socket = socket.socket()
    my_socket.connect((IP, PORT))
    # print instructions

    # loop until user requested to exit
    while True:
        print('\nWelcome to friends info:')
        cmd = input("Enter command:\n")

        packet = protocol.create_msg(cmd)
        my_socket.send(packet)
        handle_server_response(my_socket)


if __name__ == '__main__':
    main()
