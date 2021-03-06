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

#Time diff after which the conversation is considered "new"
hours = 6
timeDiff = hours*60*60*1000 

#Conversation starts counter
number = 0

#Stats for participants
startOfConvoStats = {
    user1: 0,
    user2: 0
}

for file in os.listdir(dir):
    with open('user/message_1.json') as file:
        data = json.load(file)

    for msgNumber in range(0,len(data["messages"])-2):
        if int(data["messages"][msgNumber]["timestamp_ms"])-int(data["messages"][msgNumber+1]["timestamp_ms"]) > timeDiff:
            if int(data["messages"][msgNumber+1]["timestamp_ms"])-int(data["messages"][msgNumber+2]["timestamp_ms"]) < timeDiff:
                message = "not a text"
                if "content" in data["messages"][msgNumber]:
                    message = str(data["messages"][msgNumber]["content"])
        
                number += 1
                startingParticipant = str(data["messages"][msgNumber]["sender_name"]).split(" ")[0]
                startOfConvoStats[startingParticipant] += 1
                # print(f'new convo {number} started by {startingParticipant} [Message: {message}]')
            
        
print(f"Conversations started: {number}")
print(f"{user1}: {startOfConvoStats[user1]}")
print(f"{user2}: {startOfConvoStats[user2]}")


#Data visualisation

labels = [user1, user2]
sizers = [startOfConvoStats[user1],startOfConvoStats[user2]]
colors = ['yellowgreen','lightskyblue']
explode = (0.1, 0)

plot.pie(sizers,explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plot.axis('equal')
plot.show()

