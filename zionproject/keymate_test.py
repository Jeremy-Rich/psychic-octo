
import keymateapi
from keymateapi.models import operations, errors

API_KEY = "1299677cb91dae581cdee0b2d02af550242c657c"

def query_knowledge_base(query):
    s = keymateapi.Keymateapi(
        bearer_auth=API_KEY
    )
    try:
        response = s.query(q=query)
        return response.to_dict() if response else None
    except errors.SDKError as e:
        print(f"An error occurred: {e}")
        return None

def upsert_knowledge_base(data):
    s = keymateapi.Keymateapi(
        bearer_auth=API_KEY
    )
    try:
        response = s.upsert(q=data)
        return response.to_dict() if response else None
    except errors.SDKError as e:
        print(f"An error occurred: {e}")
        return None

# Test the functions
if __name__ == "__main__":
    test_query = "Test query for Keymate"
    test_data = "Test data for Keymate"
    
    print("Querying knowledge base...")
    query_result = query_knowledge_base(test_query)
    print(f"Query Result: {query_result}")

    print("Upserting to knowledge base...")
    upsert_result = upsert_knowledge_base(test_data)
    print(f"Upsert Result: {upsert_result}")
