import socket
import threading
import protocol

PORT = 8888
clients = {}


class Server:
    def __init__(self, port):
        self._server_socket = socket.socket()
        self._server_socket.bind(('', port))
        self._server_socket.listen()

    def _connect_to_client(self):
        """  Connecting to the client and return the client socket   """
        (client_socket, client_address) = self._server_socket.accept()
        print('Connected with ' + client_address[0] + ':' + str(client_address[1]))
        # register client
        clients[client_socket.fileno()] = client_socket
        return client_socket

    @staticmethod
    def client_listen(client_socket):
        """ wait to massages from the client """
        while True:
            # Check if protocol is OK, e.g. length field OK
            #try:
                #valid_protocol, msg = protocol.get_msg(client_socket)
            #except ConnectionResetError:
                #break

            #if valid_protocol:
            msg = client_socket.recv(1024).decode()

            Server.send_msg(msg)

            #else:
                # prepare proper error to client
                #response = 'Packet not according to protocol'
                # send to client
                #client_socket.send(protocol.create_msg(response))
                # Attempt to clean garbage from socket

    @staticmethod
    def send_msg(msg):
        for client in clients.values():
            try:
                print(msg)
                client.send(msg.encode())
            except:
                print('looks like I can\'t send this msg to this client')

    def handle_client(self):
        """ Handles the client connection and start a thread """
        client_socket = self._connect_to_client()
        t = threading.Thread(target=Server.client_listen, args=(client_socket,))
        t.start()


def main():
    # creating a server socket
    server = Server(PORT)
    # connecting to new clients for ever:
    while True:
        server.handle_client()


if __name__ == '__main__':
    main()
