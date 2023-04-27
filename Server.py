from fastapi import FastAPI, status, HTTPException
import uvicorn, pickle, mariadb, sys
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: str
    passwd: str

users = []

'''
SERVERADDRESS = ""

try:
    try:
        with open("serverAddress", 'r') as f:
            SERVERADDRESS = f.readline()
    except EOFError:
        pass
    except FileNotFoundError:
        pass
    else:
        print("undefined error")
    conn = mariadb.connect(
        user            =                                                           "client",
        password        = "7E6890CCFA16700AB04A41AAADA4FC6B98CE212D7A5D14F9238D2F5F98D1590C",
        host            =                                                      SERVERADDRESS,
        port            =                                                               1397,
        database        =                                                         "projectn"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()

'''

@app.post("/login")
async def login(user: User):
    if (user in users):
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found.")


@app.post("/register")
async def login(user: User):
    if user in users:
        raise HTTPException(status_code=409, detail="User already registered.")
    users.append(user)
    with open("members.dat", 'wb') as f:
        pickle.dump(users, f)
    print("registered: " + user)
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