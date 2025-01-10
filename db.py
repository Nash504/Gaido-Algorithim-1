import os
from supabase import create_client, Client
from dotenv import load_dotenv
from ai import gen

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

result = gen()

def get_events():
    response = supabase.table('events').select('*').execute()
    return response.data

def insert_event(event):
    response = supabase.table('events').insert(event).execute()
    if response.error:
        return response.error
    else:
        return response.data
    
insert_event(result)