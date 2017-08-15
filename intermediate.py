#import matplotlib with subnpackage pyplot
import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np

iris=datasets.load_iris()

#get three numpy arrays for species and two features of sepal of each species
sepal_length = np.array(iris.data[:,0])
sepal_width = np.array(iris.data[:,1])
species = list(iris.target)


#dictionary to map color to species

dict_color = {0:"red",1:"blue",2:"green"}

#generate a list of color strings using the dictionary
color_flower=list()

i = 0
while i < len(species):
    color_flower.append(dict_color.get(species[i])) #how to add entries to list
    i += 1

color_flower=np.array(color_flower)

#scatterplot of sepal length and width with colors for species

plt.scatter(sepal_length,sepal_width,c=color_flower,alpha=.80)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Sepal Length and Width For Three Iris Species')

#summary statistics

print(sepal_length.mean()
print(sepal_length.std())
print(sepal_width.mean())
print(sepal_width.std())
