import random
import logging
import time
import threading
from threading import Timer, Thread
from concurrent.futures import ThreadPoolExecutor
from queue import Queue


__author__ = "Ejie Emmanuel Ebuka"

# Future and Queue
# Getting values from a thread

"""
Queue is like a group of people waiting for ATM service.
Future is used for synchronizing program execution in some concurrent
programming languages.
"""

# Use future to pass messages 
def test_f(name):
    tname = threading.current_thread().name
    logging.info(f'Starting... {tname}')
    time.sleep(random.randrange(1, 10))
    logging.info(f'Finishing... {tname}')
    ret = "Hello " + name + " here is your random number: " + str(random.randrange(1, 20))
    return ret

def pooled():
    workers = 20
    ret = []
    with ThreadPoolExecutor(max_workers=workers) as exec:
        for a in range(workers):
            value = random.randrange(1, 10)
            future = exec.submit(test_f, "Bob" + str(a))
            ret.append(future)
    logging.info(f'Doing great work on the main thread')
    for r in ret:
        logging.info(f'Returned: {r.result()}')

# Use Queue to pass messages backs and forths
def test_q(name, que):
    tname = threading.current_thread().name
    logging.info(f'Starting... {tname}')
    time.sleep(random.randrange(1, 10))
    logging.info(f'Finishing... {tname}')
    ret = "Hello " + name + " here is your random number: " + str(random.randrange(1, 20))
    que.put(ret)

def queued():
    queue = Queue()
    thread = Thread(target=test_q, args=['Chris', queue])
    thread.start()
    logging.info(f'Doing great work on the main thread')
    thread.join()
    ret = queue.get()
    logging.info(f'Returned: {ret}')

def main():
    logging.basicConfig(format="%(levelname)s - %(asctime)s - %(message)s", datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info("Starting... Queue App")
    pooled()
    # queued()


if __name__ == "__main__":
    main()
