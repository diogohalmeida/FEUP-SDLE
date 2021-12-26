import asyncio
import logging
from threading import Thread
from server import KServer
from kademlia.network import Server

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log = logging.getLogger('kademlia')
log.setLevel(logging.DEBUG)
log.addHandler(handler)

BOOTSTRAP_NODES = [("127.0.0.1",5000)]



async def run():
    server = Server()
    await server.listen(8469)
    await server.bootstrap([('127.0.0.1', 8468)])
    await server.set("key", "val")
    server.stop()

asyncio.run(run())


def main():

    server = KServer("127.0.0.1", 6000)
    loop = server.start(BOOTSTRAP_NODES)

    loop.set_debug(True)

    threads = [
        Thread(target=loop.run_forever, daemon=True),
        # Thread(target=loop.run_forever, daemon=True)
    ]

    for t in threads:
        t.start()


if __name__ == '__main__':
    # main()
    pass