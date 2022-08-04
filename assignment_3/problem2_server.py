import random
import asyncio
import time
from datetime import datetime

import zmq
import zmq.asyncio

context = zmq.asyncio.Context()

async def run_server(port=5556):
    sock = context.socket(zmq.PUB)
    sock.bind(f'tcp://*:{port}')
    print("server running --------")
    while True:
        time.sleep(10.0)
        msg = "rand: "+str(random.randint(0, 100))+" / 운동,"+"rand: "+str(random.randint(0, 100))+" / 기술,"+"rand: "+str(random.randint(0, 100))+" / 과학"
        timestamp = datetime.now().strftime('%Y-%m-%d / %H:%M:%S')
        print(msg+"[ "+timestamp+" ]")
        await sock.send_string(msg)

if __name__ == '__main__':
    asyncio.run(run_server())
    context.destroy()