from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

iris=pd.read_csv('Iris.csv') 
array = iris.values  

x1 = array[:,0]#'SepalLength'
x2 = array[:,3]#'PetalWidth'

# create new plot and data
X = np.array(list(zip(x1, x2)))
colors = ['b', 'g', 'r']  # colors
markers = ['o', 'v', 's'] # shapes
plt.ylabel('Length')

kmeans = KMeans(n_clusters=3).fit(X)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 200, 
            c = 'yellow', label = 'Centroids')

for i, l in enumerate(kmeans.labels_):
    plt.plot(x1[i], x2[i], color=colors[l], marker=markers[l])
plt.xlabel('Width')
plt.legend()
plt.show()
