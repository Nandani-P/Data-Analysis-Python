# This is a comment
#
# Data Source : "https://www.gapminder.org/data/"
#
# Author : Nandani Patidar
#
# Read and write data from CSV file. Sorting and ranking countries on different measures.

import math  
import operator
import csv
import pandas as pd
from FinalProjectCountryClass import *


class readWriteCSV():
    def __init__(self):
        self.diCountries = {}
        self.Total = 0
        self.dictC1 = {}

    # read CSV files and create/update country objects and add to the dictionary
    def csvReadData(self):  
        
        LifeExpFile = pd.read_csv("C:/Users/nanda/Downloads/life_expectancy_years.csv")
        countryAgeSeries = LifeExpFile[["country","2020"]]
        for i, j in countryAgeSeries.itertuples(index=False):
            if math.isnan(j)!= True:
                addCountry = Country(i, 2020, j)
                self.diCountries.update({i:addCountry})
            else:
                addCountry = Country(i, 2020, 0)
                self.diCountries.update({i:addCountry})
        
        PerCapFile = pd.read_csv("C:/Users/nanda/Downloads/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        CountryIncSeries = PerCapFile[["country","2020"]]        
        for i, j in CountryIncSeries.itertuples(index=False):            
            if i in self.diCountries:
                existingCountryObj = self.diCountries[i]
                existingCountryObj.setIncome(j)                
            else:
                addCountry = Country(i, 2020, 0, j)
                self.diCountries.update({i:addCountry})        

        popDen = pd.read_csv("C:/Users/nanda/Downloads/population_density_per_square_km.csv")
        CountryPopSeries = popDen[["country","2020"]]
        for i, j in CountryPopSeries.itertuples(index=False):            
            if i in self.diCountries:
                existingCountryObj = self.diCountries[i]
                existingCountryObj.setDensity(j)                
            else:
                addCountry = Country(i, 2020, 0, 0, j)
                self.diCountries.update({i:addCountry})
        

        attrHDI = pd.read_csv("C:/Users/nanda/Downloads/hdi_human_development_index.csv")
        CountryHDISeries = attrHDI[["country","2015"]]
        for i, j in CountryHDISeries.itertuples(index=False):            
            if i in self.diCountries:
                existingCountryObj = self.diCountries[i]
                existingCountryObj.setHDI(j)
            else:
                addCountry = Country(i, 2015, 0, 0, 0, j)
                self.diCountries.update({i:addCountry})
        #print ("sample ", self.diCountries["India"].name, self.diCountries["India"].perIncome, self.diCountries["India"].popDensity, self.diCountries["India"].HDI) 

        attrDemocracy = pd.read_csv("C:/Users/nanda/Downloads/democracy_score_use_as_color.csv")
        CountryDmcrySeries = attrDemocracy[["country","2011"]]       
        for i, j in CountryDmcrySeries.itertuples(index=False):
            
            if i in self.diCountries:
                existingCountryObj = self.diCountries[i]
                existingCountryObj.setDemocracy(j)
            else:
                addCountry = Country(i, 2011, 0, 0, 0, 0, j)
                self.diCountries.update({i:addCountry})
           
        dfDemoScore = pd.DataFrame(data=CountryDmcrySeries)        
        dfDemoScore['rankDS'] = dfDemoScore['2011'].rank(method='min', ascending=False)                
        for index, row in dfDemoScore.iterrows():
            existingCountryObj = self.diCountries[row['country']]         
            if math.isnan(row['rankDS'])!= True:                   
                existingCountryObj.setAggrRank(row['rankDS'])
                existingCountryObj.setRankDS(row['rankDS'])
            else:                
                existingCountryObj.setAggrRank(100)
                existingCountryObj.setRankDS(100)

        attrFI = pd.read_csv("C:/Users/nanda/Downloads/freedix_fh.csv")
        CountryFISeries = attrFI[["country","2018"]]
        for i, j in CountryFISeries.itertuples(index=False):            
            if i in self.diCountries:
                existingCountryObj = self.diCountries[i]
                existingCountryObj.setFreedomInd(j)
            else:
                addCountry = Country(i, 2015, 0, 0, 0, j)
                self.diCountries.update({i:addCountry})

        dfFreedomInd = pd.DataFrame(data=CountryFISeries)        
        dfFreedomInd['rankFI'] = dfFreedomInd['2018'].rank(method='min', ascending=True)                
        for index, row in dfFreedomInd.iterrows():
            existingCountryObj = self.diCountries[row['country']]         
            if math.isnan(row['rankFI'])!= True:                   
                existingCountryObj.setFreedomInd(row['rankFI'])
                existingCountryObj.setRankFI(row['rankFI'])
            else:                
                existingCountryObj.setFreedomInd(100)
                existingCountryObj.setRankFI(100)

        attrGovtHealthSpend = pd.read_csv("C:/Users/nanda/Downloads/government_share_of_total_health_spending_percent.csv")
        CountryGHSSeries = attrGovtHealthSpend[["country","2009"]]       
        for i, j in CountryGHSSeries.itertuples(index=False):           
            if i in self.diCountries:
                existingCountryObj = self.diCountries[i]
                existingCountryObj.setGovtSpend(j)
            else:
                addCountry = Country(i, 2011, 0, 0, 0, 0, j)
                self.diCountries.update({i:addCountry})
                
    # individual functions to create rank of measures             
    def rankLEFunc(self):
        count = 1
        for country in (sorted(self.diCountries.values(), key=operator.attrgetter('lifeExp'), reverse=True)):
            country.setAggrRank(count)
            country.setRankLE(count)
            count += 1

    def rankPCIFunc(self):   
        cnt = 1
        for country in (sorted(self.diCountries.values(), key=operator.attrgetter('perIncome'), reverse=True)):
            country.setAggrRank(cnt)
            country.setRankPCI(cnt)
            cnt += 1
                
    def rankPDFunc(self):
        count = 1    
        for country in (sorted(self.diCountries.values(), key=operator.attrgetter('popDensity'))):           
            country.setAggrRank(count)
            country.setRankPD(count)
            count += 1
            
    def rankHDIFunc(self):
        cnt = 1
        for country in (sorted(self.diCountries.values(), key=operator.attrgetter('HDI'), reverse=True)):
            country.setAggrRank(cnt)
            country.setRankHDI(cnt)
            cnt+= 1

    def rankGHSFunc(self):
        cnt = 1
        for country in (sorted(self.diCountries.values(), key=operator.attrgetter('govtSpend'), reverse=True)):
            country.setAggrRank(cnt)
            country.setRankGHS(cnt)
            cnt+= 1
            
    # Generate aggregate ranking and write all other ranks in CSV file        
    def csvWriteRank(self):
        listRank =[]
        listRankWrap =[]
        c = 1
        with open('rankfile.csv', 'w', newline='', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerows([['Country', 'Overall', 'Aggregate Rank', 'Life Expectancy ranking', 'Population Density Ranking', 'Per Capita Income', 'Human Development Index', 'Democarcy Score', 'Freedom Index', 'Government share of health spending(%)' ]])            
            for country in (sorted(self.diCountries.values(), key=operator.attrgetter('aggrRank'))):
                listRank = [country.name, c,  country.aggrRank, country.rankLE, country.rankPD, country.rankPCI, country.rankHDI, country.rankDS, country.rankFI, country.rankGHS]
                listRankWrap = [listRank]
                writer.writerows(listRankWrap)
                c+=1

    # Aggragate of three criterias given by users
    def dictMeasureRanking(self, measure1, measure2, measure3):
        dictRanking = {}
        for i in self.diCountries:
            total = 0
            countryObject = self.diCountries[i]
            if 'C1' == measure1 or 'C1' == measure2 or 'C1' == measure3:
                total = total + countryObject.rankLE
            if 'C2' == measure1 or 'C2' == measure2 or 'C2' == measure3:
                total = total + countryObject.rankPD
            if 'C3' == measure1 or 'C3' == measure2 or 'C3' == measure3:
                total = total + countryObject.rankPCI
            if 'C4' == measure1 or 'C4' == measure2 or 'C4' == measure3:
                total = total + countryObject.rankHDI
            if 'C5' == measure1 or 'C5' == measure2 or 'C5' == measure3:
                total = total + countryObject.rankDS
            if 'C6' == measure1 or 'C6' == measure2 or 'C6' == measure3:
                total = total + countryObject.rankFI
            if 'C7' == measure1 or 'C7' == measure2 or 'C7' == measure3:
                total = total + countryObject.rankGHS
            dictRanking.update({i: total})
        
        Count = 1
        print("\nTop five Countries: ")
        for j in sorted(dictRanking, key=dictRanking.get):            
            print (Count, j, "\n")
            Count+= 1
            if Count == 6:
                break
        Count = 1
        print("Bottom five Countries: ")
        for j in sorted(dictRanking, key=dictRanking.get, reverse = True):            
            if Count < 6:
                print(Count, j, "\n")
            Count+=1   
            

