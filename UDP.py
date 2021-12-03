import logging
import socket
import multiprocessing
import threading
import sys
import time

__author__ = "Ejie Emmanuel Ebuka"

# UDP socket

"""
User Datagram Protocol (UDP) is a communication protocol that primarily used for establishing
low-latency and loss-tolerating connections between applications on the internet.
It speeds up transmissions by enabling the transfer of data before an agreement is
provided by the receiving party.
"""

logging.basicConfig(format="%(levelname)s - %(asctime)s - %(message)s", datefmt='%H:%M:%S', level=logging.DEBUG)

# Multiprocess socket
def make_sock(ip="localhost", port=10, sender=False):
    process = multiprocessing.current_process().name
    logging.info(f'{process} : starting...')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = (ip, port)
    if sender:
        logging.info(f'{process} : starting to send')
    else:
        logging.info(f'{process} : binding to {ip} - port : {port}')
        sock.bind(address)
    with sock:
        while True:
            if sender:
                logging.info(f'{process} : sending...')
                sock.sendto(b'Hello UDP, is Me', address)
                time.sleep(1)
            else:
                data, addr = sock.recvfrom(1024)
                logging.info(f'{process} : from {addr} = {data}')

def main():
    broadcast = multiprocessing.Process(target=make_sock, kwargs={'sender':True}, daemon=True, name="Broadcaster")
    listener = multiprocessing.Process(target=make_sock, kwargs={'sender':False}, daemon=True, name="Listener")
    broadcast.start()
    listener.start()
    timer = threading.Timer(5, sys.exit, [0])
    timer.start()


if __name__ == "__main__":
    main()