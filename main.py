from fastapi import FastAPI
from router import authentication, user
from fastapi.middleware.cors import CORSMiddleware
from repository import models
from repository.database import engine
from starlette.middleware.sessions import SessionMiddleware

# Configure CORS
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
origins = ["*"]
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Add the session middleware to the app
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)


models.Base.metadata.create_all(engine)

app.include_router(user.router)
app.include_router(authentication.router)
  

