# This is a comment
#
# Author : Nandani Patidar
#
# main program

from RankCountries import *
from Analysis import *
cri = readWriteCSV()

cri.csvReadData()
cri.rankAll()
cri.csvWriteRank()

# Function to get custom list of countries (this is sorted list based on aggregate ranking) 
def getCountriesList(fromRange, toRange):
    listCountries =[]
    cnt = 1
    for country in (sorted(cri.diCountries.values(), key=operator.attrgetter('aggrRank'))):
        if cnt >= fromRange and cnt <= toRange:
            listCountries.append(country.name)
        cnt+= 1
    return listCountries

# main program


listfile = [0, 'data/internet_users.csv', 'data/cell_phones_per_100_people.csv', 'data/child_mortality_0_5_year_olds_dying_per_1000_born.csv', 'data/population_total.csv', 'data/population_density_per_square_km.csv','data/energy_production_total.csv', 'data/life_expectancy_years.csv','data/food_supply_kilocalories_per_person_and_day.csv', 'data/body_mass_index_bmi_men_kgperm2.csv', 'data/body_mass_index_bmi_women_kgperm2.csv', 'data/government_share_of_total_health_spending_percent.csv', 'data/income_per_person_gdppercapita_ppp_inflation_adjusted.csv']

yAxislabellist = [0, "Internet Users (% of population)", "Cell phones per 100 people", "Child Mortality (0-5 years child death per 1000 children)", "Total Population (100 millions)", "Population density per square km)", "Energy Production total", "Life Expectancy", "Kilo Calories per person per day", "Body Mass Index Male (kg/m2)", "Body Mass Index Female (kg/m2)", "Government share of total health spending(%)", "Income per person"]
print("\nHere is a list of items you can view the graph: ")
print("\nInternet Users (% of population) : 1 \nCell phones per 100 people : 2  \nChild Mortality (0-5 years child death per 1000 children) : 3 \nTotal Population (100 millions) : 4  \nPopulation density per square km) : 5 \nEnergy Production total : 6 \nLife Expectancy : 7 \nKilo Calories per person per day : 8 \nBody Mass Index Male (kg/m2) : 9 \nBody Mass Index Female (kg/m2) : 10 \nGovernment share of total health spending(%) : 11 \nIncome per person : 12")
i = int(input("\nInput number : "))
print ("\nWe have a list of countries ranked on the basis of eight criterias (Life Expectancy, Population Density, etc.) where 1 being the top rank.\n\nStarting rank can not be more than 180. \nIt will show the graph for only 10 countries from the starting rank.")

fromRange = int(input("\nEnter a starting rank : "))

toRange = fromRange + 9
yAxislabel = yAxislabellist[i]
filename = listfile[i]
countryList = getCountriesList(fromRange, toRange)

objVi = visualization()
objVi.getfileData(filename)
data = objVi.getfileData(filename)
objVi.linePlotCountryVsYears(yAxislabel, data, countryList)

