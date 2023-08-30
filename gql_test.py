import requests

def send_graphql_request(endpoint, query, headers=None):
    """
    Sends a GraphQL request.

    :param endpoint: The URL for the GraphQL endpoint.
    :param query: The GraphQL query string.
    :param headers: Any additional headers for the request (e.g. authentication).
    :return: The response data.
    """
    
    response = requests.post(endpoint, json={'query': query}, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

if __name__ == '__main__':
    # Example Usage
    URL = "http://flaskapp:8000/gql"
    QUERY = """
    {
        first: getUser(id: 1) {
            id
            role {
                id
            }
        }
        second: getUser(id: 2) {
            id
            role {
                id
            }
        }
    }
    """
    
    # Optionally, add headers for authentication or other purposes
    HEADERS = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN"
    }

    result = send_graphql_request(URL, QUERY, HEADERS)
    print(result)
