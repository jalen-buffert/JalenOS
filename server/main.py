from fastapi import FastAPI
from server.routes import priorities
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#Wont use these now going to allow all for now => '*'
origins = ['http://localhost:4200']
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
app.include_router(priorities.router)

@app.get('/')
async def root():
    return {'Message': "Hello Application"}

