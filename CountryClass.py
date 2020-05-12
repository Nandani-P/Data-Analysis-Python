# This is a comment
#
# Author : Nandani Patidar
#
# 

# Base class stores only name
class CountryBase:
    def __init__(self, name = 0):
        self.name = name
        
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

# Inheriting countryBase class with some added criteria, measures as attributes    
class Country(CountryBase):
    def __init__(self, name=0, year=0, lifeExpe=0, capInc=0, popDensity=0, HDI=0, demoScore=0, freedIndex=0, govtSpend=0, aggrRank=0, rankLE=0, rankPCI=0, rankPD=0, rankHDI=0, rankDS=0, rankFI=0, rankGHS=0):
        CountryBase.__init__(self, name)
        self.year = year
        self.lifeExp = lifeExpe
        self.perIncome = capInc
        self.popDensity = popDensity
        self.HDI = HDI
        self.demoScore = demoScore
        self.freedIndex = freedIndex
        self.govtSpend = govtSpend
        self.aggrRank = aggrRank
        
        self.rankLE = rankLE
        self.rankPCI = rankPCI
        self.rankPD = rankPD
        self.rankHDI = rankHDI
        self.rankDS = rankDS
        self.rankFI = rankFI
        self.rankGHS = rankGHS
        
    def setIncome(self, capInc):
        self.perIncome = capInc

    def setDensity(self, popDensity):
        self.popDensity = popDensity

    def setHDI(self, HDI):
        self.HDI = HDI

    def setDemocracy(self, demoScore):
        self.demoScore = demoScore
        
    def setFreedomInd(self, freedIndex):
        self.freedIndex = freedIndex

    def setGovtSpend(self, govtSpend):
        self.govtSpend = govtSpend

    def setAggrRank(self, rank):
        self.aggrRank = rank + self.aggrRank

    def setRankLE(self, rankLE):
        self.rankLE = rankLE

    def setRankPCI(self, rankPCI):
        self.rankPCI = rankPCI

    def setRankPD(self, rankPD):
        self.rankPD = rankPD

    def setRankHDI(self, rankHDI):
        self.rankHDI = rankHDI

    def setRankDS(self, rankDS):
        self.rankDS = rankDS

    def setRankFI(self, rankFI):
        self.rankFI = rankFI

    def setRankGHS(self, rankGHS):
        self.rankGHS = rankGHS
    
