#!/usr/bin/env python
# coding=utf-8
import fbconsole
import sys

#fbconsole.APP_ID = '702463706522649'
#fbconsole.automatically_authenticate('LOGIN','PASS','9cbf04214ed96eb7bf859edb2990acf4','request_uri')
#status = fbconsole.post('/me/feed', {'message':'Hello from my awesome script'})

fbconsole.APP_ID = '702463706522649'
fbconsole.AUTH_SCOPE = [ 'manage_pages','publish_actions']
fbconsole.authenticate()
msg = sys.argv
status = fbconsole.post("/me/feed", {"message":msg[1]})