import random
import logging
import time
import threading
from concurrent.futures import ThreadPoolExecutor

__author__ = "Ejie Emmanuel Ebuka"

# Thread pools
# Reusing existing threads, because creating threads are expensive

# Test
def test(item):
    s = random.randrange(1, 10)
    logging.info(f'Thread {item}: id = {threading.get_ident()}')
    logging.info(f'Thread {item}: name = {threading.current_thread().name}')
    logging.info(f'Thread {item}: sleeping for {s}')
    time.sleep(s)
    logging.info(f'Thread {item}: finished')

# main
def main():
    logging.basicConfig(format="%(levelname)s - %(asctime)s - %(message)s", datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info("Starting... Pool App")
    workers = 5
    items = 15
    with ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(test, range(items))
    logging.info("Finished All Threads")

if __name__ == "__main__":
    main()


# Thread locking
# Avoid dread race conditions and deadlocks
# Race condition is the state of excution where multiple threads modified same resource
# Deadlock is the state where multiple threads waiting for the same resource

# Test 2
counter = 0

def test_2(count):
    global counter
    tname = threading.current_thread().name
    logging.info(f'Starting: {tname}')

    for x in range(count):
        logging.info(f'Count: {tname} += {count}')
        # lock interpreter (GIL)
        lock = threading.Lock()
        # lock.acquire()
        # try:
        #     counter += 1
        # finally:
        #     lock.release()
        with lock:
            logging.info(f'Locked: {tname}')
            counter += 1
            time.sleep(2)
    logging.info(f'Completed: {tname}')

def main():
    logging.basicConfig(format="%(levelname)s - %(asctime)s - %(message)s", datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info("Starting... Pool App")
    workers = 3
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for a in range(workers * 3):
            value = random.randrange(1, 10)
            executor.submit(test_2, value)
    logging.info("Finished All Threads")

if __name__ == "__main__":
    main()

