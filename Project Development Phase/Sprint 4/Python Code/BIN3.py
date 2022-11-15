import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "0kzyfe",
        "typeId": "BIN_3",
        "deviceId":"BIN3"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    level=random.randint(0,10) 
    weight=random.randint(0,10)
    myData={  'name': 'Bin_3', 'lat': 15.092677, 'lon': 79.188314 ,'Level':level, 'Weight':weight  }
    if weight == 10:
     print ('ALERT !! Weight is HIGH') 
    if level == 10:
     print ('ALERT !! Level is HIGH') 
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0,onPublish=None)
    print ("Published data Successfully: %s", myData) 
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
