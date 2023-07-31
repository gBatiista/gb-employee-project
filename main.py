from fastapi import FastAPI

from routes import main_routes

app = FastAPI()

app.include_router(main_routes.router, prefix="")


@app.get("/")
def root():
    return {"status": "online"}
