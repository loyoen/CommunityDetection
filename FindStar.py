import json
def FindStarReadjson(filename):
    f = open(filename)
    line = f.readline()
    DictMap = {}
    Cnt = 1
    while line:
        try:
            s = json.loads(line)
        except:
            line = f.readline()
            continue
        
        for userid in s['ids']:
            try:
                DictMap[userid] += 1
            except:
                DictMap[userid] = 1
        print Cnt
        Cnt += 1
        line = f.readline()
    f.close()
    StarFilename = "stars.txt"
    outfile = open(StarFilename,"w+")
    StarLinJieNum = Cnt / 400
    for item in DictMap:
        if DictMap[item]>StarLinJieNum:
            outfile.write(str(item)+"\n")
    outfile.close()
    return StarFilename
#FindStarReadjson("Osoc-Epinions1.txt")
