# -*- coding: utf-8 -*-
# group 7

#libraries for CAH
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster
import pandas 
import numpy as np
import pickle

# Import data
data = pickle.load(open('data_non_supervised','rb'))

#sample links matrix
data2=data[:,10:]
Z = linkage(data2,method='ward',metric='euclidean')

#Display dendogramme
plt.title("CAH")
dendrogram(Z,orientation='left',color_threshold=0)
plt.show()

#materialization of 5 classes (hauteur h = 50)
plt.title('CAH avec matérialisation des 4 classes')
dendrogram(Z,orientation='left',color_threshold=50)
plt.show()

#cutting to the height h = 50 ==> identification of 5 groups 
groupes_cah = fcluster(Z,t=50,criterion='distance')
print(groupes_cah)

#index of higher groups
idg = np.argsort(groupes_cah)

#print observations and groups
obs_group = pandas.DataFrame(data2[idg],groupes_cah[idg])
print(obs_group)



 