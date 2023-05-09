from fastapi import FastAPI, status, HTTPException
import uvicorn, pickle, sys, json
from pydantic import BaseModel

'''
To publish. you should type following command:
    pyinstaller --onefile Server.py
'''

app = FastAPI()

class User(BaseModel):
    id: str
    passwd: str

users = dict()

@app.post("/login")
async def login(user: User):
    user = dict(user)
    if (user["id"] in users and user["passwd"] == users[user["id"]]):
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found.")

@app.post("/register")
async def login(user: User):
    user = dict(user)
    if user["id"] in users:
        raise HTTPException(status_code=409, detail="User already registered.")
    else:
        users[user["id"]] = user["passwd"]
        with open("members.dat", 'wb') as f:
            pickle.dump(users, f)
        print("registered: " + json.dumps(user))
    return user

if __name__ == "__main__":
    try:
        with open("members.dat", 'rb') as f:
            users = pickle.load(f)
    except EOFError:
        pass
    except FileNotFoundError:
        pass
    else:
        print("undefined error")
    uvicorn.run(app, host="0.0.0.0", port=6974)