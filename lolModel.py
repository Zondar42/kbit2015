import lolPoint

class Model:
	def __init__(self, _focalLen, _pntList_wrld, _numPnts, _lineList, _numLines):
		self.camPos_wrld = lolPoint.lolPoint(0, 0, 0)
		self.pos = lolPoint.lolPoint(0, 0, 0)
		self.focalLen = _focalLen
		self.pntList_wrld = _pntList_wrld
		self.numPnts = _numPnts
		self.lineList = _lineList
		self.numLines = _numLines

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