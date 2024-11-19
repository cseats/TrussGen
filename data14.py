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
    lowerC = ['a','b','c','d','e','f','g','h','i','j']
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
    loading = [-3/7]*7

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
            'neighbors':['a','i'],
            'ang1Crit':[[80,30],False],
            'ang2Crit':[[360,0],False],
            'prevAng1Sign':1,
            'prevAng2Sign':1,
            'prevAng1Loc':0}, #Make the second one the flat one
        
        '2':{'type':'top',
            'neighbors':['1','b'],
            'ang1Crit':[[115,60],False],
            'ang2Crit':[[20,0],[180,160]],
            'prevAng1Sign':+1,
            'prevAng2Sign':1,
            'prevAng1Loc':'low'
            },
        
        '3':{'type':'bot',
            'neighbors':['2','i'],
            'ang1Crit':[[85,45],False],
            'ang2Crit':[[360,0],False],
            'prevAng1Sign':-1,
            'prevAng2Sign':1,
            'prevAng1Loc':'high'},
        
        '4':{'type':'top',
            'neighbors':['3','c'],
            'ang1Crit':[[145,85],False],
            'ang2Crit':[[20,0],[180,160]],
            'prevAng1Sign':+1,
            'prevAng2Sign':1,
            'prevAng1Loc':'low'
            },
        
        '5':{'type':'bot',
            'neighbors':['4','i'],
            'angles':[[75,15],[360,0]],
            
            'ang1Crit':[[85,45],False],
            'ang2Crit':[[360,0],False],
            'prevAng1Sign':-1,
            'prevAng2Sign':1,
            'prevAng1Loc':'high'},
        
        '6':{'type':'top',
            'neighbors':['5','d'],
            'angles':[[100,70],[225,135]],
            
            'ang1Crit':[[145,85],False],
            'ang2Crit':[[20,0],[180,160]],
            'prevAng1Sign':+1,
            'prevAng2Sign':1,
            'prevAng1Loc':'low'
            },
        
        '7':{'type':'bot',
            'neighbors':['6','i'],
            'ang1Crit':[[85,45],False],
            'ang2Crit':[[360,0],False],
            'prevAng1Sign':-1,
            'prevAng2Sign':1,
            'prevAng1Loc':'high'},
        
    }
    
    return nodeDict, stock, polygons, loadNodes, mems,stockLib


def getMem():
    memData = {
    1:{'name':'1-i', 'start':1,'end':2,'slope':False},
    2:{'name':'1-a', 'start':1,'end':3,'slope':False},
    3:{'name':'2-1', 'start':2,'end':3,'slope':False},
    4:{'name':'2-b', 'start':3,'end':4,'slope':False},
    5:{'name':'3-2', 'start':2,'end':4,'slope':False},
    6:{'name':'3-i', 'start':2,'end':5,'slope':False},
    7:{'name':'4-3', 'start':4,'end':5,'slope':False},
    8:{'name':'4-c', 'start':4,'end':6,'slope':False},
    9:{'name':'5-4', 'start':5,'end':6,'slope':False},
    10:{'name':'5-i', 'start':5,'end':7,'slope':False},
    11:{'name':'6-5', 'start':6,'end':7,'slope':False},
    12:{'name':'6-d', 'start':6,'end':8,'slope':False},
    13:{'name':'7-6', 'start':7,'end':8,'slope':False},
    14:{'name':'7-i', 'start':7,'end':9,'slope':False},
    
    
    
    15:{'name':'8-7', 'start':8,'end':9,'slope':False, 'r':0.805,'mod':1},
    
    }
    
    memSym = {
        16:{'symMem':12,'nodes':[8,10]},
        17:{'symMem':13,'nodes':[8,11],},
        18:{'symMem':14,'nodes':[9,11],},
        19:{'symMem':11,'nodes':[10,11],},
        20:{'symMem':8,'nodes':[10,12],},
        21:{'symMem':9,'nodes':[10,13]},
        22:{'symMem':10,'nodes':[11,13]},
        23:{'symMem':7,'nodes':[12,13]},
        24:{'symMem':4,'nodes':[12,14]},
        25:{'symMem':5,'nodes':[12,15]},
        26:{'symMem':6,'nodes':[13,15]},
        27:{'symMem':3,'nodes':[14,15]},
        28:{'symMem':2,'nodes':[14,16]},
        29:{'symMem':1,'nodes':[15,16]},
        
    }

  
    return memData,memSym

def getNodeSym():
    
    return  {10:6,
             11:7,
             12:4,
             13:5,
             14:3,
             15:2,
             16:1}
    
def getNodeData():
    nodeData = {
            1:{'name':'A-1', 'mems':False, 'loc': [0,0],'found':True},
            2:{'name':'E-1', 'mems':[1], 'loc': [0,0],'found':True},
            3:{'name':'1-2', 'mems':[2,3], 'loc': [],'found':False},
            4:{'name':'1-2', 'mems':[4,5], 'loc': [],'found':False},
            5:{'name':'1-2', 'mems':[6,7], 'loc': [],'found':False},
            6:{'name':'1-2', 'mems':[8,9], 'loc': [],'found':False},
            7:{'name':'1-2', 'mems':[10,11], 'loc': [],'found':False},
            8:{'name':'1-2', 'mems':[12,13], 'loc': [],'found':False},
            9:{'name':'1-2', 'mems':[14,15], 'loc': [],'found':False},
            
        }
    return nodeData




def writeResults(data):
    
    name = "designResults.csv"
    # Write the dictionary to CSV
    headers = ['designNumber','wastedVol','volume','cutOff','utilization','fTimesLengthSum']
    
    with open(name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for k,v in data.items():
            subset_dict = {key: v[key] for key in headers if key in v}
            row = [k]
            writer.writerow(subset_dict)

    
    print(f'Results are written to {name}')

def getTargetLen():
    return 12

def getLastNode():
    return 16
def getMiddleNode():
    return 9

def getLastPoly():
    return 8

