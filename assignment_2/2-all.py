import json
import zlib
import socket
import ssl

class Solution():
    
    def special_bits(self, L=1, R=2, k=1):
        num = -2
        # Write your code between start and end for solution of problem 1
        # Start
        num = 0
        for i in range(0, k):
            num = num + 2**i
        if not L <= num <= R:
            num = -1
        # End
        return num

    def toggle_string(self, S):
        s = ""
        # Write your code between start and end for solution of problem 2
        # Start
        s_num = list(S.encode('ASCII'))
        for i in s_num:
            if 65 <= i <= 90:
                i = i + 32
                s = s + ('%c' %i)
            elif 97 <= i <= 122:
                i = i - 32
                s = s + ('%c' %i)
        # End
        return s

    def send_message(self, message):
        message = self.to_json(message)
        message = self.encode(message)
        message = self.compress(message)
        return message

    def recv_message(self, message):
        message = self.decompress(message)
        message = self.decode(message)
        message = self.to_python_object(message)
        return message
    
    # String to byte
    def encode(self, message):
        # Write your code between start and end for solution of problem 3
        # Start
        message = message.encode('utf-8')
        return message
        # End
        
    
    # Byte to string
    def decode(self,message):
        # Write your code between start and end for solution of problem 3
        # Start
        message = message.decode('ascii')
        return message
        # End 

    # Convert from python object to json string
    def to_json(self, message):
        # Write your code between start and end for solution of problem 3
        # Start
        message = json.dumps(message)
        return message
        # End 

    # Convert from json string to python object
    def to_python_object(self, message):
        # Write your code between start and end for solution of problem 3
        # Start
        message = json.loads(message)
        return message
        # End 
    
    # Returns compressed message 
    def compress(self, message):
        # Write your code between start and end for solution of problem 3
        # Start
        message = zlib.compress(message)
        return message
        # End 

    # Returns decompressed message
    def decompress(self, compressed_message):
        # Write your code between start and end for solution of problem 3
        # Start
        compressed_message = zlib.decompress(compressed_message)
        return compressed_message
        # End 


    def client(self, host, port, cafile=None):
        # Write your code between start and end for solution of problem 4
        # Start
        cert = "" # Variable to store the certificate received from server
        cipher = "" # Variable to store cipher used for connection
        msg = "" # Variable to store message received from server
        purpose = ssl.Purpose.SERVER_AUTH
        context = ssl.create_default_context(purpose, cafile=cafile)
        raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        raw_sock.connect((host, port))
        ssl_sock = context.wrap_socket(raw_sock, server_hostname=host)
        cipher_info = ssl_sock.cipher()
        cipher = cipher_info[0]
        cert = ssl_sock.getpeercert()
        msg = ssl_sock.recv(1024)
        msg = msg.decode('utf-8')
        # End
        return cert, cipher, msg
    
    

    
