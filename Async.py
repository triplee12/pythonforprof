import threading
import multiprocessing
import logging
import asyncio
import random

__author__ = "Ejie Emmanuel Ebuka"

# Async code
# Async runs in the same thread
# Async uses co-routins which run on the same thread
# Async goes with "async" and "wait" keywords

logging.basicConfig(format="%(levelname)s - %(asctime)s - %(message)s", datefmt='%H:%M:%S', level=logging.DEBUG)

def display(msg):
    threadname = threading.current_thread().name
    processname = multiprocessing.current_process().name
    logging.info(f'{processname}\{threadname}: {msg}')

async def work(name):
    display(name + " " + ' starting...')
    await asyncio.sleep(random.randint(1, 10))
    display(name + " " + ' finished')

async def run_async(max):
    tasks = []
    for x in range(max):
        name = "Item" + str(x)
        tasks.append(asyncio.ensure_future(work(name)))
    await asyncio.gather(*tasks)

def main():
    display("Main starting...")
    loop = asyncio.get_event_loop()
    # This will make your app runs forever
    # loop.run_forever()
    
    # Run until task is completed
    loop.run_until_complete(run_async(100))
    
    # close the loop
    loop.close()
    display("Main finished")

if __name__ == "__main__":
    main()
