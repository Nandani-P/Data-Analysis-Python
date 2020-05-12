import matplotlib.pyplot as plt
import pandas as pd


class visualization():

    def __init__(self):
        self.listline = ['b-','g-','r-', 'y-','v-', 'p-','m-','s-','k-', 'c-']
        self.listdash = ['b--','g--','r--', 'y--','v--', 'p--','m--','s--','k--', 'c--' ]       

    def getfileData(self, filename):        
        data = pd.read_csv(filename, index_col='country')
        filedata = data[data.columns[-10:]]
        return filedata
    
    def linePlotCountryVsYears(self, yAxislabel, data, countryList):
        plt.close()
        count = 0
        xAxis = data.columns
        for i in countryList:
            yAxis = data.loc[i]
            plt.plot(xAxis, yAxis, self.listline[count], label=i)
            count+= 1
        plt.legend(loc='best')
        plt.ylabel(yAxislabel)
        plt.xlabel("Years")
        plt.xticks()        
        plt.savefig('plot.png', dpi=500, bbox_inches=None, orientation='portrait', figsize=(10,6))
        plt.show()

    

        


#plt.scatter(intUserAus, intUserIceland)
#data.T.plot()
#plt.legend(loc='upper left')
#plt.plot(years, intUserAus, 'g--')
#plt.xticks(rotation=90)
'''plt.style.use('ggplot')
data.T.plot(kind='bar')
plt.show()'''
























