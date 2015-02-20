import Tkinter

class Displayer:
	def __init__(self, _width, _height):
		self.tkMaster = Tkinter.Tk()
		self.canvas = Tkinter.Canvas(self.tkMaster, width=_width, height=_height)
		self.canvas.pack()
		#self.line = [[0 for x in range(5)] for x in range(5)] 
		self.m = Model()
	def drawModel(self, model):
		for i in range(0, model.numPoints):
			j = (i + 1)%model.numPoints
			self.canvas.create_line(model.contour[i][0], model.contour[i][1], model.contour[j][0], model.contour[j][1], fill="red")
	def update(self):
		self.drawModel(self.m)
	def mainLoop(self):
		self.tkMaster.mainloop()
		
class Model:
	def __init__(self):
		self.numPoints = 3 
		self.contour = [[50, 100, 0], [100, 10, 0], [100, 100, 0]] 
		