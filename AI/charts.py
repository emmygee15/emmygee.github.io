import matplotlib.pyplot as plt
from numpy import random
import seaborn as sns
import pandas as pd

scores = pd.read_csv("pokemon.csv")

def myBoxPlot():
    sns.boxplot(data = scores)
    plt.show()

def myScatterPlot():
    sns.lmplot(x = "Attack", y = "Defense", data = scores, fit_reg = False, hue = "Speed")
    plt.show()

def myLinePlot():
    sns.lineplot(x = "Attack", y = "Defense", data = scores)
    plt.show()

myBoxPlot()
myScatterPlot()
myLinePlot()


#varX = random.randint(100, size =(100))
#varY = random.randint(100, size =(100))

#varX.sort()
#varY.sort()

#plt.plot(varX, varY)
#plt.show()


#HISTOGRAM
#varX = random.normal(170, 10, 250)
#plt.hist(varX)
#plt.show()


#import matplotlib.pyplot as plt
#from numpy import random