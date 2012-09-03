# Find out available id numbers
# My version of Justin's Ruby implementation (https://github.com/j95tin/idphoto)

import urllib2

startId = 0
endId = 20000
logFile = open('photolist.txt', 'w')
print "starting program"
print "From #%s to #%s" % (startId, endId)
for i in range(startId, endId):
	url = "https://mystudent.fjuhsd.net/images/808/%s.jpg" % i
	try:
		f = urllib2.urlopen(urllib2.Request(url))
		validUrl = True
	except:
		validUrl = False
		print "error \n"
	if validUrl :
		logFile.write("%s, " % i)
	print i
logFile.close()