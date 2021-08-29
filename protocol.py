def create_msg(data):
    """
    Create a valid protocol message, with length field
    """

    msg = str(len(data)).zfill(4) + data
    return msg.encode()


def recv_all(sock, size):
    data = 0
    while len(data) < size:
        curr = sock.recv(size-len(data)).decode()
        if len(curr) == 0:
            print("Closed connection in the middle!!!!")
            return ''
        data += curr


def get_msg(my_socket):
    """
    Extract message from protocol, without the length field
    If length field does not include a number, returns False, "Error"
    """

    length = recv_all(my_socket, 4)
    if len(length) == 0:
        print('Closed')
        return False, 'Closed'

    try:
        length = int(length)
    except ValueError:
        return False, 'Error'

    msg = recv_all(my_socket, length)
    return True, msg
