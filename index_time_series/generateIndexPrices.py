#!/usr/bin/python

import math, random, datetime

graphStart = datetime.datetime(1, 1, 2, 10, 0) # 10:00
graphEnd = datetime.datetime(1, 1, 2, 18, 0)	# 18:00

class basePriceGenerator():
	price = 0.0
	NO_VALUE=-0.00000001

	def getPriceAtTime(self, dt):
		if dt < self.startTime or dt > self.stopTime:
			return self.NO_VALUE
		elif dt == self.startTime:
			return 0.0
		else:
			self.price += (random.choice([-1,1]) * math.log(random.random())/self.beta)
			return self.price


class xjoPriceGenerator(basePriceGenerator):
	startTime = datetime.datetime(1, 1, 2, 10, 0) # 10:00
	stopTime = datetime.datetime(1, 1, 2, 16, 30) # 16:30
	beta = 100


class kospiPriceGenerator(basePriceGenerator):
	startTime = datetime.datetime(1, 1, 2, 11, 0) # 11:00
	stopTime = datetime.datetime(1, 1, 2, 17, 0) # 17:00
	beta = 30


class nikkeiPriceGenerator(basePriceGenerator):
	startTime = datetime.datetime(1, 1, 2, 11, 0) # 11:00
	stopTime = datetime.datetime(1, 1, 2, 17, 30) # 17:30
	beta = 50

xjo = xjoPriceGenerator()
kospi = kospiPriceGenerator()
nikkei = nikkeiPriceGenerator()

dt = graphStart

print "timeofday,xjo,kospi,nikkei"

while dt < graphEnd:
	dt += datetime.timedelta(0,60) # Add one minute
	print "%s,%.8f,%.8f,%.8f" % \
			(dt.time(), \
			xjo.getPriceAtTime(dt), \
			kospi.getPriceAtTime(dt), \
			nikkei.getPriceAtTime(dt))
	 
