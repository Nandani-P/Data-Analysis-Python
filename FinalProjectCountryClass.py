class Country(object):

    def __init__(self, name=0, year=0, lifeExpe=0, capInc=0, popDensity=0, HDI=0, demoScore=0, aggrRank=0, rankLE=0, rankPCI=0, rankPD=0, rankHDI=0, rankDS=0):
        self.name = name
        self.year = year
        self.lifeExp = lifeExpe
        self.perIncome = capInc
        self.popDensity = popDensity
        self.HDI = HDI
        self.demoScore = demoScore
        self.aggrRank = aggrRank
        
        self.rankLE = rankLE
        self.rankPCI = rankPCI
        self.rankPD = rankPD
        self.rankHDI = rankHDI
        self.rankDS = rankDS
        

    def setIncome(self, capInc):
        self.perIncome = capInc

    def setDensity(self, popDensity):
        self.popDensity = popDensity

    def setHDI(self, HDI):
        self.HDI = HDI

    def setAggrRank(self, rank):
        self.aggrRank = rank + self.aggrRank

    def setDemocracy(self, demoScore):
        self.demoScore = demoScore
