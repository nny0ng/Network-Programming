import sys
import asyncio
import zmq
import zmq.asyncio
from datetime import datetime

context = zmq.asyncio.Context()

async def run_client(port=5556, zf=0):
    if zf == 0:
        print("wrong category")
        return
    elif zf == "sports" or "technology" or "science":
        sub = zf
    sock = context.socket(zmq.SUB)
    sock.connect(f'tcp://localhost:{port}')
    sock.setsockopt_string(zmq.SUBSCRIBE, '')
    while True:

        msg = await sock.recv_string()
        sports, tech, science = msg.split(",")

        if sub == "sports":
            timestamp = datetime.now().strftime('%Y-%m-%d / %H:%M:%S')
            print("sports article [", timestamp, "] >>", sports)
        elif sub == "technology":
            timestamp = datetime.now().strftime('%Y-%m-%d / %H:%M:%S')
            print("technology article [", timestamp, "] >>", tech)
        elif sub == "science":
            timestamp = datetime.now().strftime('%Y-%m-%d / %H:%M:%S')
            print("science article [", timestamp, "] >>", science)
        else:
            print("none categories")
            break

    sock.close()

if __name__ == '__main__':
    asyncio.run(run_client(zf=sys.argv[1]))
    context.destroy()