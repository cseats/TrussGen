import data
import angleLogic
import func
import plotFuncs
import drawTruss
import stockAssignment

import random

nodeDict, stock, polygons, loadNodes, mems, stockLib = data.getInitial()

def create(nodeDict, stock, polygons, loadNodes, mems, stockLib):

    cont = True
    iterationsTotal = 0
    iterationsLocal = 0
    nodeIssue = 0
    stepBack = True
    stepNum = 0
    i=1
    flat = 'bot'
    while cont: #outer loop counting polygons
        
        p = polygons[str(i)]
        n1 = p['neighbors'][0]
        n2 = p['neighbors'][1]
        r1 = stock[random.randint(0,len(stock)-1)]
        stepForward = False
        proceed = False
        for r2 in stock:
            if not stepForward:
                modify = True
                mod = 1
                while modify:
                    
                    
                    if p['type'] == flat:
                        ans1,ans2 = func.find_circle_line_intersection(*nodeDict[n1], r1*mod, nodeDict[n2][1], plot=False)
                        # ans2 = False

                        if ans1:
                            mod2, r2 = func.flat_line_2_force(ans1[0],nodeDict[n2][0],stock)
            
                            if ans2:
                                mod2_2, r2_2 = func.flat_line_2_force(ans2[0],nodeDict[n2][0],stock)

                                if mod2_2>mod2 and mod2_2 and r2_2:
                                    mod2,r2 = mod2_2, r2_2
                                    ans1 = ans2
                                    ans2 = False
                                    print(ans1)

                    elif i == 2:
                        [ans1,ans2] = func.circle_intersections(nodeDict[n1][0], nodeDict[n2], r1*mod)
                        if ans1:
                            mod2, r2 = func.flat_line_2_force(ans1[1],nodeDict[n1][1],stock)
                            
                            if  mod2 and ans2:
                                mod2_2, r2_2 = func.flat_line_2_force(ans2[1],nodeDict[n1][1],stock)

                                if mod2_2>mod2:
                                    mod2,r2 = mod2_2, r2_2
                        # if ans1:
                        #     print(ans1)
                    else:
                        [ans1,ans2] = func.find_intersection(*nodeDict[n1], r1*mod, *nodeDict[n2], r2)
                        mod2 = 0
                    x1, y1 = nodeDict[p['neighbors'][0]]
                    x2, y2 = nodeDict[p['neighbors'][1]] #EXT poly
                    
                    once = True
                    for a in [ans1]:
                        if a:#p['type'] == flat:
                            intFound,ang1,ang2  = angleLogic.evaluate_sol(a,x1,y1,x2,y2,polygons,i)

                        else:
                            intFound = False

                    if intFound and r1 and r2:
                        nodeDict,polygons,mems = data.update(polygons,mems,i,ang1,ang2,mod,mod2,r1,r2,n1,n2,nodeDict,a[0],a[1])
                        modify = False
                        proceed = True
                        iterationsLocal = 0
                        stepForward = True
                        break
                    else: 
                        mod -= 0.01
                        
                        if mod<0.5:
                            modify = False
            else:
                break
        iterationsLocal +=1
        if proceed:
            i += 1
            iterationsLocal = 0
            # print(f'This is i: {i}\n')
            
            
            
            if i > nodeIssue and nodeIssue!=0:
                nodeIssue = 0
                stepNum = 0
            
        else:  
            if iterationsLocal > 20:
                if nodeIssue == 0:
                    nodeIssue = i
                stepBack = True
                
                if nodeIssue<i and nodeIssue>0:
                    nodeIssue = i
                    stepNum = 1
                else:
                    stepNum+=1
                
                i -= stepNum
                iterationsLocal = 0
                if i<1:
                    i = 1
                    stepNum = 0
        
        
        
        
        if iterationsTotal >100 or i == 4:
            cont = False


    nodeData, memData = drawTruss.forcediagram2Truss(polygons,mems,nodeDict)
    # print(mems)
    # print(polygons['1'])
    # print(polygons['2'])
    # print(polygons['3'])
    # print(nodeDict)
    return memData,nodeData, stockLib
    assign = stockAssignment.assignPrep(memData,stockLib)
    print(assign)
    # plotFuncs.forceDiagram(nodeDict,polygons)