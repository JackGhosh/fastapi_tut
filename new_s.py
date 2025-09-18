from fastapi import FastAPI

app=FastAPI()

@app.get("/ping")
async def root():
    return {"message":"Hiii guys you reach me "}