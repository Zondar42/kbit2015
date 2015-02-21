import lolPoint

class Model:
	def __init__(self):
		self.focalLen = 100
		self.camPos_wrld = lolPoint.lolPoint(0, 0, 0)
		self.pos = lolPoint.lolPoint(0, 0, 0)
		self.numLines = 12
		self.numPnts = 8
		self.pntList_wrld = [lolPoint.lolPoint(-50, 50, -50),#0
			lolPoint.lolPoint(-50, 50, 50),#1
			lolPoint.lolPoint(50, 50, 50),#2
			lolPoint.lolPoint(50, 50, -50),#3
			lolPoint.lolPoint(-50, -50, -50),#4
			lolPoint.lolPoint(-50, -50, 50),#5
			lolPoint.lolPoint(50, -50, 50),#6
			lolPoint.lolPoint(50, -50, -50)]#7
		# The line list is relative, and therefore has no coord specifier
		self.lineList = [[0, 1],
			[1, 5],
			[5, 4],
			[4, 0],# left wall
			
			[1, 2],
			[2, 6],
			[6, 5],# back wall
			
			[0, 3],
			[3, 2],# bottom wall
			
			[3, 7],
			[7, 6],# right wall
			
			[4, 7]]# top wall

	def updateCamPos(self, newCamPos):
		self.camPos_wrld = newCamPos
	
	def isVisible(self, pos_wrld):
		for pnt_wrld in self.pntList_wrld:
			if (self.camPos_wrld.z + pos_wrld.z + pnt_wrld.z) <= 0:
				return False
		return True
	def generatePointList(self, pos_wrld):
		# if the player has moved reproject all the points
		#print pos_wrld
		pntList_cam = []
		for i in range(0, self.numPnts):
			pntList_cam.append(self.getCamPnt(self.pntList_wrld[i], pos_wrld))
		return pntList_cam

	def getCamPnt(self, vertex_wrld, pos_wrld):
		pnt_wrld = vertex_wrld.add(pos_wrld)
		# Project the world line and dehomogenize
		_pnt_cam = lolPoint.lolPoint(self.focalLen*(pnt_wrld.x + self.camPos_wrld.x),# + self.camPos_wrld.x * pnt_wrld.z,
			self.focalLen*(pnt_wrld.y + self.camPos_wrld.y),# + self.camPos_wrld.y * pnt_wrld.z,
			(pnt_wrld.z + self.camPos_wrld.z))# + self.camPos_wrld.z * pnt_wrld.z)
		# We dont use a lol point since this is a nonhomogenous 2d point
		pnt_cam = [_pnt_cam.x/_pnt_cam.z, _pnt_cam.y/_pnt_cam.z, ]
		return pnt_cam