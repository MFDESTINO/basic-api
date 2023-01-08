from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router

#import configs from .env file
config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    verbose = config['VERBOSE']
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    if verbose:
        print("Connected to the Atlas MongoDB database.")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(router, tags=["users"], prefix="/user")