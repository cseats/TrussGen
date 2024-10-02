
import data
import forceDiagramGen
import stockAssignment
import drawTruss
import func
import calcs

import matplotlib.pyplot as plt


nodeDict, stock, polygons, loadNodes, mems, stockLib = data.getInitial()


cont  = True
fig, ax = plt.subplots()
xi = 0
macroData = {}
ind = 1
for j in range(10):
    yi = 0
    
    for i in range(10):
        
        while cont:

            memData,nodeData,stockLib = forceDiagramGen.create(nodeDict, stock, polygons, loadNodes, mems, stockLib)

            assign = stockAssignment.assignPrep(memData,stockLib)
            
            if not assign:
                print("Could not build -- Trying again\n")
            
            else:
                macroData[ind] = {
                    'memberInfo': memData,
                    'polygons': polygons,
                    'nodeDict': nodeData,
                    'stockLib': stockLib,
                    'assignment': assign
                }
                ind += 1
                print('--------------------------------------')
                print('Success Found!')
                print(assign)
                fig,ax = drawTruss.draw_truss2(memData, nodeData,fig, ax,xi,yi)
                cont = False
        cont = True
        yi += 10
    xi+=15

singleDesigns, macroData = func.removeDups(macroData)

for k,v in singleDesigns.items():
    print(f'Design {k} ----  {v}')
# print(singleDesigns)
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(-10, 160)
plt.ylim(-5,120)
ax.set_aspect('equal', 'box')
plt.title('Truss Structure')
plt.grid(False)
plt.show()
print("WHO IS DOG")
macroData = calcs.getMetrics(macroData)
data.writeResults(macroData)