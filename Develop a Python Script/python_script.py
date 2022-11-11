import time 
import json
import wiotp.sdk.device 

myConfig = { 
"identity": { 
"orgId": "0kzyfe", 
"typeId": "python_script", 
"deviceId": "1234" 
},
"auth": { 
"token": "Yf6(6vzd0MNRXBk9?v" 
} 
} 

client = wiotp.sdk.device.DeviceClient (config=myConfig, logHandlers=None) 
client.connect()


def fun():
	name="Demo"
	latitude=11.016844
	longitude=76.955833
	myData={'name':name,'lat':latitude,'lon':longitude}
	client.publishEvent(eventId="status",msgFormat="json",data=myData,qos=0,onPublish=None)  
	print("Published  data  Successfully ti IBM IoT platform:", myData) 
	time.sleep(5) 

client.commandCallback = fun

client.disconnect()