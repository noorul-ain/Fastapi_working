"""FASTAPI GET,PUT, POST & DELETE Route Methods """

from fastapi import FastAPI
import uvicorn

app = FastAPI()
name = []
data = []

# ------Get method----------
@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/home/{user_name}")
def get_data(user_name):
    return {"message": f"Hello {user_name}"}

# -------PUT Methods---------------

@app.put("/put_data/{username}")
def put_data(username):
    name.append(username)
    return {"Your name is":username}

# -------POST Methods---------------

@app.post("/post_data/{roll}")
def post_data(roll):
    data.append(roll)
    return {"Your Roll _no  is":roll}
    
# -------POST Methods---------------

@app.delete("/delete_data/{username}")
def delete_data(username):
    name.remove(username)
    return {"Your name is   is":username}

if __name__ == "__main__":
    uvicorn.run(app)