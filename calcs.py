


def volume(data,assign,stockLib):
    
    # assign = data['assign']
    wastedVol = 0
    vol = 0
    for k,v in assign.items():
        
        area = stockLib[k]['area']
        wastedVol += area*v['wasteVol']
        vol += area*sum(v['memLen'])
    
    return wastedVol, vol, wastedVol/vol

def utilization(memData):
    
    # memData = data['memberInfo']
    mod = 0
    cnt = 1
    utSum = 0 
    fTimesLengthSum = 0
    for k,v in memData.items():
        fTimesLength = v['mod']*v['r']*v['length']
        ut = v['mod']
        
        fTimesLengthSum += fTimesLength
        utSum += ut
        cnt += 1
        
    return utSum/cnt, fTimesLengthSum


def getMetrics(macroData):
    
    for k,v in macroData.items():
        
        memData = v['memberInfo']
        assignment = v['assignment']
        stockLib = v['stockLib']
        
        wastedVol, vol, cutOff = volume(memData,assignment,stockLib)
        utilz, fTimesLengthSum = utilization(memData)
        
        macroData[k]['wastedVol'] = wastedVol
        macroData[k]['volume'] = vol
        macroData[k]['cutOff'] = cutOff
        macroData[k]['utilization'] = utilz
        macroData[k]['fTimesLengthSum'] = fTimesLengthSum
    
    return macroData