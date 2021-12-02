import logging
import multiprocessing
from multiprocessing.context import Process
from multiprocessing import process
import time
import random


__author__ = "Ejie Emmanuel Ebuka"


# Multiprocessing
# Multiple processes running the same script
# This is different from threading
# Each process has its own memory space, and its own threads

# configure logging
logging.basicConfig(format="%(levelname)s - %(asctime)s - %(message)s", datefmt='%H:%M:%S', level=logging.DEBUG)

# Define a process
def run(num):
    name = process.current_process().name
    logging.info(f'Running {name} as {__name__}')
    time.sleep(num * 2)
    logging.info(f'Finished {name}')

# Start a process
def main():
    logging.info("Starting... Multiprocess App")
    name = process.current_process().name
    logging.info(f'Running {name} as {__name__}')
    processes = []
    for x in range(5):
        p = multiprocessing.Process(target=run, args=[x], daemon=True)
        processes.append(p)
        p.start()
    # Wait for the processes
    for p in processes:
        p.join()
    logging.info(f'Finished {name}')

if __name__ == "__main__":
    main()

# Starting and stopping multiprocess
# The full life cycle
print()
print('-' * 34)

def work(msg, max):
    name = multiprocessing.current_process().name
    logging.info(f'{name} started!')
    for x in range(max):
        logging.info(f'{name} - {msg}')
        time.sleep(2)


# Main process
def main():
    logging.info('Starting...')
    max = 2
    worker = Process(target=work, args=['working', max], daemon=True, name="worker")
    worker.start()
    time.sleep(5)
    # if process is running, stop it
    if worker.is_alive:
        worker.terminate()
    worker.join()
    logging.info(f'Finished: {worker.exitcode}')

if __name__ == "__main__":
    main()
print()
print('-' * 34)


# Multiprocess pool
# Pools of process and their results

def work_pool(item, count):
    name = multiprocessing.current_process().name
    logging.info(f'{name} started: {item}')
    for x in range(count):
        logging.info(f'{name}: {item} = {x}')
        time.sleep(4)
    logging.info(f'{name} finished!')
    return item + ' has finished'

# callback
def call_back(result):
    logging.info(f'Result: {result}')

def main():
    logging.info(f'Starting...')
    max = 10
    pool = multiprocessing.Pool(max)
    results = []
    for x in range(max):
        item = 'Item' + str(x)
        count = random.randrange(1, 10)
        r = pool.apply_async(work_pool,[item, count], callback=call_back)
        results.append(r)
    # Wait for the process
    for result in results:
        result.wait()
    
    # close pool
    pool.close()
    pool.join()
    logging.info('Finished')

if __name__ == '__main__':
    main()
