from fastapi import FastAPI, Path
from datetime import date
import json


today = date.today()
# create api object
app = FastAPI()

# GET - ENDPOINT RETURNS INFO
# POST - ENDPOINT IS GETTING/CREATING NEW DATA
# PUT - ENDPOINT UPDATE DATA
# DELETE - ENDPOINT DELETE DATA


# @ is for 
@app.get('/')
def home():
    return {"Data":"test"}

# new endpoint defined by about
@app.get("/get-user/{user_id}")
def get_item(user_id: int = Path(None, description="Pass user ID.")): #defining type needs to be int

    # load here because it will be updated with POST
    f = open('users.json')
    data = json.load(f)

    return data["users"][user_id]

# Query parameter = .../home?redirect=/time&msg... ? signifies this
# use this to search for existing username and write new one?

@app.get("/get-by-name")
def get_item(name: str): #defining type needs to be int

    # load here because it will be updated with POST
    f = open('users.json')
    data = json.load(f)

    for i in range(len(data["users"])):
        if data["users"][i]["username"] == name:
            return data["users"][i]


    add_user = {
                "userId": len(data["users"]),
                "username": name,
                "date": str(today)
                }


    data["users"].append(add_user)


    # Serializing json
    json_object = json.dumps(data, indent=4)

    # Writing to sample.json
    with open("users.json", "w") as outfile:
        outfile.write(json_object)
        
    return {"New user written" : "Done"}
