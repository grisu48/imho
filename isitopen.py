#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import sys
import json
import datetime


# Default URLS to be checked
DEFAULT_URLS = ['http://it-syndikat.org/status.php']


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


if __name__ == "__main__":	
	urls = []
	verbose = False

	# Use program arguments as urls
	for iArg in range(1, len(sys.argv)) :
		arg = sys.argv[iArg]
		if len(arg.strip()) == 0 : continue
		if arg[0] == '-' :	# Program parameter
			if arg == "-h" or arg == "--help" :
				print "isITopen Script - Determine the OPEN status of your hackerspace"
				print "  2016, Phoenix <felix@feldspaten.org>"
				print ""
				print "Usage: " + str(sys.argv[0]) + " [OPTIONS] [URLS]"
				print "OPTIONS:"
				print "  -h               Print help message"
				print "  -v               Verbosity on"
				sys.exit(0)
			elif arg == "-v" or arg == "--verbose":
				verbose = True
			else :
				sys.stderr.write("Illegal argument: " + arg + "\n")
				sys.exit(1)

		else :
			urls.append(arg)
	
	if len(urls) == 0 : urls = DEFAULT_URLS
	for url in urls:
		try:
			if verbose : print "Checking URL '" + url + "' ... "
			checkUrl(url)
		except Exception as e:
			sys.stderr.write("Error opening url '" + str(url) + "': " + str(e) + "\n")
		

