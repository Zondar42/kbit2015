from math import sqrt
class lolPoint:
	def __init__(self, _x, _y, _z, _s = 1.0):
		self.x = _x
		self.y = _y
		self.z = _z
		self.s = _s
		
	def get(self, index):
		if index == 0:
			return self.x
		if index == 1:
			return self.y
		if index == 2:
			return self.z
		if index == 3:
			return self.s
			
	def set(self, index, val):
		if index == 0:
			self.x = val
		if index == 1:
			self.y = val
		if index == 2:
			self.z = val
		if index == 3:
			self.s = val

	def add(self, pnt):
		ret = lolPoint(0.0, 0.0, 0.0)
		for i in range(0, 3):
			ret.set(i, self.get(i) + pnt.get(i))
		return ret
		
	def sub(self, pnt):
		ret = lolPoint(0.0, 0.0, 0.0)
		for i in range(0, 3):
			ret.set(i, self.get(i) - pnt.get(i))
		return ret
		
	def dot(self, pnt):
		ret = 0.0
		for i in range(0, 3):
			ret = ret + self.get(i)*pnt.get(i)
		return ret
		
	def dev(self, scalar):
		ret = lolPoint(0.0, 0.0, 0.0)
		for i in range(0, 3):
			ret.set(i, self.get(i)/scalar)
		return ret
		
	def mul(self, scalar):
		ret = lolPoint(0.0, 0.0, 0.0)
		for i in range(0, 3):
			ret.set(i, self.get(i)*scalar)
		return ret
		
	def homogenize(self):
		self.dev(self.s)
		self.s = 1
	
	# find the distance between two points
	def distance(self, pnt):
		diff = self.sub(pnt)
		return sqrt(diff.dot(diff))
		
	def show(self):
		s =  "[ " + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + " ]"
		print s