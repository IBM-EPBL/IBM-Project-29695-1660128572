import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "0kzyfe",
        "typeId": "Ultrasonic_sensor",
        "deviceId":"987654321"
    },
    "auth": {
        "token": "f)6Dj)7L9+v&IG2!AF"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    level=random.randint(0,400)
    
    if (level<=100):   
     myData={'Level':level,"Alert":"High Alert!!!,Trash bin is about to be full"}
     client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
     print("Published data Successfully: %s", myData)
    
    if ((level>150) and (level<250)):
     myData={'Level':level,"Alert":"Warning!!,Trash is about to cross 50% of bin level"}
     client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
     print("Published data Successfully: %s", myData)
     
    if ((level>250) and (level<400)):
     myData={'Level':level,"Alert":"Bin is available"}
     client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
     print("Published data Successfully: %s", myData)
    
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
