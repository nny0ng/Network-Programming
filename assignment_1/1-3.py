import argparse, socket, random

MAX_BYTES = 65535

def server(interface, port): #server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #socket setting
    sock.bind((interface, port)) #socket binding
    sock.listen(1) #socket listening
    while True:
        print('Waiting to accept a new connection')
        sc, sockname = sock.accept() #client accept
        print('We have accepted a connection from', sockname)
        start = sc.recv(MAX_BYTES).decode('utf-8') #game start message
        if(start == "start."): #if "start."
            randnum = random.randint(1, 10) #randnom (1~10)
            print("rand number: ", randnum)
            sc.sendall(b'guess a number between 1 to 10') #send a message
            for i in range(0, 5): #client has 5 attemps
                rerandnum = sc.recv(MAX_BYTES).decode('utf-8') #client's guessnum
                if(rerandnum == str(randnum)): #success
                    sc.sendall(b'Congratulations you did it.')
                    break
                elif(int(rerandnum) < randnum):
                    sc.sendall(b'You guessed too small!')
                elif(int(rerandnum) > randnum):
                    sc.sendall(b'you Guessed too high!')
        sc.close() #fin

def client(host, port): #client
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket
    sock.connect((host, port)) #conect to server
    start = input('input "start.": ') #to start game
    if(start == "start."): #if "start."
        sock.sendall(b'start.') #send to server
        for i in range(0, 6): #until 6 reason: if 5th attempt is success then have to print conguratulation
            data = sock.recv(MAX_BYTES) #receive serever's message
            decode_data = data.decode('utf-8') #decoding
            print(decode_data) #print of game message
            if(i == 5): break #if 5th attempt is success, have to print a message and just fin
            elif(decode_data == "Congratulations you did it."): break #if success, fin
            else: #wrong
                guessnum = input('guess num: ')
                sock.sendall(guessnum.encode('utf-8'))
    sock.close() #fin

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=8000,
                        help='TCP port (default 8000)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)