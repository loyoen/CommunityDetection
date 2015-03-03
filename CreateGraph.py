import json
def GetStarDict(filename):
    f = open(filename)
    DictMap = {}
    line = f.readline()
    while line:
        DictMap[int(line)] = -1
        line = f.readline()
    f.close()
    return DictMap

def CreateGraph(StarDict,filename):
    f = open(filename)
    line = f.readline()
    DictMap = {}
    Cnt = 1
    GraphName = "graph.hgr"
    graph = open(GraphName,"w")
    while line:
        try:
            s = json.loads(line)
        except:
            line = f.readline()
            continue
        edgelist = []
        for userid in s['ids']:
            try:
                thisid = StarDict[int(userid)]
            except:
                continue
            if thisid==-1:
                thisid = Cnt
                print Cnt
                DictMap[userid] = thisid
                StarDict[int(userid)] = thisid
                Cnt += 1
            edgelist.append(thisid)
        try:
            curId = StarDict[int(s['id'])]
        except:
            curId = -2
        if curId==-1:
            curId = Cnt
            print Cnt
            DictMap[s['id']] = curId
            StarDict[int(s['id'])] = curId
            Cnt += 1
        if curId>=0:
            edgelist.append(curId)
            
            
        if len(edgelist)>1:
            for node in edgelist:
                graph.write(str(node)+" ")
            graph.write("\n")
        line = f.readline()
        
    f.close()
    graph.close()
    
    idFile = open("ID.json","w")
    jsonstr = json.dumps(DictMap)
    IDMap = idFile.write(jsonstr)
    idFile.close()
    return GraphName    
'''
def mainfunc():
    StarDict = GetStarDict("stars.txt")
    print "startCreate"
    CreateGraph(StarDict,"Osoc-Epinions1.txt")

mainfunc()
'''

