import lolPoint
import lolModel
import copy
from math import sqrt

# The way points will have to be moved out into an AI object
class MobileOb:
	# spd: speed in pixels per second
	def __init__(self, _target, _model, _spd = 4.0, _pos = lolPoint.lolPoint(0, 0, 0)):
		self.target = _target
		self.model = _model
		self.pos = _pos
		# start with a velocity so we actually reach somthing if we're allready on target
		self.velocity = lolPoint.lolPoint(1.0, 1.0, 1.0)
		self.setSpeed(_spd)

	def update(self, timeDelta_ms):
		# Move towards the target
		dist = self.velocity.mul(timeDelta_ms)
		self.pos = self.pos.add(dist)
	
	def getVelocity(self):
		self.getDist()
		if self.totTargetDistSqrd != 0:
			apparentSpd = (((self.targetDist.x + self.targetDist.y + 
				self.targetDist.z)* self.spd) / 
				(sqrt(self.totTargetDistSqrd)))
			for i in range(0,3):
				# Determine the length of the component parts of the travel vec
				sqrdCmpntLen = (self.totTargetDistSqrd - 
					self.targetDistSqrd.get((i+1)%3) - 
					self.targetDistSqrd.get((i+2)%3))
				print "sqrdCmpntLen"
				print sqrdCmpntLen
				# sqrdCmpntLen should only be negative by a small amount due 
				#  to float errors
				if sqrdCmpntLen >= 0:
					componentLen = sqrt(sqrdCmpntLen)
					self.velocity.set(i, (apparentSpd * componentLen) / self.totTargetDistSqrd )
				else:
					# If the component dimension is zero, we have no velocity 
					#  in that dimension
					self.velocity.set(i, 0)
			print "Velocity"
			self.velocity.show()

	# Calculate distance to target, both as a vector and as raw distance squared
	def getDist(self):
		self.targetDist = self.target.sub(self.pos)
		#print "targetDist"
		#self.targetDist.show()
		# Its a bit odd to have this in mob, but its really more about physics then
		#  linear algebra
		self.targetDistSqrd = lolPoint.lolPoint(self.targetDist.x**2,
			self.targetDist.y**2, 
			self.targetDist.z**2)
		self.totTargetDistSqrd = (self.targetDistSqrd.x + 
			self.targetDistSqrd.y + self.targetDistSqrd.z)
		
	def setSpeed(self, newSpeed):
		self.spd = newSpeed;
		self.spdSqrd = self.spd**2;
		self.getVelocity()
		
		
# The way points will have to be moved out into an AI object
class SmartOb(MobileOb):
	# takes speed in pixels per second
	def __init__(self, _model, _spd = 200.0, _pos = lolPoint.lolPoint(0, 0, 250)):
		self.wayPntList =[lolPoint.lolPoint(0, 0, 20),
			lolPoint.lolPoint(0, 0, 1020),
			lolPoint.lolPoint(0, 1000, 1020),
			lolPoint.lolPoint(1000, 1000, 1020),
			lolPoint.lolPoint(1000, 0, 1020),
			lolPoint.lolPoint(1000, 0, 20) ]
		self.numWyPnt = 5
		self.currWyPnt = 1
		self.target = self.wayPntList[self.currWyPnt]
		self.epsilon = 20
		MobileOb.__init__(self, self.target, _model, _spd, _pos)
	
	def update(self, timeDelta_ms):
		self.lastPos = copy.deepcopy(self.pos)
		MobileOb.update(self, timeDelta_ms)
		self.areWeThereYet(self.target)
		
	def areWeThereYet(self, pnt):
		MobileOb.getDist(self)
		# Check if we're close enough to the target, but also if we've 
		#  passed it
		if self.colide(self.target):
			print "Old target : "
			self.target.show()
			print "Reached: "
			self.pos.show()
			MobileOb.getDist(self)
			self.currWyPnt = (self.currWyPnt + 1)%self.numWyPnt
			self.target = self.wayPntList[self.currWyPnt]
			MobileOb.getVelocity(self)
			print "New target : "
			self.target.show()
			print "--"
			return True
		return False
	
	def colide(self, point):
		moveLine = [self.pos, self.lastPos]
		if self.distance(point, moveLine) < self.epsilon:
			return True
		return False
		
	# find the distance between a point and a line
	def distance(self, point, line):
		line_rel = line[1].sub(line[0])
		supportlLine_rel = point.sub(line[0])
		c1 = supportlLine_rel.dot(line_rel)
		
		if ( c1 <= 0 ):  # before beginning of the line
			return point.distance(line[0])
			
		c2 = line_rel.dot(line_rel)
		if ( c2 <= c1 ): # after the end of the line
			return point.distance(line[1])
		
		# If we made it this far, the closest point is somewhere inside the line
		#  Segment
		scalFactor = c1 / c2
		P = line[0].add(line_rel.mul(scalFactor));
		return point.distance(P)
		