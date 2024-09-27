import elementLib
import stock

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
    loading = [-2,-2,-2]

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
            'angles':[[80,50],[360,0]],

            'ang1Crit':[[75,5],False],
            'ang2Crit':[[360,0],False],
            'prevAng1Sign':1,
            'prevAng2Sign':1,
            'prevAng1Loc':0}, #Make the second one the flat one
        
        '2':{'type':'top',
            'neighbors':['1','b'],
            'angles':[[100,70],[225,135]],
            
            'ang1Crit':[[100,30],False],
            'ang2Crit':[[75,15],[180,135]],
            'prevAng1Sign':+1,
            'prevAng2Sign':1,
            'prevAng1Loc':'low'
            },
        
        '3':{'type':'bot',
            'neighbors':['2','e'],
            'angles':[[75,15],[360,0]],
            
            'ang1Crit':[[120,30],False],
            'ang2Crit':[[360,0],False],
            'prevAng1Sign':-1,
            'prevAng2Sign':1,
            'prevAng1Loc':'high'},
        
        # '1':{'type':'end',
        #      'neighbors':['a','d']},
    }
    
    return nodeDict, stock, polygons, loadNodes, mems,stockLib