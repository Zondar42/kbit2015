import lolDisplay
import lolPhysics
import lolLoader
import lolPoint

print "++++++++++ WELCOM TO LE LOLGAME!! ++++++++++"
L = lolLoader.lolLoader(500)
M = [L.loadDodec(20), L.loadDodec(100), L.loadDodec(10), L.loadDodec(50)]
pos1 = lolPoint.lolPoint(0, 500, 500)
pos2 = lolPoint.lolPoint(-200, 0, 5000)
pos3 = lolPoint.lolPoint(100, 300, 20)
pos4 = lolPoint.lolPoint(-400, 200, 1000)
P = [lolPhysics.Doodad(M[0], pos1), 
	lolPhysics.Doodad(M[1], pos2), 
	lolPhysics.Doodad(M[2], pos3), 
	lolPhysics.Doodad(M[3], pos4)]
D = lolDisplay.Displayer(1000, 600, P, M)
D.mainLoop()
print "++++++++++++++++++ WEAK... +++++++++++++++++"
