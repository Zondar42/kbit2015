import Tkinter

class Displayer:
	def __init__(self, _width, _height):
		self.height = _height
		self.halfHeight = _height/2
		self.width = _width
		self.halfWidth  = _width/2
		self.focalLen = 100
		self.camPos_wrld = (70, 70, 0)
		self.tkMaster = Tkinter.Tk()
		self.canvas = Tkinter.Canvas(self.tkMaster, width=self.width , height=self.height)
		self.canvas.pack()
		#self.line = [[0 for x in range(5)] for x in range(5)] 
		self.m = Model(self.focalLen, self.camPos_wrld)
	def drawModel(self, model):
		model.generateLineList(self.camPos_wrld)
		for i in range(0, model.numLines):
			# consult the line list to figure out which point to write out
			pnt1 = model.lineList[i][0]
			pnt2 = model.lineList[i][1]
			self.canvas.create_line(model.pntList_cam[pnt1][0] + self.halfWidth, 
				model.pntList_cam[pnt1][1] + self.halfHeight, 
				model.pntList_cam[pnt2][0] + self.halfWidth, 
				model.pntList_cam[pnt2][1] + self.halfHeight, 
				fill="green")
	def update(self):
		self.drawModel(self.m)
	def mainLoop(self):
		self.tkMaster.mainloop()
		
class Model:
	def __init__(self, _focalLen, _camPos_wrld):
		self.camPos_wrld = [0,0]#to force generateLineList to rub
		self.focalLen = _focalLen
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
		self.generateLineList(_camPos_wrld)

	def generateLineList(self, _camPos_wrld):
	# this probably wont work because of reference magic
		if self.camPos_wrld != _camPos_wrld:
		# if the player has moved reproject all the points
			self.camPos_wrld = _camPos_wrld
			self.pntList_cam = []
			for i in range(0, self.numPnts):
				self.pntList_cam.append(self.getCamPnt(self.pntList_wrld[i], self.camPos_wrld))
		
	def getCamPnt(self, pnt_wrld, camPos_wrld):
		# Project the world line and dehomogenize
		_pnt_cam = [self.focalLen*pnt_wrld[0] + camPos_wrld[0]*pnt_wrld[3],
			self.focalLen*pnt_wrld[1] + camPos_wrld[1]*pnt_wrld[3],
			pnt_wrld[2] + camPos_wrld[2]*pnt_wrld[3]]
		print _pnt_cam[2]
		pnt_cam = [_pnt_cam[0]/_pnt_cam[2], _pnt_cam[1]/_pnt_cam[2], 1]
		return pnt_cam
		