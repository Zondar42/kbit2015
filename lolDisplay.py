import Tkinter
from Tkinter import Tk
import time
import lolPhysics
import lolModel
import lolPoint

	
class Displayer:
	def __init__(self, _width, _height, _mobList, _modelList, _maxFPS = 10):
		self.height = _height
		self.halfHeight = _height/2
		self.width = _width
		self.halfWidth  = _width/2
		self.mobList = _mobList
		self.modelList = _modelList
		self.maxFPS = _maxFPS
		self.frameDelay = 1000/self.maxFPS
		self.focalLen = 100
		self.camPos_wrld = lolPoint.lolPoint(0, 0, 0)
		self.tkMaster = Tkinter.Tk()
		self.canvas = Tkinter.Canvas(self.tkMaster, width=self.width, 
			height=self.height, background='black')
		
		# TEST
		self.canvas.bind("<1>", lambda event: self.canvas.focus_set())
		self.canvas.bind("<Key>", self.key)
		self.canvas.pack()
		
	def key(self, event):
		if event.char == "w":
			self.camPos_wrld.y += 10
		if event.char == 's':
			self.camPos_wrld.y -= 10
		if event.char == 'd':
			self.camPos_wrld.x -= 10
		if event.char == 'a':
			self.camPos_wrld.x += 10
		if event.char == 'q':
			self.camPos_wrld.z -= 10
		if event.char == 'e':
			self.camPos_wrld.z += 10
		
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
	#takes care of the timing overhead and then calls the real update
	def update(self):
		# figure out how much time has passed since we last updated
		endTime_ms = time.clock()*1000
		timeDelta_ms = endTime_ms - self.startTime_ms
		self.startTime_ms = time.clock()*1000
		
		# Do all the important stuff
		self._update(timeDelta_ms)

		# Try to set the frame delay so we reach the target frame delay
		secondEndTime_ms = time.clock()*1000
		spentTime_ms = secondEndTime_ms - endTime_ms
		nextDelay = self.frameDelay - spentTime_ms
		self.tkMaster.after(int(nextDelay), self.update)
	
	# Takes timeDelta_ms time change in milliseconds
	def _update(self, timeDelta_ms):
		# replace with calls moving lines instead
		self.canvas.delete('all')
		for model in self.modelList:
			model.updateCamPos(self.camPos_wrld)
		for mob in self.mobList:
			mob.update(timeDelta_ms)
			if(mob.model.isVisible(mob.pos)):
				self.drawModel(mob.model.generatePointList(mob.pos), mob.model)
			
	def mainLoop(self):
		self.startTime_ms = time.clock()*1000
		self.tkMaster.after(self.frameDelay, self.update)
		self.tkMaster.mainloop()
