import judge,FindStar,format,CreateGraph
import os
def mainfunc(filename):
    FormatFileName = format.FormatDeal(filename)
    StarFilename = FindStar.FindStarReadjson(FormatFileName)
    StarDict = CreateGraph.GetStarDict(StarFilename)
    print "startCreate"
    GraphName = CreateGraph.CreateGraph(StarDict,FormatFileName)
    PartNum = len(StarDict)/20
    UbFactor = 10
    CmdLine = ".\hmetis-1.5.3-WIN32\hmetis-1.5.3-WIN32\hmetis.exe %s %d %d 10 1 1 1 0 0" %(GraphName,PartNum,UbFactor)
    print CmdLine
    os.system(CmdLine)
    PartFileName = GraphName + ".part." + str(PartNum)
    print PartFileName
    judge.JudgeFunc(PartFileName,FormatFileName)
mainfunc("soc-Epinions1.txt")
