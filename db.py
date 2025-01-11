import os
import json
from dotenv import load_dotenv
from supabase import Client, create_client
from ai import gen

load_dotenv()

# Supabase initialization
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Generate content and insert into Supabase
def get_events():
    response = supabase.table('events').select('*').execute()
    return response.data

def insert_event(event):
    response = supabase.table('events').insert(event).execute()
    if response:
        return response.data
    else:
        print("Error inserting event.")
        
if __name__ == "__main__":

    result = gen()
    if result:
        response = insert_event(result)
        print(response)
    else:
        print("No valid event data to insert.")
