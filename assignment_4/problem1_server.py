import csv
from wsgiref.simple_server import make_server

def app(environ, start_response):
    key = environ.get('QUERY_STRING', '/') # get key

    file = open('problem1_csv.csv') # open file to read
    definition = ''
    csv_reader = csv.reader(file) # read file
    for row in csv_reader:
        if row[0] == key: # find key's row
            definition = row[1] # store in definition
            break

    if definition == '': # none keyword
        definition = 'keyword is not exist!'

    status = '200 OK'
    response_headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, response_headers)
    response = [definition.encode('utf-8')]  # response to client

    return response

if __name__ == '__main__':
    httpd = make_server('', 8000, app)
    host, port = httpd.socket.getsockname()
    print('Serving on', host, 'port', port)
    httpd.serve_forever()