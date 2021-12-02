from threading import Timer, Thread
from queue import Queue
import random
import logging
import time
import threading
import multiprocessing


__author__ = "Ejie Emmanuel Ebuka"


# Producer and Consumer

logging.basicConfig(format="%(levelname)s - %(asctime)s - %(message)s", datefmt='%H:%M:%S', level=logging.DEBUG)

def display(msg):
    threadname = threading.current_thread().name
    processname = multiprocessing.current_process().name
    logging.info(f'{processname} - {threadname} : {msg}')

# Producer
def producer(queue, finished, max):
    finished.put(False)
    for x in range(max):
        value = random.randint(1, 150)
        queue.put(value)
        display(f'Producing... {x} : {value}')
    finished.put(True)
    display("Finished producing")

# Consumer
def consumer(work, finished):
    counter = 0
    while True:
        if not work.empty():
            value = work.get()
            display(f'Consuming... {counter} : {value}')
            counter += 1
        else:
            que = finished.get()
            if que == True:
                break
        display("Finished consuming")

# Main
def main():
    max = 100
    work = Queue()
    finished = Queue()
    produce = Thread(target=producer, args=[work, finished, max], daemon=True)
    consume = Thread(target=consumer, args=[work, finished], daemon=True)
    produce.start()
    consume.start()
    produce.join()
    display("Producer has finished")
    time.sleep(2)
    consume.join()
    display("Consumer has finished")
    display("Finished!")

if __name__ == "__main__":
    main()
