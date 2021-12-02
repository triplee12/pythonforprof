import threading
import multiprocessing
import logging
import time
from multiprocessing import process
from multiprocessing.context import Process
from multiprocessing.connection import Listener, Client


__author__ = "Ejie Emmanuel Ebuka"


# Communicating with processes
# Real time processing, even on others machine

logging.basicConfig(format="%(levelname)s - %(asctime)s - %(message)s", datefmt='%H:%M:%S', level=logging.DEBUG)

# Worker
def producer(server="localhost", port=8000, password="1234pass"):
    name = process.current_process().name
    logging.info(f'{name} started')
    # Listening to connections
    address = (server, port)
    listener = Listener(address, authkey=password)
    connect = listener.accept()
    logging.info(f'{name} : connect from {listener.last_accepted}')
    # Loop connected process
    while True:
        message = connect.recv()
        logging.info(f'{name}, data : {message}')
        if message == 'exit':
            connect.close()
            break
    listener.close()
    logging.info(f'{name} finished')

def main():
    name = process.current_process().name
    logging.info(f'{name} started')
    # Setup process
    address = 'localhost'
    port =  8080
    password = b'1234pass'
    p = Process(target=producer, args=[address, port, password], daemon=True, name="blockdev")
    p.start()
    logging.info(f'{name} waiting for work')
    time.sleep(2)
    destination = (address, port)
    connect = Client(destination, authkey=password)
    # Commands
    while True:
        command = input('\r\nEnter a command or Type exit: \r\n').strip()
        logging.info(f'{name} command: {command}')
        connect.send(command)
        if command == 'exit':
            break
    if p.is_alive:
        logging.info(f"{name} closing worker")
        connect.close()
        time.sleep(2)
        p.terminate()
    p.join()
    logging.info(f'{name} finished')

if __name__ == "__main__":
    main()
