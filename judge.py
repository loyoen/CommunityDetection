import json
import random 
def GetStarsDict(starfile):
    idFile = open(starfile)
    DictStar = json.loads(idFile.read())
    return DictStar

def ItemCompute(StarsDict,line,percent,partlist,partelems):
    ansMap = {
            "total"     :   0,
            "remove"    :   0,
            "recover"   :   0,
            "recommander" : 0,
            "RandomRecover" : 0
        }
    try:
        s = json.loads(line)
    except:
        return ansMap
    StarsList = []
    for userid in s['ids']:
        if str(userid) in StarsDict:
            StarsList.append(userid)
    if len(StarsList)<30:
        return ansMap
    '''
    mostLen = 10
    if(len(StarsList)*(100-percent)/100<mostLen):
        mostLen = len(StarsList)*(100-percent)/100
    
    randomList = random.sample(range(0,len(StarsList)),mostLen)
    
    leftList = []
    removeList = []
    for i in range(0,len(StarsList)):
        if i in randomList:
            removeList.append(StarsList[i])
        else:
            leftList.append(StarsList[i])
    '''
    leftList = StarsList[:len(StarsList)*percent/100]
    removeList = StarsList[len(StarsList)*percent/100:]
    
    leftPartElem = []
    removePartElem = []
    PartsCntDict = {}
    for item in removeList:
        removePartElem.append(StarsDict[str(item)])   
        
    for item in leftList:
        partid = partlist[StarsDict[str(item)]-1]    
        leftPartElem.append(StarsDict[str(item)])   
        try:
            PartsCntDict[partid] += 1
        except:
            PartsCntDict[partid] = 1
    MaxCnt = 0
    thisPart = -1
    #anotherPart = -1
    for item in PartsCntDict:
        if MaxCnt<PartsCntDict[item]:
            #anotherPart = thisPart
            MaxCnt = PartsCntDict[item]
            thisPart = item
    
    if thisPart == -1:
        return ansMap
    '''
    if anotherPart==-1:
        for item in removeList:
            if StarsDict[str(item)] in partelems[thisPart]:
                ansMap["recover"] += 1
    '''
    
    '''
    for item in removeList:
        if StarsDict[str(item)] in partelems[thisPart]:
            ansMap["recover"] += 1
    '''
    ansMap["recover"] = len(list(set(partelems[thisPart]).intersection(set(removePartElem))))
    ansMap["total"] = len(StarsList)
    ansMap["remove"] = len(removeList)
    
    print "......",len(partelems[thisPart])
    recommanderLen = len(list(set(partelems[thisPart]).difference(set(leftPartElem))))
    ansMap["recommander"] = recommanderLen
    
    iCnt = 0
    while iCnt<recommanderLen:
        guessId = random.randint(1,len(partlist))
        if guessId not in leftPartElem:
            leftPartElem.append(guessId)
            iCnt += 1
    
    ansMap["RandomRecover"] = len(list(set(leftPartElem).intersection(set(removePartElem))))
    
    print "remove:\t",ansMap["remove"],"\trecover:\t",ansMap["recover"],"\trecommand:\t",ansMap["recommander"]
    print "RandomRecover\t",ansMap["RandomRecover"]
    return ansMap

def GetPartInfo(partfilename):
    PartFile = open(partfilename)
    partlist = []
    partelems = {}
    line = PartFile.readline()
    Cnt = 1
    while line:
        partid = int(line)
        partlist.append(partid)
        try:
            partelems[partid].append(Cnt)
        except:
            partelems[partid] = []
            partelems[partid].append(Cnt)
        Cnt += 1
        line = PartFile.readline()
        
    ans = {
            "PartList"  :   partlist,
            "PartElems" :   partelems
        }
    return ans
    
def JudgeFunc(PartFileName,FormatFileName):
    PartsInfo = GetPartInfo(PartFileName)
    DictStar = GetStarsDict("ID.json")
    f = open(FormatFileName)
    line = f.readline()
    totalRemove = 0
    totalRecover = 0
    totalRecommander = 0
    totalRandomRecover = 0
    
    totalCnt = 0
    while line:
        lineAns = ItemCompute(DictStar,line,90,PartsInfo["PartList"],PartsInfo["PartElems"])
        totalRemove += lineAns["remove"]
        totalRecover += lineAns["recover"]
        totalRecommander += lineAns["recommander"]
        totalRandomRecover += lineAns["RandomRecover"]
        line = f.readline()
        totalCnt += 1
        
    print "totalRemove:",totalRemove,"\ttotalRecove:",totalRecover,"\ttotalRecommander:",totalRecommander
    print "totalRandomRecover",totalRandomRecover
    
    print "call rate:",float(totalRecover)/float(totalRemove)
    print "accuration rate:",float(totalRecover)/float(totalRecommander)
    
    print "random call rate:",float(totalRandomRecover)/float(totalRemove)
    print "random accurate:",float(totalRandomRecover)/float(totalRecommander)
    f.close()
