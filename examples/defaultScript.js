/*
The script interpreter is Javascript, three parameters are passed into the script:

Message = The message sent to the App.
lat = The current latitude of the device.
lng = the current longitude of the device.
guid = the guid of the goTenna which generated the message.

At the end of the script you must return something - if nothing is returned the message will not respond back to the other goTenna.

The following functions are available to the script:

print(string) - Adds a message to the activity log.
getData(url) - returns data from the url as a string.
postData(url,parameters) - returns data from the url as a string with the parameter string being passed as post data. The parameters must be url encoded.
peertalk(message) - sends the message over the peertalk interface
network_status() - Returns a string describing the current network type (e.g. Wifi).
host_reachable() - Checks if the network can reach a known host (www.apple.com).
cell_status() - Returns a string to indicate if cellular data is available.
gotenna_battery() - Returns the goTenna battery level.
iphone_battery() - Returns the iPhone battery level.
select(sqlstatement) - Executes a SQL Statement against the logging tables ("gtmessages" and "gtdevices").
send(targetguid,message) - Sends the message to the target device.
shout(message) - sends a shout message.

*/

print('Default message: '+message + ' Lat:'+lat+' Lng:'+lng);

if (message == "timer_event") {
    send("1234567890","shout message timer");
    return '';
} else if (message == "startup_event") {
    shout("Startup");
    return "";
} else {
    return message;
}


