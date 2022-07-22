import json
from datetime import date
import json
today = date.today()


user = 1

# Data to be written
users  = {
  "users": [
    {
      "userId": "0",
      "username": "Fred",
      "date": str(today)
    },
    {
      "userId": "1",
      "username": "Ben",
      "date": str(today)
    },
    {
      "userId": "2",
      "username": "Sarah",
      "date": str(today)
    }
  ]
}

# Serializing json
json_object = json.dumps(users, indent=4)

# Writing to sample.json
with open("users.json", "w") as outfile:
	outfile.write(json_object)

f = open('users.json')
data = json.load(f)

# name ="Fred"

# for i in range(len(data["users"])):
#     if data["users"][i]["username"] == name:
#             print(data["users"][i])

name = "bob"

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