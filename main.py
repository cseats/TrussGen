
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
yi = 0
macroData = {}
ind = 1
for j in range(5):
    xi = 0
    
    for i in range(5):
        
        while cont:

            memData,nodeData,stockLib, build = forceDiagramGen.create(nodeDict, stock, polygons, loadNodes, mems, stockLib)
            if build:
                assign = stockAssignment.assignPrep(memData,stockLib)
            else:
                assign = False
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
                print(f'>>> Success Found! Design Number: {ind}')
                print(assign)
                fig,ax = drawTruss.draw_truss2(memData, nodeData,fig, ax,xi,yi)
                cont = False
        cont = True
        xi+=15
    yi += 10

singleDesigns = func.removeDups(macroData)

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