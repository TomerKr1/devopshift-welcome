import logging
import os

'''
the order of the messages
ERROR
WARN
INFO 
DEBUG
'''
loglevel = os.getenv("LOGLEVEL", "INFO")
print("You level is", loglevel)

logging.basicConfig(filename="loggingLab.log",format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("Tomer")
logger.setLevel(logging.DEBUG)

logger.info("This is an info message")




logger.warning("This is a warning message")
logger.error("This is an error message")






# new_logger = logging.getLogger("Tomer2")
# new_logger.setLevel(logging.DEBUG)
# new_logger.info("This is an info message from the new logger")