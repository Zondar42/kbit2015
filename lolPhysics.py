import math
import lolModel

# The way points will have to be moved out into an AI object
class MobileOb:
	# spd: speed in pixels per second
	def __init__(self, _target, _model, _spd = 4, _pos = [0, 0, 0]):
		self.target = _target
		self.model = _model
		self.spd = _spd/1000;
		self.pos = _pos
		# start with a heading so we actually reach somthing if we're allready on target
		self.heading = [1, 1, 1]
		self.getDist()
		self.getHeading()
	def update(self, timeDelta_ms):
		# Move towards the target
		for i in range(0,2):
			self.pos[i] = self.heading[i]*timeDelta_ms
		print self.pos
	def getHeading(self):
		totTargetDist = self.targetDist[0] + self.targetDist[1] + self.targetDist[2]
		print totTargetDist
		if totTargetDist != 0:
			self.heading[0] = (self.targetDist[0]*self.spd)/totTargetDist
			self.heading[1] = (self.targetDist[1]*self.spd)/totTargetDist
			self.heading[2] = (self.targetDist[2]*self.spd)/totTargetDist
		print " heading"
		print self.heading
		print " speed"
		print self.spd
	def getDist(self):
		self.targetDist = [self.target[0] - self.pos[0],
			self.target[1] - self.pos[1],
			self.target[2] - self.pos[2]]
		print " target distance"
		print self.targetDist
		
# The way points will have to be moved out into an AI object
class SmartOb(MobileOb):
	# takes speed in pixels per second
	def __init__(self, _model, _spd = 5, _pos = [0, 0, 0]):
		self.wayPntList =[[0, 0, 0],
			[0, 0, -200],
			[0, 200, -200],
			[200, 200, -200],
			[200, 0, -200],
			[200, 0, 0] ]
		self.numWyPnt = 5
		self.currWyPnt = 1
		self.target = self.wayPntList[self.currWyPnt]
		MobileOb.__init__(self, self.target, _model, _spd, _pos)
	
	def _update(self, timeDelta_ms): 	
		MobileOb.update(self, timeDelta_ms)
	def _update(self, timeDelta_ms): 	
		self.areWeThereYet(self.target)
		MobileOb.update(self, timeDelta_ms)
	
	def areWeThereYet(self, pnt):
		MobileOb.getDist(self)
		for i in range(0,2):
			# See if the distance sign is the oposite of the heading
			#  that must mean we passed out target, time to get the next one
			if (self.targetDist[i] < 0 and self.heading[i] > 0) or (self.targetDist[i] > 0 and self.heading[i] < 0):
				MobileOb.getDist(self)
				self.currWyPnt = (self.currWyPnt + 1)%self.numWyPnt
				MobileOb.getHeading(self)
				print "New target aquired: "
				print self.currWyPnt
				return True
		return False
	
		
		