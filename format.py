import json
def FormatDeal(filename):
    fi = open(filename)
    line = fi.readline()
    DictMap = {}
    while line:
        if line[0] == "#":
            line = fi.readline()
            continue
        elems = line.split("\t")
        print elems[0]

        try:
            DictMap[elems[0]].append(elems[1].replace("\n",""))
        except:
            DictMap[elems[0]] = []
            DictMap[elems[0]].append(elems[1].replace("\n",""))
        line = fi.readline()
    fi.close()
    FormatFileName = "O"+filename
    fo = open(FormatFileName,"w")
    for item in DictMap:
        DictTmp = {}
        DictTmp["id"] = item
        DictTmp["ids"] = DictMap[item]
        jsonline = json.dumps(DictTmp)
        fo.write(jsonline)
        fo.write("\n")
    fo.close()
    return FormatFileName
