# This is a comment
#
# Author : Nandani Patidar
#
# main program


from RankCountries import *
from FinalProjectCountryClass import *

print ("\nBelow are given the criterias and their code. You have to enter the code of your choice of criteria from the given list")
print ("\nLife Expectancy : C1 \nPopulation Density : C2 \nPer Capita Income : C3 \nHuman Development Index : C4 \nDemocracy Score : C5 \nFreedom Index : C6")

print("\nYou can choose any three")
First = input("\nEnter the code for 1st criteria: " )
Second = input("Enter the code for 2nd criteria: " )
Third = input("Enter the code for 3rd criteria: " )


cri = readWriteCSV()
cri.csvReadData()
cri.rankPDFunc()
cri.rankLEFunc()
cri.rankPCIFunc()
cri.rankHDIFunc()
cri.csvWriteRank()
     
cri.dictMeasureRanking(First, Second, Third)
