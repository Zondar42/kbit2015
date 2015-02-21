class Point:
	def add(self, vec):
	def sub(self, vec):
	# find the distance between a point and a line
	def distance(self, point, line):
		line_rel = line[1] - line[0]
		supportlLine_rel = point - line[0]
		c1 = self.dot3d(supportlLine_rel, line_rel)
		if ( c1 <= 0 )  # before beginning of the line
            return self.distance(point, line[0])
		c2 = self.dot3d(line_rel, line_rel)
		if ( c2 <= c1 ) # after the end of the line
			return self.distance(point, line[1])
]
		b = c1 / c2
		P = line[0] + b * line_rel;
		return self.distance(point, Pb)
	
	# find the distance between two points
	def distance(self, pnt1, pnt2):
		diff = 0
		for i in range(0,3):
			diff = diff + pnt1[i]-pnt2[i]
		return math.sqrt(self.dot3d(diff,diff)))
		
	def dot3d(vec1, vec2):
		ret = 0
		for i in range(0,3):
			ret = ret + vec1[i]*vec2[i]
		return ret