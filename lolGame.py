import lolDisplay
import lolPhysics
import lolModel

print "++++++++++ WELCOM TO LE LOLGAME!! ++++++++++"
M = [lolModel.Model()]
P = [lolPhysics.SmartOb(M[0])]
D = lolDisplay.Displayer(800, 550, P, M)
D.mainLoop()
print "++++++++++++++++++ WEAK... +++++++++++++++++"
