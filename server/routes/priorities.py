from fastapi import APIRouter, HTTPException 
from server.data import real_priorities
from server.models.priority import Priority,PriorityCreate
import uuid

router = APIRouter(prefix ="/priorities", tags =['priorities'])

# Read - GET all
@router.get('/', response_model = list[Priority])
async def read_priorities():
    return {"Priorities": real_priorities}

# Read - GET a specific prioriy by ID
@router.get('/{priority_id}', response_model=Priority, status_code = 200)
async def read_singular_priority(priority_id: str | int):
    for priority in real_priorities:
        if priority_id == str(priority.priority_id):
            return {"Priority":priority}
    raise HTTPException(status_code=404, detail = 'ID not found')

# Create - POST a new one
@router.post('/', response_model=Priority, status_code=201)
async def create_new_priority(priority: PriorityCreate):
    id = str(uuid.uuid4())
    new_priority = Priority(priority_id = id, action = 'Pending', **priority.model_dump())
    real_priorities.append(new_priority)
    return {"Message":"Priority Created", "Priority": new_priority}

# Update - PUT to update a priority 
@router.put('/{priority_id}')
async def update_priority(priority_id: str, priority: Priority):
    for i, r_priority in enumerate(real_priorities):
        if priority_id == str(r_priority.priority_id):
            real_priorities[i] = priority
            return {"Message": "Priority Updated", "Updates": priority}
    raise HTTPException(status_code=404, detail = 'Priority ID not found')
    
# Delete - Delete a priority
@router.delete('/{priority_id}')
async def delete_priority(priority_id: str): 
    for i, r_priority in enumerate(real_priorities):
        if priority_id == str(r_priority.priority_id):
            delete_p = real_priorities.pop(i)
            return {"Messages": "Deleted Priority", "Deleted": delete_p}
    raise HTTPException(status_code=404, detail = 'Priority ID not found')


# Patch a specific one 

# Delete a specific one 