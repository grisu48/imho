#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
	import urllib2
	import sys
	import json
	import datetime
except Exception as e:
	print "Import error:",str(e)
	sys.exit(1)

urls = ['http://it-syndikat.org/status.php']


def checkUrl(url):
	t = urllib2.urlopen(url)
	data = t.read()
	jsonData = json.loads(data)
	status = jsonData["open"]
	name = jsonData["space"]
	lastChange = int(jsonData["lastchange"])
	if type(status) is bool :
		pass
	else:
		status = str(status).lower()
		status = status == "true"
	lastChange = datetime.datetime.fromtimestamp(lastChange).strftime('%Y-%m-%d %H:%M:%S')
	if (status == True):
		print str(name) + " is OPEN! (since " + str(lastChange) + ")"
	else:
		print str(name) + " is CLOSED! (since " + str(lastChange) + ")"

for url in urls:
	try:
		checkUrl(url)
	except Exception as e:
		print "Error opening url '" + str(url) + "': " + str(e)

