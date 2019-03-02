#!/usr/bin/python
import json
import datetime
import time

# Globals
messagesArray = []

def addMessage(message):
    messagesArray.insert(0,message)
    if len(messagesArray) > 100:
        messagesArray.pop()

# Setup GoTenna

print 'loading goTenna Library'

import goTenna
print 'goTenna Library loaded'

SDK_TOKEN = '**** SDK TOKEN GOES HERE ****'

def event_callback(event):
    if (event.event_type == goTenna.driver.Event.MESSAGE):
        if event.message.payload.message != '':
            newMessage = str(event.message.payload.sender_initials)+', '+str(event.message.payload.message)
            print 'MESSAGE:'+newMessage
            addMessage(newMessage)
        else:
            print('could not decode message.')
    elif (event.event_type != 3):
        print(event.event_type)

print 'Generating Gid'
gid = goTenna.settings.GID.generate(goTenna.settings.GID.PRIVATE)

print 'Setting up Gid'

geo_settings = goTenna.settings.GeoSettings(region=2)
settings = goTenna.settings.GoTennaSettings(None, geo_settings)
api = goTenna.driver.Driver(SDK_TOKEN, gid, settings,event_callback)

def handleSend(*args, **kwargs):
    print('Broadcast sent')

def send(message):
    addMessage(message)
    payload = goTenna.payload.TextPayload(message)
    api.send_broadcast(payload,handleSend)

print 'Starting API'
api.start()
print 'API Started'


# Setup Webserver
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import urllib

PORT_NUMBER = 8080
class myHTTPhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = urllib.unquote(self.path)[1:]
        responseMessage = 'No handler'
        if (message == ''):
            # Default request - send default html
            fileHandle = open("/gotenna/index.html", "r")
            responseMessage = fileHandle.read()
            fileHandle.close()
        elif (message == 'index.html' or message == 'favicon.ico'):
            print 'Ignoring request:'+message
            responseMessage = 'Ignoring request'
        elif (message == 'timestamp'):
            print 'Timestamp request'
            responseMessage = 'Keepalive ' + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            send(responseMessage)
        elif (message == 'messages'):
            responseMessage = json.dumps(messagesArray)
        else:
            send(message)
            print 'Request:'+message
            responseMessage = 'Message sent'
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(responseMessage)
        return

try:
	server = HTTPServer(('', PORT_NUMBER), myHTTPhandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	server.serve_forever()
except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
    api.disconnect()
    api.stop()

