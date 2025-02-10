import random

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
print("---------------labl1-----------------")



value1 = input("Enter the server name: ")
try:
    if not value1.isalnum():
        print("Invalid input. Only alphanumeric characters are allowed.")
except Exception as e:
    print(f"An error occurred: {e}") 
if value1 in server_names:
    print("The server exists.")
else:
    raise ValueError(f"{value1} is not a recognized server.")
    
print("---------------labl2-----------------")
if value1 in server_status:
    print(f"The status of {value1} is {server_status[value1]}")    
    print("would you like to change the status?")
    change = input("Enter yes or no: ")
    if change == "yes":
        server_status[value1] = not server_status[value1]
        print(f"The status of {value1} has been changed to {server_status[value1]}")
        
        
        

