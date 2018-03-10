# Introduction

Mesh Developers Toolkit is an iOS App built on goTenna, this repository provides sample code for the App which is now available from the iTunes App Store.

Mesh Toolkit has been built using the goTenna SDK.

The Mesh Toolkit allows incoming messages to be parsed with an inbuilt JavaScript interpreter and the results sent back to the goTenna which generated the message.

Examples of how this can be used is to get weather data from a API or forward messages to a notification service, for example Pushover.

Alternatively, incoming messages can be forwarded to an external web service or URL schema, for example allowing messages to be parsed using Pythonista.

Mesh Toolkit also includes an inbuilt webserver which allows an external device to send messages via a connected goTenna, for example to send a broadcast from a Lightning Detector running on a Raspberry Pi.

Mesh Toolkit also implements a URL schema which allows other Apps on the iOS device to send messages.

For example, a short cut can be implement using a home screen widget and the Workflow App.

Note: To provide web services this App runs in the foreground and does not idle which will reduce battery life therefore we recommend that it is run using external power.

Version 1.5 adds a number of new features:

The script can now scheduled to run approximately every minute.

A preference has been added to enable this.

Also when the setting is enabled the script is run after Mesh Toolkit has connected to the goTenna.

To enable you to identify what event has called the script - the message is set to “startup_event” or “timer_event”.

This release now stores messages and devices in a sqlite3 database which can be accessed as JSON from your script or a web request (“/script?sql=“).

For example if you wished to get all devices which have not connected to Mesh Toolkit in the last five minutes the sql would be:

` select * from gtdevices where timestamp < datetime(current_timestamp,'-5 minutes'); `

A setting has been added to disable this logging (messages and devices are stored for 48 hours).


# Usage notes

NOTE: This application is designed to work with goTenna off-grid messaging devices (https://gotenna.com).

It is built using the goTenna SDK.

The script interpreter is Javascript (using JavaScriptCore), three parameters are passed into the script:

` Message ` = The message sent to the App.
` lat ` = The current latitude of the device.
` lng ` = the current longitude of the device.

Release 1.3:

`  guid ` = the guid of the goTenna which generated the message.


At the end of the script you must return something - if nothing is returned the message will not respond back to the other goTenna.

The following functions are available to the script through the script context:

` print(string) `- Adds a message to the activity log.

` getData(url) `- returns data from the url as a string.

` postData(url,parameters) ` - returns data from the url as a string with the parameter string being passed as post data - the parameters must be url encoded.

Release 1.3 added the following functions:

` network_status() `- Returns a string describing the current network type (e.g. Wifi).

` host_reachable() `- Checks if the network can reach a known host (www.apple.com).

` cell_status() `- Returns a string to indicate if cellular data is available.

` gotenna_battery() `- Returns the goTenna battery level.

` iphone_battery() `- Returns the iPhone battery level.

Release 1.5 added the following functions:

` select(sqlstatement) ` - Executes a SQL Statement against the logging tables ( ("gtmessages" and "gtdevices").

 ` send(targetguid,message)  ` - Sends the message to the target device.

 ` shout(message) ` - sends a shout message.

The default script is:

```
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
```
If the app is set up to redirect messages to an external webserver the parameters are appended to the URL in the format ` ?message=MESSAGE&lat=LATITUDE&lng=LONGITUDE?guid=GUID`

The url schema is “mtk” and requests can be made similar to ` mtk://shout?message=Hello ` or  ` mtk://message?message=MESSAGE?guid=GUID `where GUID is the guid of the device to send to.

These can be tested using the Workflow app and the open URLs component.

External calls to the HTTP server are:

``` curl ‘http://192.168.1.116:8080/message?message=hello%20from%20a%20goTenna&guid=GUID' ```

Or:

``` curl ‘http://192.168.1.116:8080/shout?message=shout%20from%20a%20goTenna' ```

Or:

``` curl ‘http://192.168.1.116:8080/script?message=shout%20from%20a%20goTenna' ```


# Pairing

When the Mesh Toolkit App is first launch it will prompt for the GUID to be set, we recommend that this is set to the same value as in the goTenna App.

Once this is set when you change to the Messages tab, the App will automatically pair with the goTenna in the same way as the goTenna App.

Once the GUID is set the App will automatically pair with the goTenna when it is launched.

# Example code

Added example Javascript script to get weather data from api.openweathermap.org.

2/March/2018 Added example based on the excelent article [Raspberry Pi lightning strikes](https://hexaly.se/2017/06/27/lightning-strikes-detection-station-that-tweets-storm-alerts/) using the [code from here](https://github.com/Hexalyse/LightningTweeter) and [here](https://github.com/pcfens/RaspberryPi-AS3935/).

10/March/2018 For clarity (and if you need to restore it) the default script created when the App is installed has been added to the examples.


