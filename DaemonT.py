import random
import logging
import time
import threading
from threading import Timer, Thread
from concurrent.futures import ThreadPoolExecutor


__author__ = "Ejie Emmanuel Ebuka"

# Daemon Thread
# Quitting a thread when the app exits

# Test
def test():
    tname = threading.current_thread().name
    logging.info(f'Starting... {tname}')
    for x in range(100):
        logging.info(f'Working on... {tname}')
        time.sleep(2)
    logging.info(f'Finished: {tname}')

def stop():
    logging.info('Exiting the application')
    exit(0)

def main():
    logging.basicConfig(format="%(levelname)s - %(asctime)s - %(message)s", datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info("Starting... Daemon App")
    # Stop in 5 seconds
    timer = Timer(5, stop)
    timer.start()
    thread = Thread(target=test, daemon=True)
    thread.start()
    logging.info("Finished All Threads")

if __name__ == "__main__":
    main()

