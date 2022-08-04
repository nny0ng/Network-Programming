import argparse
import socket

def client(address, cause_error=False):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    data = input('input "start": ')
    if data == "start":
        sock.sendall(data.encode('utf-8'))
    for i in range(0, 6):
        data = sock.recv(4096)
        if not data:
            raise EOFError('socket closed')
        decode_data = data.decode('utf-8')
        print(decode_data)
        if i == 5: break
        elif decode_data == "Congratulations you did it.": break
        else:
            guess_num = input('guess num: ')
            sock.sendall(guess_num.encode('utf-8'))
    sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Example client')
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-e', action='store_true', help='cause an error')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    address = (args.host, args.p)
    client(address, args.e)