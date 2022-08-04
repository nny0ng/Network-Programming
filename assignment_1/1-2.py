import argparse, socket

MAX_BYTES = 65535

def server(port): #server
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket
    sock.bind(('127.0.0.1', port)) #socket binding
    print('Listening at {}'.format(sock.getsockname())) #listening
    while True:
        data, address = sock.recvfrom(MAX_BYTES) #receive message
        text = data.decode('ascii') #message decoding
        print('The client at {} says {!r}'.format(address, text)) #client's message print
        if(len(data)%2 == 0): #even
            text = 'data size is {} bytes long'.format(len(data))
        else: #odd
            text = 'Error 403 Forbidden.'
        data = text.encode('ascii') #message encoding
        sock.sendto(data, address) #message send

def client(port): #client
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket
    data = input("input message: ").encode() #data encoding
    sock.sendto(data, ('127.0.0.1', port)) #send to server
    data, address = sock.recvfrom(MAX_BYTES) #receive server's message
    text = data.decode('ascii') #message decoding
    print(text) #print

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=8000, help='UDP port (default 8000)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)