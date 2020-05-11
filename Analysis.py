import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np


def plotCountryVsYears(yAxislabel):
    plt.close('all')
    count = 0
    topCountries = ['Australia', 'Iceland', 'Norway', 'Canada', 'Sweden', 'New Zealand', 'Finland', 'United States', 'Spain']
    listColor = ['b-','g-','r-', 'y-','v-', 'p-','m','s-','k-', 'c-']
    xAxis = data.columns
    for i in topCountries:
        yAxis = data.loc[i]
        plt.plot(xAxis, yAxis, listColor[count], label=i)
        count+= 1
    plt.legend(loc='best')
    plt.ylabel(yAxislabel)
    plt.xlabel("Years")
    plt.xticks(rotation=90)
    plt.show()
    
data = pd.read_csv('C:/Users/nanda/Downloads/internet_users.csv', index_col='country', usecols = ["country", '2015', '2016', '2017'])
yAxislabel = "Internet Users (% of population)"
plotCountryVsYears(yAxislabel)

data = pd.read_csv('C:/Users/nanda/Downloads/child_mortality_0_5_year_olds_dying_per_1000_born.csv', index_col='country', usecols = ["country", '2012', '2013','2014','2015', '2016', '2017', '2018', '2019', '2020'])
plotCountryVsYears("Child Mortality (0-5 years child death per 1000 children)")




#plt.scatter(intUserAus, intUserIceland)
#data.T.plot()
#plt.legend(loc='upper left')
#plt.plot(years, intUserAus, 'g--')

'''plt.style.use('ggplot')
data.T.plot(kind='bar')
plt.show()'''
























