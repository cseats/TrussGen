
import forceDiagramGen
import stockAssignment
import drawTruss
import func
import calcs

import matplotlib.pyplot as plt
import time


polyNum = 10

if polyNum == 14:
    import data14 as data
elif polyNum == 6:
    import data6 as data
elif polyNum == 10:
    import data10 as data
else:
    raise Exception("A data file is required, none provided for the specified # of polygons.")

def main():
    start_time = time.time()
    nodeDict, stock, polygons, loadNodes, mems, stockLib = data.getInitial()


    cont  = True
    fig, ax = plt.subplots()
    xi = 0
    macroData = {}
    ind = 1
    for j in range(1):
        yi = 0
        
        for i in range(1):
            
            while cont:

                memData,nodeData,stockLib, build = forceDiagramGen.create(nodeDict, stock, polygons, loadNodes, mems, stockLib,data)

                if build:
                    assign = stockAssignment.assignPrep(memData,stockLib)
                else:
                    assign = False
                
                if not assign :
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
                    print(f'>>> Success Found! Design # {ind}')
                    print(assign)
                    # fig,ax = drawTruss.draw_truss2(memData, nodeData,fig, ax,xi,yi)
                    cont = False
            cont = True
            yi += 10
        xi+=15
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")
    singleDesigns, macroData = func.removeDups(macroData)
    xi = 0
    yi = 0
    cnt = 1
    for k,v in singleDesigns.items():
        # print(f'Design {k} ----  {v}')
        memData = macroData[k]['memberInfo']
        nodeData = macroData[k]['nodeDict']
        
        fig,ax = drawTruss.draw_truss2(memData, nodeData,fig, ax,xi,yi)
        xi+= 15
        
        if cnt%10 == 0:
            xi = 0
            yi+=10
        cnt+=1
        
    print(f'Completed Designs -- There are {cnt} unique designs!')
    # plt.xlabel('X')
    # plt.ylabel('Y')
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.xticks([])  # Remove x-axis numbers
    plt.yticks([])  # Remove y-axis numbers
    plt.xlim(-10, 160)
    plt.ylim(-5,120)
    ax.set_aspect('equal', 'box')
    plt.title('Truss Structure')
    plt.grid(False)
    plt.show()

    macroData = calcs.getMetrics(macroData)
    data.writeResults(macroData)


if __name__ == "__main__":
    main()