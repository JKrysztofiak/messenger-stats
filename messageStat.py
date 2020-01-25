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

#Conversation starts counter
number = 0

#Stats for participants
convoStats = {
    user1: 0,
    user2: 0
}

for file in os.listdir(dir):
    with open('user/message_1.json') as file:
        data = json.load(file)

    for msg in data["messages"]:
        number+=1
        user = str(msg["sender_name"]).split(" ")[0]
        convoStats[user] += 1
        
print(f"Conversations started: {number}")
print(f"{user1}: {convoStats[user1]}")
print(f"{user2}: {convoStats[user2]}")


#Data visualisation

l1 = user1+'\n('+str(convoStats[user1])+')'
l2 = user2+'\n('+str(convoStats[user2])+')'
labels = [l1, l2]
sizers = [convoStats[user1],convoStats[user2]]
colors = ['gold','dodgerblue']
explode = (0.1, 0)

plot.pie(sizers,explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=45, )

plot.axis('equal')
plot.show()

