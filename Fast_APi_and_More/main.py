from fastapi import FastAPI
from models import ServerStatusResponse, Server, add_new_server
from models import read_server_list
app = FastAPI()

servers=read_server_list()

def search_for_server(name):
    for server in servers:
        if(name==server.name):
            return server
    return None



@app.get("/server")
def get_server(server_name1: str) -> ServerStatusResponse:
    myserver=search_for_server(server_name1)
    if myserver != None:
       return ServerStatusResponse(server_name=server_name1, server_status=myserver.online )
    else:
        return ServerStatusResponse(server_name="none", server_status=False)


@app.post("/server")
def create_server(server_name: str) -> ServerStatusResponse:
    new_server = Server(name=server_name, online=True, cpus=10, ram=20)
    add_new_server(new_server)
    return ServerStatusResponse(server_name=server_name, server_status="Created")


@app.get("/MyServers")
def get_all_servers():
        servers = read_server_list()
        return servers
