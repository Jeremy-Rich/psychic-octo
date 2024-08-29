import requests
import json

# Set your KeyMate endpoint and API key if needed
ENDPOINT = "https://app.keymate.ai/api"
API_KEY = "1299677cb91dae581cdee0b2d02af550242c657c"  # Include your API key

# Function to test endpoint connection
def test_endpoint_connection():
    url = f"{ENDPOINT}/status"
    headers = {
        "Authorization": f"Bearer {API_KEY}"  # Use your API Key here if required
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Endpoint is reachable.")
        return response.status_code, response.json()
    else:
        print("Failed to connect to the endpoint.")
        print("Status Code:", response.status_code)
        print("Response Data:", response.text)
        return response.status_code, None

# Function to query the knowledge base
def query_knowledge_base(query):
    url = f"{ENDPOINT}/query"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"  # Use your API Key here if required
    }
    data = {
        "q": query
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print("Raw Response Text:", response.text)
    return response.json()

# Function to upsert (insert/update) data into the knowledge base
def upsert_to_knowledge_base(data_text):
    url = f"{ENDPOINT}/upsert"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"  # Use your API Key here if required
    }
    data = {
        "q": data_text
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print("Raw Response Text:", response.text)
    return response.json()

# Example usage
if __name__ == "__main__":
    # Test endpoint connection
    print("Testing endpoint connection...")
    status_code, status_response = test_endpoint_connection()
    if status_response:
        print("Status Response:", status_response)

    query = "example query"
    print("Querying knowledge base...")
    query_result = query_knowledge_base(query)
    print("Query Result:", query_result)

    data_text = "example data to be inserted"
    print("Upserting to knowledge base...")
    upsert_result = upsert_to_knowledge_base(data_text)
    print("Upsert Result:", upsert_result)
