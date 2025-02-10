import logging
import os
import json
import sys
import logging.handlers
import random
import datetime

'''
the order of the messages
ERROR
WARN
INFO 
DEBUG
'''
loglevel = os.getenv("LOGLEVEL", "INFO")
log_format=os.getenv("LOGFORMAT","JSON")
print("Your level of debug is", loglevel)
print("Your log format is", log_format)


logger=logging.getLogger("Tomer")  # create a logger object
logger.setLevel(loglevel)  # set the logger level to debug



logging.StreamHandler(sys.stdout)

class jsonFormatter(logging.Formatter):
    def format(self, record:logging.LogRecord) -> str:
        log = {
            'time': self.formatTime(record, datefmt="%Y-%m-%d %H:%M:%S"),
            "module": record.module,
            "message": record.msg,
           
        }
        return json.dumps(log)
    
class TextFomateer(logging.Formatter):
    def format(self, record:logging.LogRecord) -> str:
        return f"{"TTTT,",record.getMessage()}"
    


sys_handler=logging.StreamHandler(sys.stdout)  # create a handler object


file_handler=logging.FileHandler("log.txt")


if log_format=="JSON":
    print("you choose json")
    formater=jsonFormatter()
    
else:
  formater=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
   # handler.setFormatter(TextFomateer())
   
   
sys_handler.setFormatter(formater)  # set the formatter to the handler
logger.addHandler(sys_handler)  # add the handler to the logger

file_handler.setFormatter(formater)
logger.addHandler(file_handler)






server_names = [
    "light",
    "nginx",
    "docker", 
    "apache",
    "mysql",
    "postgresql",
    "redis",
    "memcached",
    "haproxy",
    "varnish",
    "cassandra",
    "mongodb",
    "rabbitmq",
    "kafka",    
    "zookeeper",
    "elasticsearch",
    "logstash",
    "kibana",
    "prometheus",
    "grafana",
]


server_status = {server: random.choice([True, False]) for server in server_names}
while True:
    value1 = input("Enter the server name: ")
    try:
        if not value1.isalnum():
            logger.error("Invalid input. Only alphanumeric characters are allowed.")
    except Exception as e:
        print(f"An error occurred: {e}") 
    if value1 in server_names:
        logger.info(f"{value1} The server exists.")
    else:
       logger.critical(f"{value1} is not a recognized server.")

    if value1 in server_status:
        logger.info(f"The status of {value1} is {server_status[value1]}")    
       
        print("would you like to change the status?")
        change = input("Enter yes or no: ")
        if change == "yes":
            server_status[value1] = not server_status[value1]
            logger.info(f"The status of {value1} has been changed to {server_status[value1]}")





# new_logger = logging.getLogger("Tomer2")
# new_logger.setLevel(logging.DEBUG)
# new_logger.info("This is an info message from the new logger")