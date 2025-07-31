from fastapi import FastAPI
from routes import spending, user

app = FastAPI()


app.include_router(spending.router)
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "welcome to money buddy"}