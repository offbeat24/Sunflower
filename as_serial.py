import asyncio
from time import sleep

import serial_asyncio

class Writer(asyncio.Protocol):
    def connection_made(self, transport):
        """Store the serial transport and schedule the task to send data.
        """
        self.transport = transport
        print('Writer connection created')
        asyncio.ensure_future(self.send())
        print('Writer.send() scheduled')

    def connection_lost(self):
        print('Writer closed')

    async def send(self):
        while True :
            n = "A"
            await asyncio.sleep(0.5)
            self.transport.serial.write(n.encode())
            print(f'Writer sent: {n.encode()}')
        # message = b'1234567890'
        # for b in message:
        #     await asyncio.sleep(0.5)
        #     self.transport.serial.write(bytes([b]))
        #     print(f'Writer sent: {bytes([b])}')
        self.transport.close()

