import lolDisplay
import lolPhysics
import lolModel

M = [lolModel.Model()]
P = [lolPhysics.SmartOb(M[0])]
D = lolDisplay.Displayer(800, 550, P, M)
D.update(1)
D.mainLoop()
	