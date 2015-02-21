
class Model:
	def __init__(self):
		self.focalLen = 100
		self.camPos_wrld = [0,0,0]
		self.pos = [0, 0, 0]
		self.numLines = 12
		self.numPnts = 8
		self.pntList_wrld = [[-50, 50, 50, 1],#0
			[-50, 50, 150, 1],#1
			[50, 50, 150, 1],#2
			[50, 50, 50, 1],#3
			[-50, -50, 50, 1],#4
			[-50, -50, 150, 1],#5
			[50, -50, 150, 1],#6
			[50, -50, 50, 1]]#7
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
	
	def generatePointList(self, pos_wrld):
		# if the player has moved reproject all the points
		pntList_cam = []
		for i in range(0, self.numPnts):
			pntList_cam.append(self.getCamPnt(self.pntList_wrld[i], pos_wrld))
		return pntList_cam

	def getCamPnt(self, vertex_wrld, pos_wrld):
		pnt_wrld = []
		for i in range(0, 3):
			pnt_wrld.append(vertex_wrld[i] + pos_wrld[i])
		# Add the scaling value, starts at 1
		pnt_wrld.append(1)
		
		# Project the world line and dehomogenize
		_pnt_cam = [self.focalLen*pnt_wrld[0] + self.camPos_wrld[0]*pnt_wrld[3],
			self.focalLen*pnt_wrld[1] + self.camPos_wrld[1]*pnt_wrld[3],
			pnt_wrld[2] + self.camPos_wrld[2]*pnt_wrld[3]]
		print _pnt_cam[2]
		pnt_cam = [_pnt_cam[0]/_pnt_cam[2], _pnt_cam[1]/_pnt_cam[2], 1]
		return pnt_cam