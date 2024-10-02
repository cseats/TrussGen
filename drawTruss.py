import data

import matplotlib.pyplot as plt
import math

def draw_truss2(elements, nodes,fig, ax,xi,yi):
    # fig, ax = plt.subplots()
    
    # Plot the nodes
    # for node_id, coordinates in nodes.items():
    #     x, y = coordinates['loc']
        
    #     x += xi
    #     y += yi
        
    #     ax.plot(x, y, 'bo')  # 'bo' means blue circle
        
        
        # ax.text(x, y, f' {node_id}', fontsize=12, ha='right', color='blue')  # Label the nodes
    
    # Plot the elements
    for element_id, node_ids in elements.items():
        node1, node2 = node_ids['start'],node_ids['end']
        x_values = [nodes[node1]['loc'][0]+xi, nodes[node2]['loc'][0]+xi]
        y_values = [nodes[node1]['loc'][1]+yi, nodes[node2]['loc'][1]+yi]
        # x_values += xi
        # y_values += yi
        
        ax.plot(x_values, y_values, color='k')  # 'r-' means red line
        mid_x = (x_values[0] + x_values[1]) / 2
        mid_y = (y_values[0] + y_values[1]) / 2
        # ax.text(mid_x, mid_y, f'{element_id}', fontsize=12, ha='center', va='bottom', color='red')  # Label the elements
    
    return fig,ax
    # ax.set_aspect('equal', 'box')
    # plt.xlabel('X')
    # plt.ylabel('Y')
    # plt.title('Truss Structure')
    # plt.grid(True)
    # plt.show()
    # print("WHO IS DOG")
def draw_truss(elements, nodes):
    fig, ax = plt.subplots()
    
    # Plot the nodes
    for node_id, coordinates in nodes.items():
        x, y = coordinates
        ax.plot(x, y, 'bo')  # 'bo' means blue circle
        ax.text(x, y, f' {node_id}', fontsize=12, ha='right', color='blue')  # Label the nodes
    
    # Plot the elements
    for element_id, node_ids in elements.items():
        node1, node2 = node_ids
        x_values = [nodes[node1][0], nodes[node2][0]]
        y_values = [nodes[node1][1], nodes[node2][1]]
        ax.plot(x_values, y_values, 'r-')  # 'r-' means red line
        mid_x = (x_values[0] + x_values[1]) / 2
        mid_y = (y_values[0] + y_values[1]) / 2
        ax.text(mid_x, mid_y, f'{element_id}', fontsize=12, ha='center', va='bottom', color='red')  # Label the elements
    
    ax.set_aspect('equal', 'box')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Truss Structure')
    plt.grid(True)
    plt.show()

# # Example usage
# elements = {
#     1: [1, 2],
#     2: [2, 3],
#     3: [3, 1],
#     4: [1, 4],
#     5: [2, 4],
#     6: [3, 4]
# }

# nodes = {
#     1: [0, 0],
#     2: [2, 0],
#     3: [1, 2],
#     4: [1, 1]
# }
def find_intersection(line1_point, line1_slope, line2_point, line2_slope):
    """
    This function finds the intersection point of two lines.
    
    Parameters:
    - line1_point: tuple of the x, y coordinates of the first line's origin (x1, y1)
    - line1_slope: slope of the first line (m1)
    - line2_point: tuple of the x, y coordinates of the second line's origin (x2, y2)
    - line2_slope: slope of the second line (m2)
    
    Returns:
    - A tuple representing the (x, y) coordinates of the intersection point, or None if the lines are parallel.
    """
    
    x1, y1 = line1_point
    m1 = line1_slope
    x2, y2 = line2_point
    m2 = line2_slope
    
    # Check if the lines are parallel (if their slopes are equal)
    # if m1 == m2:
    #     return None  # No intersection, the lines are parallel
    if  m1 is False: # vertical m1
        y_intersection = m2*(x1-x2)+y2
        return x1,y_intersection
    if m2 is False: # vertical m1
        y_intersection = m1*(x2-x1)+y1
        return x2,y_intersection
    # Equation of line 1: y = m1 * (x - x1) + y1
    # Equation of line 2: y = m2 * (x - x2) + y2
    # Setting both equal to solve for x:
    # m1 * (x - x1) + y1 = m2 * (x - x2) + y2
    # Rearranging to solve for x:
    x_intersection = (m1 * x1 - m2 * x2 + y2 - y1) / (m1 - m2)
    
    # Use one of the line equations to find the corresponding y value
    y_intersection = m1 * (x_intersection - x1) + y1
    
    return (x_intersection, y_intersection)

# # draw_truss(elements, nodes)
def getSlopes(mems,nodeDict,memData):
    M = {}
    
    for i in range(1,len(memData)):
        # print(memData)
        n1 = mems[memData[i]['name']]['head']
        n2 = mems[memData[i]['name']]['tail']
    # for name,mem in mems.items():
        # n1 = mem['head']
        # n2 = mem['tail']
        
        x1,y1 = nodeDict[str(n1)]
        x2,y2 = nodeDict[str(n2)]
        if x1 == x2:
            m = False #Vertical member
        elif x1>x2:
            m = (y1-y2)/(x1-x2)
        elif x2>x1:
            m = (y2-y1)/(x2-x1)
        else:
            m = "PROBLEM"
        # M[name] = m
        memData[i]['slope'] = m
        memData[i]['r'] = mems[memData[i]['name']]['r']
        memData[i]['mod'] = mems[memData[i]['name']]['mod']
        
    return memData
def getSym(nodeData):
    symmetryMapNode = data.getNodeSym()#{6:2,7:3,8:1}
    symLine = nodeData[5]['loc'][0]
    for new,ref in symmetryMapNode.items():
        
        refCords = nodeData[ref]['loc']
        xDelta = symLine-refCords[0]
        nodeData[new] = {"loc": [refCords[0]+xDelta*2,refCords[1]]}
    return nodeData
def forcediagram2Truss(polygons,mems,nodeDict):
    # memData = {
    # 1:{'name':'1-e', 'start':1,'end':2,'slope':False},
    # 2:{'name':'1-a', 'start':1,'end':3,'slope':False},
    # 3:{'name':'2-1', 'start':2,'end':3,'slope':False},
    # 4:{'name':'2-b', 'start':3,'end':4,'slope':False},
    # 5:{'name':'3-2', 'start':2,'end':4,'slope':False},
    # 6:{'name':'3-e', 'start':2,'end':5,'slope':False},
    # 7:{'name':'3-4', 'start':4,'end':5,'slope':False, 'r':0.805,'mod':1},
    
    # }
    memData,memSym = data.getMem()
    
    memData = getSlopes(mems,nodeDict,memData)
    
    for k,v in memSym.items():
        
        memData[k] = {'name':'1-e', 'start':v['nodes'][0],'end':v['nodes'][1],'slope':False,'r':memData[v['symMem']]['r'],'mod':memData[v['symMem']]['mod']}
    
    # memData[8] = {'name':'1-e', 'start':4,'end':7,'slope':False,'r':memData[4]['r'],'mod':memData[4]['mod']}
    # memData[9] = {'name':'1-e', 'start':4,'end':6,'slope':False ,'r':memData[5]['r'],'mod':memData[5]['mod']}
    # memData[10] = {'name':'1-e', 'start':5,'end':6,'slope':False ,'r':memData[6]['r'],'mod':memData[6]['mod']}
    # memData[11] = {'name':'1-e', 'start':6,'end':7,'slope':False ,'r':memData[3]['r'],'mod':memData[3]['mod']}
    # memData[12] = {'name':'1-e', 'start':7,'end':8,'slope':False ,'r':memData[2]['r'],'mod':memData[2]['mod']}
    # memData[13] = {'name':'1-e', 'start':6,'end':8,'slope':False ,'r':memData[1]['r'],'mod':memData[1]['mod']}
    # # print(m)
    

    # find_intersection(origin, mOrder[], line2_point, line2_slope)
    cont = True
    xInit = 1
    origin = [0,0]
    targetLen = 12
    while cont:
        
        
        # xInit = 1
        # nodeData = {
        #     1:{'name':'A-1', 'mems':False, 'loc': origin,'found':True},
        #     2:{'name':'E-1', 'mems':[1], 'loc': [xInit,0],'found':True},
        #     3:{'name':'1-2', 'mems':[2,3], 'loc': [],'found':False},
        #     4:{'name':'1-2', 'mems':[4,5], 'loc': [],'found':False},
        #     5:{'name':'1-2', 'mems':[6,7], 'loc': [],'found':False},
            
        # }
        nodeData = data.getNodeData()
        nodeData[1]['loc'] = origin
        nodeData[2]['loc'] = [xInit,0]

        for i in range(3,len(nodeData)+1):
            n = nodeData[i]
            if True:#n['found']:
                
                mem1 = n['mems'][0]
                m1 = origin1 = memData[mem1]['slope']
                origin1 = memData[mem1]['start']
                
                x1,y1 = nodeData[origin1]['loc']
                
                mem2 = n['mems'][1]
                m2 = memData[mem2]['slope']
                origin2 = memData[mem2]['start']
                x2,y2 = nodeData[origin2]['loc']
                xi,yi = find_intersection([x1,y1], m1, [x2,y2], m2)
                nodeData[i]['loc'] = [xi,yi]
        
        nodeData = getSym(nodeData)
        
        trussLen = nodeData[8]['loc'][0] - nodeData[1]['loc'][0]
        
        if abs(trussLen-targetLen)<0.01:
            cont = False
            build = True
        elif abs(trussLen-targetLen)>20:
            cont = False
            build = False
        else:
            if abs(trussLen-targetLen)<2:
                xInit += 0.0001
            else:
                xInit += 0.01
        
    # draw_truss2(memData, nodeData)
    memData = calcMemLen(memData,nodeData)
    # print("DOG")
    return nodeData,memData,build

def calcMemLen(mem,nodes):
    
    for i in range(1,len(mem)+1):
        
        n1 = mem[i]['start']
        n2 = mem[i]['end']
        x1,y1 = nodes[n1]['loc']
        x2,y2 = nodes[n2]['loc']
        
        xDelta = x2-x1
        yDelta = y2-y1
        memL = math.sqrt(xDelta**2 + yDelta**2)
        mem[i]['length'] = memL
        
    
    return mem

symmetryMapMem = {}


        