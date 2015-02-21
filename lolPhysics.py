import math
import lolModel

# The way points will have to be moved out into an AI object
class MobileOb:
	def __init__(self, _target, _model, _spd = 4, _pos = [0, 0, 0]):
		self.target = _target
		self.model = _model
		self.spd = _spd;
		self.pos = _pos
		self.getDist()
		self.getHeading()
		
	def update(self, tDelta):
		# Move towards the target
		for i in range(0,2):
			self.pos[i] = self.pos[i] = self.heading[i]*tDelta
			
	def getHeading(self):
		totTargetDist = self.targetDist[0] + self.targetDist[1] + self.targetDist[2]
		if totTargetDist != 0:
			self.heading[0] = (self.targetDist[0]*self.spd)/totTargetDist
			self.heading[1] = (self.targetDist[1]*self.spd)/totTargetDist
			self.heading[2] = (self.targetDist[2]*self.spd)/totTargetDist
		
	def getDist(self):
		self.targetDist = [self.target[0] - self.pos[0],
			self.target[1] - self.pos[1],
			self.target[2] - self.pos[2]]
		
# The way points will have to be moved out into an AI object
class SmartOb(MobileOb):
	def __init__(self, _model, _spd = 2, _pos = [0, 0, 0]):
		self.wayPntList =[[0, 0, 0],
			[0, 0, -200],
			[0, 200, -200],
			[200, 200, -200],
			[200, 0, -200],
			[200, 0, 0] ]
		self.numWyPnt = 5
		self.currWyPnt = 0
		self.target = self.wayPntList[self.currWyPnt]
		MobileOb.__init__(self, self.target, _model, _spd, _pos)
	
	def update(self, tDelta):
		if(self.areWeThereYet(self.target)):
			self.getDist()
			self.getHeading()
		#MobileOb.update(tDelta)
	
	def areWeThereYet(self, pnt):
		self.getDist()
		for i in range(0,2):
			# See if the distance sign is the oposite of the heading
			#  that must mean we passed out target, time to get the next one
			if (self.targetDist[i] < 0 and self.heading[i] > 0) or (self.targetDist[i] > 0 and self.heading[i] < 0):
				self.getDist()
				self.currWyPnt = (self.currWyPnt + 1)%self.numWyPnt
				getHeading()
				return True
		return False
	
		
		