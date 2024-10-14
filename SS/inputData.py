import func 
import plotFuncs
import stock
import angleLogic
import elementLib
import data

import random
import matplotlib.pyplot as plt

lowerC = ['a','b','c','d','e','f','g','h']
# stock = stock.getStock()
libDf = elementLib.loadElement52()
stock = list(set(libDf['force'].to_list()))
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
         'ang2Crit':[[75,15],False],
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

top=True

# 1st check type, if type matches flat then we know that node has to be flat


def circleInt():
    # print('circle circle intersection ~~~~~~~~\n')
    pass

def circleLineInt():
    # print('Circle line intersection time------\n')
    pass

def calcAngle():
    pass
    

flat = 'bot'
r1 = 1
r2 = 1
cont = True
#for i in range(1,4):
i = 1
stepBack = False
mems = {}
attempts = 0
while cont:
    p = polygons[str(i)]
    if attempts == 0:
        r2 = stock[random.randint(0,len(stock)-1)]
    r1 = stock[random.randint(0,len(stock)-1)]
    for r2 in stock:
        # print(p)
        # print(nodeDict[p['neighbors'][0]])
        # print(nodeDict[p['neighbors'][1]])
        # print('------------')
        modify = True
        mod = 1
        while modify:
            n1 = p['neighbors'][0]
            n2 = p['neighbors'][1]
            
            if p['type'] == flat:
                ans1,ans2 = func.find_circle_line_intersection(*nodeDict[n1], r1*mod, nodeDict[n2][1], plot=False)
                # ans2 = False

                if ans1:
                    mod2, r2 = func.flat_line_2_force(ans1[0],nodeDict[n2][0],stock)
    
                    if ans2:
                        mod2_2, r2_2 = func.flat_line_2_force(ans2[0],nodeDict[n2][0],stock)

                        if mod2_2>mod2:
                            mod2,r2 = mod2_2, r2_2
                            ans1 = ans2
                            ans2 = False
                            print(ans1)

            elif i == 2:
                [ans1,ans2] = func.circle_intersections(nodeDict[n1][0], nodeDict[n2], r1*mod)
                if ans1:
                    mod2, r2 = func.flat_line_2_force(ans1[1],nodeDict[n1][1],stock)
                    
                    if not mod2 and ans2:
                        mod2_2, r2_2 = func.flat_line_2_force(ans2[1],nodeDict[n1][1],stock)

                        if mod2_2>mod2:
                            mod2,r2 = mod2_2, r2_2
                if ans1:
                    print(ans1)
            else:
                [ans1,ans2] = func.find_intersection(*nodeDict[n1], r1*mod, *nodeDict[n2], r2)
                mod2 = 0
            x1, y1 = nodeDict[p['neighbors'][0]]
            x2, y2 = nodeDict[p['neighbors'][1]] #EXT poly
            
            # print(ans1)
            # print(ans2)
            #CASE 1: Flat top
            #Case 2: Flat bottom
            #Case 3: inside
            once = True
            for a in [ans1,ans2]:
                if a:#p['type'] == flat:
                    intFound,ang1,ang2  = angleLogic.evaluate_sol(a,x1,y1,x2,y2,polygons,i)
                    # xi,yi = a

                    # #determine angles for intersections
                    # angleCrit1 = p['angles'][0]
                    # angleCrit2 = p['angles'][1]
                    # if y1>=yi:
                    #     ang1 = func.calculate_counterclockwise_angle([xi, yi], [x1, y1], plot=False)
                    # else:
                    #     ang1 = func.calculate_counterclockwise_angle([x1, y1], [xi, yi], plot=False)

                    # if y2>=yi:
                    #     ang2 = func.calculate_counterclockwise_angle([xi, yi],[x2, y2], plot=False)
                    # else:
                    #     ang2 = func.calculate_counterclockwise_angle([x2, y2], [xi, yi], plot=False)

                    
                    # # i+=1
                    # circleLineInt()
                    # # foundInt = True
                    # if i>1:
                    #     prevAng1 = polygons[str(i-1)]["prevAng1"]
                    #     prevAng2 = polygons[str(i-1)]["prevAng2"]
                    # else:
                    #     prevAng1 = 0
                    #     prevAng2 = 0

                    # ang1Crit = p['ang1Crit']
                    # ang2Crit = p['ang2Crit']
                    # intFound = angleLogic.anglePass(ang1,ang1Crit,ang2,ang2Crit,p,prevAng1,prevAng2)
                    
                    if intFound:
                        modify = False
                        nodeDict[str(i)] = a
                        stepBack = False

                        
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
                        break
                    else:
                        if once:
                            mod -= 0.01
                            once = False
                            if mod<.5:
                                # if nodeIssue<i:
                                #     nodeIssue = i
                                stepBack = True 
                                modify = False
                                # raise Exception("NOPE") 
                        # circleInt()
                else:
                    if once:
                        mod -= 0.01
                        once = False
                    # mod -= 0.01
                        if mod<.2:
                            # if nodeIssue<i:
                            #     nodeIssue = i
                            stepBack = True 
                            modify = False
                    # raise Exception("NOPE") 
                # circleInt()
        
        attempts += 1
        if stepBack:
            if attempts>500:
                # if i == 3:
                #     plotFuncs.forceDiagram(nodeDict,polygons)
                if nodeIssue<i:
                    nodeIssue = i
                    stepNum = 1
                else:
                    stepNum +=1
                attempts = 0
                i -= stepNum
                if i <1:
                    i = 1
                print('Taking a step back')
        else:
            attempts = 0
            i+=1 
            if i>nodeIssue:
                nodeIssue=0
            print('-------------')
            print(f'I  = {i}\n')
            break
            
        
        # if stepBack:                                                                                                                      :
        #     i-=1
        # else:
        #     i+=1
        
        if i == 4:
            cont = False
            break
print(mems)
print(polygons['1'])
print(polygons['2'])
print(polygons['3'])
print(nodeDict)
plotFuncs.forceDiagram(nodeDict,polygons)
    #REGULAR CIRCLE::
    #> Check if we found an intersection
        #Yes?
            #> Check if we meet angle criteria (check 1st and 2nd if they are in the correct plane)
                #Yes?
                    # > proceed to next node
                #No?
                    #> Try reduction Method x number of times
        #No?
            #> Try reduction Method on bigger circle number of times
            

    # LINE CIRCLE:
        #Get node for line y and see if other node +r can get you there,
            #change circle and check against y intersection
            
            





