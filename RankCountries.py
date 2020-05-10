#
#
#
#
#
import math  
import operator 
import pandas as pd
from FinalProjectCountryClass import Country
   
class readCriteria():
    def __init__(self):
        self.diCountries = {}
        
        
        
    
    def criteria(self):
        LifeExpFile = pd.read_csv("C:/Users/nanda/Downloads/life_expectancy_years.csv")
        countryAgeSeries = LifeExpFile[["country","2020"]]
        for i, j in countryAgeSeries.itertuples(index=False):
            addCountry = Country(i, 2020, j)
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
        #print ("sample ", diCountries["India"].name, diCountries["India"].perIncome, diCountries["India"].popDensity, diCountries["India"].HDI) 

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
                existingCountryObj.rankDS = row['rankDS']
            else:                
                existingCountryObj.setAggrRank(100)
                existingCountryObj.rankDS = 100
            #print(existingCountryObj.rankDS, row['country'])'''


    def rankPDFunc(self):
        cnt = 1     
        for country in (sorted(self.diCountries.values(), key=operator.attrgetter('popDensity'))):           
            country.setAggrRank(cnt)
            country.rankPD = cnt
            cnt+= 1
            
    def rankPDFunc(self):
        cnt = 195
        for country in (sorted(diCountries.values(), key=operator.attrgetter('lifeExp'))):
            country.setAggrRank(cnt)
            country.rankLE = cnt
            cnt-= 1

       
            cnt = 195
            for country in (sorted(diCountries.values(), key=operator.attrgetter('perIncome'))):
                country.setAggrRank(cnt)
                country.rankPCI = cnt
                cnt-= 1
                

            cnt = 195
            for country in (sorted(diCountries.values(), key=operator.attrgetter('HDI'))):
                country.setAggrRank(cnt)
                country.rankHDI = cnt
                cnt-= 1'''
                    
        
        import csv
        listRank =[]
        listRank1 =[]
        c = 1
        with open('rankfile.csv', 'w', newline='', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerows([['Country', 'Overall', 'Aggregate Rank', 'Life Expectancy ranking', 'Population Density Ranking', 'Per Capita Income', 'Human Development Index', 'Democarcy Score' ]])            
            for country in (sorted(self.diCountries.values(), key=operator.attrgetter('aggrRank'))):
                listRank = [country.name, c,  country.aggrRank, country.rankLE, country.rankPD, country.rankPCI, country.rankHDI, country.rankDS]
                listRank1 = [listRank]
                writer.writerows(listRank1)
                c+=1

cri = readCriteria()
cri.criteria()
cri.rankPDFunc()
