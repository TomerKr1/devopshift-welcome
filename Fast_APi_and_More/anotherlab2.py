from dataclasses import dataclass
from urllib import request
from fastapi import FastAPI
import httpx
from models import ServerStatusResponse, Server, add_new_server
from models import read_server_list
app = FastAPI()
import requests  # Import the correct module

import requests
import time

url = "https://api.example.com/system/metrics?metrics=cpu,memory"
url1='https://jsonplaceholder.typicode.com/users'
headers = {"Authorization": "Bearer YOUR_API_KEY"}



retries = 3

for attempt in range(1, retries + 1):
    try:
        print(f"Fetching system metrics... (Attempt {attempt})")
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()  # Raise an error for non-200 responses
        print("System Metrics:", response.json())
        break
    except requests.exceptions.HTTPError as errh:
        if response.status_code == 401:
            print("Invalid API Key.")
            break
        elif response.status_code == 500:
            print("Server is currently down.")
        else:
            print(f"HTTP error occurred: {errh}")
    except requests.exceptions.ConnectionError:
       
        print("Error: Unable to connect to the API.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"General error occurred: {e}")
    
    if attempt < retries:
        print(f"Retrying in 2 seconds...")
        time.sleep(2)
    else:
        print("All retry attempts failed.")



@dataclass
class UserResponse:
    id:int
    username: str
    email: str
    address: dict[str] 


@app.get("/")
def get_my_users(user_id:int):
   
    params = {"id": user_id}
    try:
        response = httpx.get('https://jsonplaceholder.typicode.com/users', params=params, timeout=5.0)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except :
        print("Error")
        return {"error": "Server not found"}
        
      
        
    if response.status_code == 200:
        data = response.json()
        if data:  # Ensure response list is not empty
            user = data[0]
            user_data = UserResponse(
                id=user["id"],
                username=user["username"],
                email=user["email"],
                address=user["address"]
            )
            return user_data  # FastAPI automatically converts it to JSON
    elif response.status_code==404:
         return {"error": "User not found"} 
    elif response.status_code==500:
        return {"error": "Server not found"}
    
    
