from fastapi import APIRouter
from server.data import real_priorities

router = APIRouter(prefix ="/priorities", tags =['priorities'])

# GET all
@router.get('/')
async def read_priorities():
    return real_priorities

# GET a specific one 
@router.get('/{priority_id}')
async def read_singular_priority(id: int):
    return real_priorities['id']

# POST a new one 


# Patch a specific one 

# Delete a specific one 