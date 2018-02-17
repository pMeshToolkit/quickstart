# Introduction

Mesh Toolkit is an iOS App built on goTenna, this repository provides sample code for the App which will be available from the iTunes App Store.

Mesh Toolkit has been built using the goTenna SDK.

The Mesh Toolkit allows incoming messages to be parsed with an inbuilt JavaScript interpreter and the results sent back to the goTenna which generated the message.

Examples of how this can be used is to get weather data from a API or forward messages to a notification service, for example Pushover.

Alternatively, incoming messages can be forwarded to an external web service or URL schema, for example allowing messages to be parsed using Pythonista.

Mesh Toolkit also includes an inbuilt webserver which allows an external device to send messages via a connected goTenna, for example to send a broadcast from a Lightning Detector running on a Raspberry Pi.

Mesh Toolkit also implements a URL schema which allows other Apps on the iOS device to send messages.

For example, a short cut can be implement using a home screen widget and the Workflow App.

Note: To provide web services this App runs in the foreground and does not idle which will reduce battery life therefore we recommend that it is run using external power.

# Usage notes

NOTE: This application is designed to work with goTenna off-grid messaging devices (https://gotenna.com).

It is built using the goTenna SDK.

The script interpreter is Javascript (using JavaScriptCore), three parameters are passed into the script:

Message = The message sent to the App.
lat = The current latitude of the device.
lng = the current longitude of the device.

At the end of the script you must return something - if nothing is returned the message will not respond back to the other goTenna.

The following functions are available to the script through the script context:

` print(string) `- Adds a message to the activity log.
` getData(url) `- returns data from the url as a string.
` postData(url,parameters) ` - returns data from the url as a string with the parameter string being passed as post data. The parameters must be url encoded.

The default script is:

```
print('Default message: '+message + ' Lat:'+lat+' Lng:'+lng);
return message;
```
If the app is set up to redirect messages to an external webserver the parameters are appended to the URL in the format ` ?message=MESSAGE&lat=LATITUDE&lng=LONGITUDE`

The url schema is “mtk” and requests can be made similar to ` mtk://shout?message=Hello ` or  ` mtk://message?message=MESSAGE?guid=GUID `where GUID is the guid of the device to send to.

These can be tested using the Workflow app and the open URLs component.


External calls to the HTTP server are:

``` curl ‘http://192.168.1.116:8080/message?message=hello%20from%20a%20goTenna&guid=GUID' ```

Or:

``` curl ‘http://192.168.1.116:8080/shout?message=shout%20from%20a%20goTenna' ```

Or:

``` curl ‘http://192.168.1.116:8080/script?message=shout%20from%20a%20goTenna' ```

# Example code

Example code is currently under development
