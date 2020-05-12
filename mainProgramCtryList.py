# This is a comment
#
# Author : Nandani Patidar
#
# main program

from RankCountries import *
from Analysis import *
cri = readWriteCSV()
cri.csvReadData()
cri.rankPDFunc()
cri.rankLEFunc()
cri.rankPCIFunc()
cri.rankHDIFunc()
cri.rankGHSFunc()
cri.csvWriteRank()

def getCountriesList(fromRange, toRange):
    listCountries =[]
    cnt = 1
    for country in (sorted(cri.diCountries.values(), key=operator.attrgetter('aggrRank'))):
        if cnt >= fromRange and cnt <= toRange:
            listCountries.append(country.name)
        cnt+= 1
    return listCountries

countryList = getCountriesList(5, 14)

# main program
objVi = visualization()
data = pd.read_csv('data/internet_users.csv', index_col='country', usecols = ["country", '2005', '2006', '2008', '2009','2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'])
yAxislabel = "Internet Users (% of population)"
objVi.linePlotCountryVsYears(yAxislabel, data, countryList)

'''data = pd.read_csv('data/cell_phones_per_100_people.csv', index_col='country', usecols = ['country', '2004', '2005','2006','2007', '2008', '2009','2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'])
plotCountryVsYears("Cell phones per 100 people")

data = pd.read_csv('data/child_mortality_0_5_year_olds_dying_per_1000_born.csv', index_col='country', usecols = ["country", '2010', '2011','2012', '2013','2014','2015', '2016', '2017', '2018', '2019', '2020'])
objVi.plotCountryVsYears("Child Mortality (0-5 years child death per 1000 children)")

data = pd.read_csv('data/population_total.csv', index_col='country', usecols = ['country', '2004', '2005','2006','2007', '2008', '2009','2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
objVi.plotCountryVsYears("Total Population (100 millions)")

data = pd.read_csv('data/population_density_per_square_km.csv', index_col='country', usecols = ['country', '2004', '2005','2006','2007', '2008', '2009','2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
objVi.plotCountryVsYears("Population density per square km)")

data = pd.read_csv('data/energy_production_total.csv', index_col='country', usecols = ['country', '2004', '2005','2006','2007', '2008', '2009'])
objVi.plotCountryVsYears("Energy Production total")

data = pd.read_csv('data/life_expectancy_years.csv', index_col='country', usecols = ['country', '2004', '2005','2006','2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
objVi.plotCountryVsYears("Life Expectancy")

data = pd.read_csv('data/food_supply_kilocalories_per_person_and_day.csv', index_col='country', usecols = ['country', '2004', '2005','2006','2007', '2008', '2009', '2010', '2011', '2012', '2013'])
objVi.plotCountryVsYears("Kilo Calories per person per day")

data = pd.read_csv('data/body_mass_index_bmi_men_kgperm2.csv', index_col='country', usecols = ['country', '1980','2000', '2001', '2002', '2003', '2004', '2005','2006','2007', '2008'])
plotCountryVsYears("Body Mass Index Male (kg/m2)")
data = pd.read_csv('data/body_mass_index_bmi_women_kgperm2.csv', index_col='country', usecols = ['country', '1980', '2000', '2001', '2002', '2003','2004', '2005','2006','2007', '2008'])
objVi.plotCountryVsYears("Body Mass Index Female (kg/m2)")

data = pd.read_csv('data/government_share_of_total_health_spending_percent.csv', index_col='country', usecols = ['country', '1995', '2000', '2001', '2002', '2003','2004', '2005','2006','2007', '2008', '2009', '2010'])
objVi.plotCountryVsYears("Government share of total health spending(%)")'''

data = pd.read_csv('data/income_per_person_gdppercapita_ppp_inflation_adjusted.csv', index_col='country', usecols = ['country', '1995', '2000', '2001', '2002', '2003','2004', '2005','2006','2007', '2008', '2009', '2010','2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
objVi.linePlotCountryVsYears("Income per person", data, countryList)
