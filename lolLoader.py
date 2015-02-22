import lolPoint
import lolModel
from math import sqrt

# This is something like a data file, some day we might want load from a file
class lolLoader:
	def __init__(self, _focalLen = 10):
		self.focalLen = _focalLen
	def loadCube(self, scale = 50):
		numPnts = 8
		pntList_wrld = [lolPoint.lolPoint(-scale, scale, -scale),#0
			lolPoint.lolPoint(-scale, scale, scale),#1
			lolPoint.lolPoint(scale, scale, scale),#2
			lolPoint.lolPoint(scale, scale, -scale),#3
			lolPoint.lolPoint(-scale, -scale, -scale),#4
			lolPoint.lolPoint(-scale, -scale, scale),#5
			lolPoint.lolPoint(scale, -scale, scale),#6
			lolPoint.lolPoint(scale, -scale, -scale)]#7
		numLines = 12
		# The line list is relative, and therefore has no coord specifier
		lineList = [[0, 1],[1, 5],[5, 4],[4, 0],# left wall
			[1, 2],[2, 6],[6, 5],# back wall
			[0, 3],[3, 2],# bottom wall
			[3, 7],[7, 6],# right wall
			[4, 7]]# top wall
		return lolModel.Model(self.focalLen, pntList_wrld, numPnts, lineList, 
			numLines)
	def loadDodec(self, scale =50):	
		numPnts = 20
		sd1 = (scale*(1 + sqrt(5)))/2
		sd2 = (scale*2)/(1 + sqrt(5))
		
		pntList_wrld = [# Orange points
			lolPoint.lolPoint(scale, scale, scale),#0 +++
			lolPoint.lolPoint(-scale, scale, scale),#1 -++
			lolPoint.lolPoint(-scale, -scale, scale),#2 --+
			lolPoint.lolPoint(scale, -scale, scale),#3 +-+
			lolPoint.lolPoint(scale, scale, -scale),#4 ++-
			lolPoint.lolPoint(-scale, scale, -scale),#5 -+-
			lolPoint.lolPoint(-scale, -scale, -scale),#6 ---
			lolPoint.lolPoint(scale, -scale, -scale),#7 +--
			# Green points
			lolPoint.lolPoint(0, sd2, sd1),#8 0++
			lolPoint.lolPoint(0, -sd2, sd1),#9 0-+
			lolPoint.lolPoint(0, sd2, -sd1),#10 0+-
			lolPoint.lolPoint(0, -sd2, -sd1),#11 0--
			# Blue points
			lolPoint.lolPoint(sd2, sd1, 0),#12 ++0
			lolPoint.lolPoint(-sd2, sd1, 0),#13 -+0
			lolPoint.lolPoint(-sd2, -sd1, 0),#14 --0
			lolPoint.lolPoint(sd2, -sd1, 0),#15 +-0
			# Pink points
			lolPoint.lolPoint(sd1, 0, sd2),#16 +0+
			lolPoint.lolPoint(-sd1, 0, sd2),#17 -0+
			lolPoint.lolPoint(sd1, 0, -sd2),#18 +0-
			lolPoint.lolPoint(-sd1, 0, -sd2)]#19 -0-
		numLines = 15
		# The line list is relative, and therefore has no coord specifier
		# Top hexagon
		# Orange points
		lineList = [
			# Blue points
			# make a house
			[6, 14],[14, 2],# left
			[15,14],
			[7, 15],[15, 3],# right
			# upsidedown a house 12 n 13
			[4, 12],[12, 0],# left
			[13,12],
			[5, 13],[13, 1],# right
			# Green points
			[4, 10],[10, 5],# top
			[10,11],
			[6, 11],[11, 7],# bottom
			[0, 8],[8, 1],# top
			[8,9],
			[2, 9],[9, 3],# bottom
			# Pink points
			[7, 18],[18, 4],# front
			[16, 18],
			[3, 16],[16, 0],# back
			[6, 19],[19, 5],# front
			[17, 19],
			[2, 17],[17, 1]# back
			]
		return lolModel.Model(self.focalLen, pntList_wrld, numPnts, lineList, 
			numLines)