import logging


__author__ = "Ejie Emmanuel Ebuka"

# Logging basics

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""
# Basic logging
# They do not all get displayed by default

def test():
    level = logging.getLevelName(logging.getLogger().getEffectiveLevel())
    print("-" * 34)
    print(f"Log level: {level}")
    logging.debug("Debug message here")
    logging.info("Info message here")
    logging.warning("Warning message here")
    logging.error("Error message here")
    logging.critical("Critical message here")
    print("-" * 34)

test()

# Getting and setting logging levels
# Allows for filtering

# First get root logger
rootlog = logging.getLogger()
print(f"Level: {logging.getLevelName(rootlog.getEffectiveLevel())}")

# Set level to debug
rootlog.setLevel(logging.DEBUG)
test()

# Log to file
# basicConfig only works if the logger has not been configured before
# logging.basicConfig(filename="mylog/mylog.txt", filemode='w', format='%(levelname)s:%(message)s', level=logging.DEBUG)
# logging.debug("Hello")

handler = logging.FileHandler("mylog/mylog.log")
formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
handler.setFormatter(formatter)
rootlog.addHandler(handler)
rootlog.debug("Test")
test()
