import logging
import select
import socket

__author__ = "Ejie Emmanuel Ebuka"

# Blocking and Non-blocking sockets
# Blocking socket stops
# Non-blocking socket runs in the background

"""
ready_to_read, ready_to_write, in_error
"""

logging.basicConfig(format="%(levelname)s - %(asctime)s - %(message)s", datefmt='%H:%M:%S', level=logging.DEBUG)

# Blocking socket
def blocking(host, ip):
    logging.info("Blocking socket")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.info("Blocking socket connecting...")
    sock.connect((host, ip))
    logging.info("Blocking socket connected")
    logging.info("Blocking socket sending...")
    sock.send(b'Hello, block socket\r\n')
    logging.info("Blocking socket waiting...")
    data = sock.recv(1024)
    logging.info(f"Blocking socket data = {len(data)}")
    logging.info("Blocking socket closing...")
    sock.close()

# Non-blocking socket
def non_blocking(host, port):
    logging.info("Non blocking socket")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.info("Non blocking socket connecting...")
    ret = sock.connect_ex((host, port))
    if ret != 0:
        logging.info("Non blocking socket - fiailed to connect")
        return
    logging.info("Non blocking socket - connected!")
    sock.setblocking(False)
    inputs = [sock]
    outputs = [sock]
    while inputs:
        logging.info("Non blocking socket - waiting...")
        readable, writable, errors = select.select(inputs, outputs, inputs, 0.5)
        for sock in writable:
            logging.info("Non blocking socket - sending...")
            data = sock.send(b'Hello, World!\r\n')
            logging.info(f"Non blocking socket - sent {data}")
            outputs.remove(sock)
        for sock in readable:
            logging.info("Non blocking socket - reading...")
            data = sock.recv(1024)
            logging.info(f"Non blocking socket - data {len(data)}")
            logging.info("Non blocking socket - closing...")
            sock.close()
            inputs.remove(sock)
            break
        for sock in errors:
            logging.info("Non blocking socket - error")
            inputs.remove(sock)
            outputs.remove(sock)
            break

def main():
    # blocking("youtube.com", 80)
    non_blocking("youtube.com", 80)

if __name__ == "__main__":
    main()
