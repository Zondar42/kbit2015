import Tkinter
import lolPhysics
import lolModel

class Displayer:
	def __init__(self, _width, _height, _mobList, _modelList):
		self.height = _height
		self.halfHeight = _height/2
		self.width = _width
		self.halfWidth  = _width/2
		self.mobList = _mobList
		self.modelList = _modelList
		self.focalLen = 100
		self.camPos_wrld = (70, 70, 0)
		self.tkMaster = Tkinter.Tk()
		self.canvas = Tkinter.Canvas(self.tkMaster, width=self.width, 
			height=self.height, background='black')
		self.canvas.pack()
		
	def drawModel(self, pointList_cam, model):
		# Consult the line list to figure out which point to write out
		for line in model.lineList:
			# The line list is always the same for a given model
			linePnt1 = line[0]
			linePnt2 = line[1]
			# The point list is unique to the mob and camera
			self.canvas.create_line(pointList_cam[linePnt1][0] + self.halfWidth, 
				pointList_cam[linePnt1][1] + self.halfHeight, 
				pointList_cam[linePnt2][0] + self.halfWidth, 
				pointList_cam[linePnt2][1] + self.halfHeight, 
				fill="green")

	def update(self, tDelta):
		for model in self.modelList:
			model.updateCamPos(self.camPos_wrld)
		for mob in self.mobList:
			mob.update(tDelta)
			self.drawModel(mob.model.generatePointList(mob.pos), mob.model)
			
	def mainLoop(self):
		self.tkMaster.mainloop()
