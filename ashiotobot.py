import sys
from twython import Twython
from boto.dynamodb2.table import *
from datetime import datetime

#DynamoDB Initialization
ashiotoTable = Table('ashioto2')

#Temp File
lastGate_file = open('/home/geek/ashiotobot/last.csv', 'a+')

# your twitter consumer and access information goes here
apiKey = 'qQgfiVwqGeslzSHBijVw0DTSo'
apiSecret = 'vfsRpwvex9E3EUJgVNZLUKZegxnAzno8Ge4Q1tU90B0N0Is87R'
accessToken = '3593473819-NXVpJn93FAwZxW9gx0TBiojJsuviulcOd7CIjlw'
accessTokenSecret = 'n2tkNjCDvVLOWVu6uXhcWIZXQBHGV6gb9diQxobTOfJtH'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

gate = 1

gate1Id = "Rokdoba"
gate2Id = "Amardham"
gate3Id = "Ramkund"
gate4Id = "Laxminarayan"
gate5Id = "Gharpure"
gateList = [gate1Id,gate2Id,gate3Id,gate4Id,gate5Id]
countList = []
time = ""

while gate <= 5:
    currentGate = gateList[gate-1]
    gateQuery = ashiotoTable.query_2(limit=1, gateID__eq=gate,reverse=True)
    toTweet = ""
    for result in gateQuery:
        count = result['outcount']
        print("Gate: "+str(gate)+" "+str(count))
        countList.append(int(count))
        #Parsing all the values
        timestampUnix = int(result['timestamp'])-19800
        #Converting unix timestamp to human datetime
        timestampHuman = str(datetime.fromtimestamp(timestampUnix).strftime('%I:%M%p'))
        print(timestampHuman)
        if gate == 1:
            time = timestampHuman
        toTweet = "Count at " + str(currentGate) + " At " + timestampHuman + " : " + str(count) + " ! http://ashioto.in #Ashioto #KumbhMela #Nashik #CountPeople #IOT"
        api.update_status(status=toTweet)
    gate+=1
    
total = 0
for item in countList:
    total += int(item)
tweet = "The Total Count At " + time + " Is: " + str(total) + " ! http://ashioto.in #Ashioto #KumbhMela #IOT #KumbhMela #Nashik"
api.update_status(status=tweet)