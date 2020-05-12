# This is a comment
#
# Author : Nandani Patidar
#
# main program


from RankCountries import *
from CountryClass import *

cri = readWriteCSV()
cri.csvReadData()
cri.rankAll()
cri.csvWriteRank()

print ("\nBelow are given the criterias and their code. You have to enter the code of your choice of criteria from the given list")
print ("\nLife Expectancy : 1 \nPopulation Density : 2 \nPer Capita Income : 3 \nHuman Development Index : 4 \nDemocracy Score : 5 \nFreedom Index : 6 \nGovernment share of health spending(%) : 7")

print("\nYou can choose any three")
First = int(input("\nEnter a first criteria: " ))
Second = int(input("Enter a second criteria: " ))
Third = int(input("Enter a third criteria: " ))


     
cri.dictMeasureRanking(First, Second, Third)
