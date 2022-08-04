import argparse
import asyncio
import random

@asyncio.coroutine
def handle_conversation(reader, writer):
    address = writer.get_extra_info('peername')
    print('Accepted connection from {}'.format(address))
    while True:
        start = yield from reader.read(4096)
        start = start.decode('utf-8')
        if start == "start":
            randnum = random.randint(1, 10)
            print("rand num: ", randnum)
            writer.write(b'guess a number between 1 to 10')
            for i in range(0, 5):
                answer = yield from reader.read(4096)
                answer = answer.decode('utf-8')
                print("answer: ", answer)
                if answer == str(randnum):
                    writer.write(b'Congratulations you did it.')
                    print("end")
                    break
                elif int(answer) < randnum:
                    writer.write(b'You guessed too small!')
                elif int(answer) > randnum:
                    writer.write(b'You guessed too high!')
        else: break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='asyncio server using coroutine')
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-p', metavar='port', type=int, default=1060, help='TCP port (default 1060)')
    args = parser.parse_args()
    address = (args.host, args.p)
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(handle_conversation, *address)
    server = loop.run_until_complete(coro)
    print('Listening at {}'.format(address))
    try:
        loop.run_forever()
    finally:
        server.close()
        loop.close()