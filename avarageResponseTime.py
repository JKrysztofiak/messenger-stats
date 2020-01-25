import json
import os
import matplotlib.pyplot as plot

#Iterating over all files in a dir
dir = os.fsdecode('user/')

#Loading JSON
with open('user/message_1.json') as file:
    data = json.load(file)

#Participants
user1 = str(data["participants"][0]["name"]).split(" ")[0]
user2 = str(data["participants"][1]["name"]).split(" ")[0]

print(f"Participants: {user1}, {user2}")

#Stats for participants
responsesByUser = {
    user1: 0,
    user2: 0,
}


responseTimeForUser = {
    user1: 0,
    user2: 0
}

avgResponseTime = {
    user1: 0.0,
    user2: 0.0
}

for file in os.listdir(dir):
    with open('user/message_1.json') as file:
        data = json.load(file)

    for msgNumber in range(0,len(data["messages"])-1):
        u1 = str(data["messages"][msgNumber]["sender_name"]).split(" ")[0]
        u2 = str(data["messages"][msgNumber+1]["sender_name"]).split(" ")[0]
        if u1 != u2:
            response = int(data["messages"][msgNumber]["timestamp_ms"])
            message = int(data["messages"][msgNumber+1]["timestamp_ms"])

            responseTime = abs(response-message)

            if responseTime < 10*60*60*1000:
                responsesByUser[u1] += 1
                responseTimeForUser[u1] += responseTime

    avgResponseTime[user1] = responseTimeForUser[user1]/responsesByUser[user1]
    avgResponseTime[user2] = responseTimeForUser[user2]/responsesByUser[user2]

    
             

            
print(f"{user1} avarage response time: {round(avgResponseTime[user1]/(1000*60),2)}min")
print(f"{user2} avarage response time: {round(avgResponseTime[user2]/(1000*60),2)}min")

