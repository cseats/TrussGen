import matplotlib.pyplot as plt

def forceDiagram(nodeDict, polygons):
    fig, ax = plt.subplots()
    for pNum, coords in nodeDict.items():
        x, y = coords
        ax.plot(x, y, 'bo')  # 'bo' means blue circle
        ax.text(x, y, f' {pNum}', fontsize=12, ha='right', color='blue')
        
    for p,data in polygons.items():

        n1x,n1y = nodeDict[p]
        n2x,n2y = nodeDict[data['neighbors'][0]]
        n3x,n3y = nodeDict[data['neighbors'][1]]

        ax.plot([n1x,n2x],[n1y,n2y])
        ax.plot([n1x,n3x],[n1y,n3y])
    plt.show()