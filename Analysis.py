import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np

class visualization():

    def __init__(self):
        
        self.listline = ['b-','g-','r-', 'y-','v-', 'p-','m-','s-','k-', 'c-']
        self.listdash = ['b--','g--','r--', 'y--','v--', 'p--','m--','s--','k--', 'c--']
        self.lowRankCountris = ['Egypt', 'Azerbaijan', 'Sudan', 'Senegal', 'Ghana', 'Morocco', 'Uzbekistan', 'Kenya', 'Tanzania', 'Philippines']
        self.highRankCountries = ['Australia', 'Iceland', 'Norway', 'Canada', 'Sweden', 'New Zealand', 'Finland', 'United States', 'Spain']
        
    def linePlotCountryVsYears(self, yAxislabel, data):
        plt.close()
        count = 0
        xAxis = data.columns
        for i in self.lowRankCountris:
            yAxis = data.loc[i]
            plt.plot(xAxis, yAxis, self.listline[count], label=i)
            count+= 1
        plt.legend(loc='best')
        plt.ylabel(yAxislabel)
        plt.xlabel("Years")
        plt.xticks()        
        plt.savefig('plot.png', dpi=500, bbox_inches=None, orientation='portrait', figsize=(10,6))
        plt.show()

    def 
        
# main program

objVi = visualization()

data = pd.read_csv('C:/Users/nanda/Downloads/internet_users.csv', index_col='country', usecols = ["country", '2005', '2006', '2008', '2009','2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'])
yAxislabel = "Internet Users (% of population)"
objVi.plotCountryVsYears(yAxislabel, data)

'''data = pd.read_csv('C:/Users/nanda/Downloads/cell_phones_per_100_people.csv', index_col='country', usecols = ['country', '2004', '2005','2006','2007', '2008', '2009','2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'])
plotCountryVsYears("Cell phones per 100 people")

data = pd.read_csv('C:/Users/nanda/Downloads/child_mortality_0_5_year_olds_dying_per_1000_born.csv', index_col='country', usecols = ["country", '2010', '2011','2012', '2013','2014','2015', '2016', '2017', '2018', '2019', '2020'])
objVi.plotCountryVsYears("Child Mortality (0-5 years child death per 1000 children)")

data = pd.read_csv('C:/Users/nanda/Downloads/population_total.csv', index_col='country', usecols = ['country', '2004', '2005','2006','2007', '2008', '2009','2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
objVi.plotCountryVsYears("Total Population (100 millions)")

data = pd.read_csv('C:/Users/nanda/Downloads/population_density_per_square_km.csv', index_col='country', usecols = ['country', '2004', '2005','2006','2007', '2008', '2009','2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
objVi.plotCountryVsYears("Population density per square km)")

data = pd.read_csv('C:/Users/nanda/Downloads/energy_production_total.csv', index_col='country', usecols = ['country', '2004', '2005','2006','2007', '2008', '2009'])
objVi.plotCountryVsYears("Energy Production total")

data = pd.read_csv('C:/Users/nanda/Downloads/life_expectancy_years.csv', index_col='country', usecols = ['country', '2004', '2005','2006','2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
objVi.plotCountryVsYears("Life Expectancy")

data = pd.read_csv('C:/Users/nanda/Downloads/food_supply_kilocalories_per_person_and_day.csv', index_col='country', usecols = ['country', '2004', '2005','2006','2007', '2008', '2009', '2010', '2011', '2012', '2013'])
objVi.plotCountryVsYears("Kilo Calories per person per day")

data = pd.read_csv('C:/Users/nanda/Downloads/body_mass_index_bmi_men_kgperm2.csv', index_col='country', usecols = ['country', '1980','2000', '2001', '2002', '2003', '2004', '2005','2006','2007', '2008'])
plotCountryVsYears("Body Mass Index Male (kg/m2)")
data = pd.read_csv('C:/Users/nanda/Downloads/body_mass_index_bmi_women_kgperm2.csv', index_col='country', usecols = ['country', '1980', '2000', '2001', '2002', '2003','2004', '2005','2006','2007', '2008'])
objVi.plotCountryVsYears("Body Mass Index Female (kg/m2)")

data = pd.read_csv('C:/Users/nanda/Downloads/government_share_of_total_health_spending_percent.csv', index_col='country', usecols = ['country', '1995', '2000', '2001', '2002', '2003','2004', '2005','2006','2007', '2008', '2009', '2010'])
objVi.plotCountryVsYears("Government share of total health spending(%)")'''

data = pd.read_csv('C:/Users/nanda/Downloads/income_per_person_gdppercapita_ppp_inflation_adjusted.csv', index_col='country', usecols = ['country', '1995', '2000', '2001', '2002', '2003','2004', '2005','2006','2007', '2008', '2009', '2010','2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
objVi.plotCountryVsYears("Income per person", data)

#plt.scatter(intUserAus, intUserIceland)
#data.T.plot()
#plt.legend(loc='upper left')
#plt.plot(years, intUserAus, 'g--')
#plt.xticks(rotation=90)
'''plt.style.use('ggplot')
data.T.plot(kind='bar')
plt.show()'''
























