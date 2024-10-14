import elementLib
import stock

import csv


def update(polygons,mems,i,ang1,ang2,mod,mod2,r1,r2,n1,n2,nodeDict,xi,yi):
    if not r1 or not r2:
        print('no')
    nodeDict[str(i)] = [xi,yi]
    polygons[str(i)]['prevAng1'] = ang1
    polygons[str(i)]['prevAng2'] = ang2
    mems[f'{i}-{n1}'] = {
        "r":r1,
        "head":n1,
        "tail":i,
        "mod":mod
    }
    mems[f'{i}-{n2}'] = {
        "r":r2,
        "head":n2,
        "tail":i,
        "mod":mod2
    }
    return nodeDict,polygons,mems
    pass

def getInitial():
    lowerC = ['a','b','c','d','e','f','g','h']
    mems = {}
    libDf = elementLib.loadElement52()
    stock = list(set(libDf['force'].to_list()))
    stockLib = {}
    for i,rows in libDf.iterrows():
        if rows['force'] not in stockLib:
            stockLib[rows['force']] = {
                'area': rows['area'],
                'force': rows['force'],
                'members':[rows['length']],
                'number': rows['number']
            }
        else:
            stockLib[rows['force']]['members'].append(rows['length'])
    loading = [-1,-1,-1]

    reaction = abs(sum(loading))
    print(reaction)
    reactions = [reaction/2,reaction/2]


    start = [0,reaction]
    loadNodes = [start]

    d = loading + reactions
    print(d)
    nodeIssue = 0
    nodeDict = {}
    for i,l in enumerate(loading+reactions):
        if i<len(loading+reactions)-1:
            loadNodes.append([start[0],loadNodes[i][1]+l])
            

    for i,n in enumerate(loadNodes):       
        nodeDict[lowerC[i]]=n
    print(loadNodes)
    print(nodeDict)


    polygons = {
        
        '1':{'type':'bot',
            'neighbors':['a','e'],
            'angles':[[80,60],[360,0]],

            'ang1Crit':[[80,30],False],
            'ang2Crit':[[360,0],False],
            'prevAng1Sign':1,
            'prevAng2Sign':1,
            'prevAng1Loc':0}, #Make the second one the flat one
        
        '2':{'type':'top',
            'neighbors':['1','b'],
            'angles':[[100,70],[225,135]],
            
            'ang1Crit':[[145,90],False],
            'ang2Crit':[[30,0],[185,170]],
            # 'ang2Crit':[[15,0],[180,170]],
            # 'ang2Crit':[[360,0],[360,0]],
            'prevAng1Sign':+1,
            'prevAng2Sign':1,
            'prevAng1Loc':'low'
            },
        
        '3':{'type':'bot',
            'neighbors':['2','e'],
            'angles':[[75,15],[360,0]],
            
            'ang1Crit':[[80,25],False],
            'ang2Crit':[[360,0],False],
            'prevAng1Sign':-1,
            'prevAng2Sign':1,
            'prevAng1Loc':'high'},
        
        # '1':{'type':'end',
        #      'neighbors':['a','d']},
    }
    
    return nodeDict, stock, polygons, loadNodes, mems,stockLib


def getMem():
    memData = {
    1:{'name':'1-e', 'start':1,'end':2,'slope':False},
    2:{'name':'1-a', 'start':1,'end':3,'slope':False},
    3:{'name':'2-1', 'start':2,'end':3,'slope':False},
    4:{'name':'2-b', 'start':3,'end':4,'slope':False},
    5:{'name':'3-2', 'start':2,'end':4,'slope':False},
    6:{'name':'3-e', 'start':2,'end':5,'slope':False},
    7:{'name':'3-4', 'start':4,'end':5,'slope':False, 'r':0.805,'mod':1},
    
    }
    
    memSym = {
        8:{'symMem':5,'nodes':[4,7]},
        9:{'symMem':5,'nodes':[4,6],},
        10:{'symMem':6,'nodes':[5,6],},
        11:{'symMem':3,'nodes':[6,7],},
        12:{'symMem':2,'nodes':[7,8],},
        13:{'symMem':1,'nodes':[6,8]},
    }

  
    return memData,memSym

def getNodeSym():
    
    return  {6:2,7:3,8:1}
    
def getNodeData():
    nodeData = {
            1:{'name':'A-1', 'mems':False, 'loc': [0,0],'found':True},
            2:{'name':'E-1', 'mems':[1], 'loc': [0,0],'found':True},
            3:{'name':'1-2', 'mems':[2,3], 'loc': [],'found':False},
            4:{'name':'1-2', 'mems':[4,5], 'loc': [],'found':False},
            5:{'name':'1-2', 'mems':[6,7], 'loc': [],'found':False},
            
        }
    return nodeData




def writeResults(data,polyNum):
    
    name = f"designResults - {polyNum}.csv"
    # Write the dictionary to CSV
    headers = ['wastedVol','volume','cutOff','utilization','fTimesLengthSum']
    
    with open(name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for k,v in data.items():
            subset_dict = {key: v[key] for key in headers if key in v}
            row = [k]
            # for h in headers[1:]:
            #     row.append(v[h])
            writer.writerow(subset_dict)

    
    print(f'Results are written to {name}')



def getTargetLen():
    return 12

def getLastNode():
    return 8
def getMiddleNode():
    return 5

def getLastPoly():
    return 4