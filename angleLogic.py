import func


def anglePass(ang1,ang1Crit,ang2,ang2Crit,p,prevAng1,prevAng2,i):
    phi = 10
    intFound = False 
    prevAngle = p['prevAng1Loc']
    sign1 = p['prevAng1Sign']
    sign2 = p['prevAng2Sign']
    if i == 5:
        pass
    if prevAngle == 'low':

        if ang1 <= ang1Crit[0][0] and ang1 >= sign1*phi + prevAng1 and ang1 >= ang1Crit[0][1]:
            if ang1Crit[1]:
                if ang1 <= ang1Crit[1][0] and ang1>= ang1Crit[1][1]:
                    intFound = True
            else:
                intFound = True

        if intFound and ang2 <= ang2Crit[0][0] and ang2>= ang2Crit[0][1]:# or intFound and ang2 <= ang2Crit[1][0] and ang2>= ang2Crit[1][1]:
            intFound = True
            # if ang2Crit[1]:
            #     if ang2 >= ang2Crit[1][0] and ang2 <= ang2Crit[1][1]: #switched
            #         intFound = False
        else:
            intFound = False


    elif prevAngle == 'high':

        # if ang1 <=sign1*phi +prevAng1 and ang1>= ang1Crit[0][1] and ang1 >= sign2*phi +prevAng2:
        if ang1 <=sign1*phi +prevAng1 and ang1>= ang1Crit[0][1] and ang1<= ang1Crit[0][0]:
            if ang1Crit[1]:
                if ang1 <= ang1Crit[1][0] and ang1>= ang1Crit[1][1]:
                    intFound = True
            else:
                intFound = True

        if intFound and ang2 <= ang2Crit[0][0] and ang2>= ang2Crit[0][1]:
            if ang2Crit[1]:
                if ang2 >= ang2Crit[1][0] and ang2 <= ang2Crit[1][1]: #switched
                    intFound = False
        else:
            intFound = False
    else:
        if ang1 <= ang1Crit[0][0] and ang1>= ang1Crit[0][1]:
            if ang1Crit[1]:
                if ang1 <= ang1Crit[1][0] and ang1>= ang1Crit[1][1]:
                    intFound = True
            else:
                intFound = True

        if intFound and ang2 <= ang2Crit[0][0] and ang2>= ang2Crit[0][1]:
            if ang2Crit[1]:
                if ang2 >= ang2Crit[1][0] and ang2 <= ang2Crit[1][1]: #switched
                    intFound = False
        else:
            intFound = False

    return intFound




def evaluate_sol(a,x1,y1,x2,y2,polygons,i):
    xi,yi = a

    #determine angles for intersections
    angleCrit1 = polygons[str(i)]['angles'][0]
    angleCrit2 = polygons[str(i)]['angles'][1]
    if y1>=yi:
        ang1 = func.calculate_counterclockwise_angle([xi, yi], [x1, y1], plot=False)
    else:
        ang1 = func.calculate_counterclockwise_angle([x1, y1], [xi, yi], plot=False)

    if y2>=yi:
        ang2 = func.calculate_counterclockwise_angle([xi, yi],[x2, y2], plot=False)
    else:
        ang2 = func.calculate_counterclockwise_angle([x2, y2], [xi, yi], plot=False)
    
    if i>1:
        prevAng1 = polygons[str(i-1)]["prevAng1"]
        prevAng2 = polygons[str(i-1)]["prevAng2"]
    else:
        prevAng1 = 0
        prevAng2 = 0

    ang1Crit = polygons[str(i)]['ang1Crit']
    ang2Crit = polygons[str(i)]['ang2Crit']
    intFound = anglePass(ang1,ang1Crit,ang2,ang2Crit,polygons[str(i)],prevAng1,prevAng2,i)
    
    return intFound,ang1,ang2