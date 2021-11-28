import time
from threading import Timer, Thread
import logging
import random


__author__ = "Ejie Emmanuel Ebuka"

# Timers, intoduction to Threads
# Excute code at time intervals
# This is the first step in learning threading

def display(msg):
    print(msg + ' ' + time.strftime('%H:%M:%S'))

# Basic timer
def run_once():
    display("Run once;")
    t = Timer(5, display, ['Timeout'])
    t.start()

run_once()
print("Waiting...")

# Interval timer
# Wrap it in a class, make it run until we stop it
# We can have multiple timers at once

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
        print("Done")

# Making a thread and controlling it
timer = RepeatTimer(1, display, ["Repeating"])
timer.start() # calling run function
time.sleep(10) # suspend execution for any given time
print("Finishing...")
timer.cancel()


# How to move a function to multiple threads
# And wait for all threads to complete

# Function to do the work
def longtask(name):
    max = random.randrange(1, 10)
    logging.info(f"Task: {name} performing {str(max)} times")
    for x in range(max):
        logging.info(f"Task {name}: {x}")
        time.sleep(random.randrange(1, 3))
    logging.info(f"Task: {name} complete")

# Main function
def main():
    logging.basicConfig(format="%(levelname)s - %(asctime)s - %(message)s", datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info("Starting...")
    # longtask("main")
    # Run it on multiple thread
    threads = []
    for x in range(10):
        thread = Thread(target=longtask, args=['thread' + str(x)])
        threads.append(thread)
        thread.start()
    # Wait for all threads to finish
    for t in threads:
        t.join()
    logging.info("Finished all threads")

if __name__ == "__main__":
    main()
