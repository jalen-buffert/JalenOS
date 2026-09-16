from fastapi import APIRouter, HTTPException 
from server.data import real_priorities
from server.schemas.priority import Priority,PriorityCreate,PriorityUpdate
#from fastapi.encoders import jsonable_encoder
import uuid

router = APIRouter(prefix ="/priorities", tags =['priorities'])

# Read - GET all
@router.get('/', response_model = list[Priority])
async def read_priorities():
    if real_priorities is None:
        return []
    else:
        return real_priorities

# Read - GET a specific prioriy by ID
@router.get('/{priority_id}', response_model=Priority)
async def read_singular_priority(priority_id: str):
    for priority in real_priorities:
        if priority_id == priority.priority_id:
            return priority
    raise HTTPException(status_code=404, detail = 'ID not found')           

# Create - POST a new one
@router.post('/', response_model=Priority, status_code=201)
async def create_new_priority(priority: PriorityCreate):
    unique_id = str(uuid.uuid4())
    new_priority = Priority(priority_id = unique_id, action = 'Pending', **priority.model_dump())
    real_priorities.append(new_priority)
    return new_priority

# Update - PUT to update a priority 
@router.patch('/{priority_id}', response_model=Priority, status_code=200)
async def update_priority(priority_id: str, priority:PriorityUpdate):
    for i, r_priority in enumerate(real_priorities):
        if priority_id == r_priority.priority_id:
            updated_data = priority.model_dump(exclude_unset=True)
            updated_priority = r_priority.model_copy(update=updated_data)
            real_priorities[i] = updated_priority
            return updated_priority
    raise HTTPException(status_code=404, detail = 'Priority not found')
    
# Delete - Delete a priority
@router.delete('/{priority_id}', status_code=204)
async def delete_priority(priority_id: str):
    l1 = len(real_priorities)
    for i, r_priority in enumerate(real_priorities):
        if priority_id == r_priority.priority_id:
            real_priorities.pop(i)
    l2 = len(real_priorities)       
    if l1 == l2:
        raise HTTPException(status_code=404, detail = 'Priority not found')


# Patch a specific one 

# Delete a specific one 