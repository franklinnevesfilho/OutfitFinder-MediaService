from fastapi import FastAPI

app = FastAPI()

@app.get("/{file_name}")
def read_file(file_name: str):
    return {"file_name": file_name}

@app.post("/{file_name}")
def create_file(file_name: str):
    return {"file_name": file_name}

@app.delete("/{file_name}")
def delete_file(file_name: str):
    return {"file_name": file_name}

@app.put("/{file_name}")
def update_file(file_name: str):
    return {"file_name": file_name}

