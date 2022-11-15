import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "0kzyfe",
        "typeId": "BIN_1",
        "deviceId":"BIN1"
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
    myData={  'name': 'Bin_1', 'lat': 13.092677, 'lon': 80.188314 ,'Level':level, 'Weight':weight  }
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0,onPublish=None)
    print ("Published data Successfully: %s", myData) 
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
