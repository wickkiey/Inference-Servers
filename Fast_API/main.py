from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(file: str = "File Name"):
    print("File Name",file)
    return {"message": "Hello World"}