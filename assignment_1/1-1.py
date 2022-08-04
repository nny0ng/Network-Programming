import socket

request_text = """\
GET /iss-pass.json?lat={}&lon={} HTTP/1.1\r\n\
Host: api.open-notify.org\r\n\
User-Agent: hayeong\r\n\
Connection: close\r\n\
\r\n\
"""

def geocode(lat, lon): #use lat, lon
    unencrypted_sock = socket.socket() #socket
    unencrypted_sock.connect(('api.open-notify.org', 80)) #connect to site
    request = request_text.format(lat, lon) #insert lat, lon to request form
    unencrypted_sock.sendall(request.encode('ascii')) #encoding
    raw_reply = b''
    while True:
        more = unencrypted_sock.recv(4096)
        if not more:
            break
        raw_reply += more
    print(raw_reply.decode('utf-8')) #decoding and print

if __name__ == '__main__':
    geocode('45', '180')