import json
from urllib.parse import urlparse

class SimulatedRequestException(Exception):
    pass

class SimulatedTimeout(SimulatedRequestException):
    pass

class SimulatedHTTPError(SimulatedRequestException):
    def __init__(self, status_code):
        self.status_code = status_code

def simulated_api_call(url, timeout=5):
    parsed_url = urlparse(url)
    path = parsed_url.path.strip('/')
    
    if 'jsonplaceholder.typicode.com' in parsed_url.netloc:
        if path == 'todos/1':
            return {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
        elif path == 'nonexistent':
            raise SimulatedHTTPError(404)
    elif 'thisisnotarealwebsite.com' in parsed_url.netloc:
        raise SimulatedRequestException("DNS lookup failed")
    elif 'api.github.com' in parsed_url.netloc:
        if 'repos/pandas-dev/pandas/issues' in path:
            raise SimulatedHTTPError(403)  
    
    raise SimulatedTimeout()

def fetch_data_from_api(url, timeout=5):
    try:
        response = simulated_api_call(url, timeout=timeout)
        return response
    except SimulatedTimeout:
        print(f"The request to {url} timed out after {timeout} seconds.")
        return None
    except SimulatedHTTPError as http_err:
        print(f"HTTP error occurred: {http_err.status_code}")
        return None
    except SimulatedRequestException as req_err:
        print(f"An error occurred while making the request: {req_err}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


urls = [
    "https://jsonplaceholder.typicode.com/todos/1",  
    "https://jsonplaceholder.typicode.com/nonexistent",  
    "https://thisisnotarealwebsite.com",  
    "https://api.github.com/repos/pandas-dev/pandas/issues",  
    "https://example.com/api/data"  
]

for url in urls:
    print(f"\nTrying to fetch data from: {url}")
    result = fetch_data_from_api(url)
    if result:
        print("Data fetched successfully:")
        print(json.dumps(result, indent=2))
    else:
        print("Failed to fetch data.")