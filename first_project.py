#First we will import important libraries 

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
import pandas as pd
import numpy as np
import seaborn as sns
sns.set(style="white", color_codes=True)

#Load the dataset

iris = pd.read_csv("C:\Desktop\Iris.csv")
# the iris dataset is now available in Pandas DataFrame

#Let's see what is in the Iris Data

iris.head()

![1](https://user-images.githubusercontent.com/21111859/30835290-981a33aa-a225-11e7-9121-49bb5111d538.png)

iris.tail()

#Describe kind of works as summary in R 

iris.describe()

iris.dtypes

# Let's see how many examples we have of each species
iris["Species"].value_counts()


# We'll use this to make a scatterplot of the Iris features.

my_scatter = iris.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm", title= "Scatter plot for sepal length vs width", fontsize=12, colormap=False, figsize=(7,7))

# We will make a bar plot with sepal length and sepal width

temp_bar = iris[['SepalLengthCm', 'SepalWidthCm']]

my_bar = temp_bar.plot(kind="bar", title= "Bar plot for sepal length and width", fontsize=12, figsize=(10,5), width = 2)


my_seaborn = sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=iris, size=6)


# We'll use seaborn's FacetGrid to color the scatterplot by species


My_Col_Seaborn = sns.FacetGrid(iris, hue="Species", size=6) \
      .map(plt.scatter, "SepalLengthCm", "SepalWidthCm") \
      .add_legend()
   

#Add regression and kernel density fits:
My_reg = sns.jointplot("SepalLengthCm", "SepalWidthCm", data=iris, kind="reg")

#We can also achieve same using following line of code
My_reg2 = sns.lmplot("SepalLengthCm", "SepalWidthCm", data=iris)

# We can look at an individual feature in Seaborn through a boxplot

#First we will look at Petal Length 

My_box = sns.boxplot(x="Species", y="PetalLengthCm", data=iris).set_title('My Individual boxplot')

#Now we will look at Sepal Length

My_box2 = sns.boxplot(x="Species", y="SepalLengthCm", data=iris).set_title('My Individual boxplot 2')


# One way we can extend this plot is adding a layer of individual points on top of
# it through Seaborn's striplot

# We'll use jitter=True so that all the points don't fall in single vertical lines
# above the species

# Saving the resulting axes as ax each time causes the resulting plot to be shown
# on top of the previous axes

ax = sns.boxplot(x="Species", y="SepalLengthCm", data=iris).set_title('Before Striplot')

ax1 = sns.stripplot(x="Species", y="SepalLengthCm", data=iris, jitter=True, edgecolor="gray").set_title('After Striplot')

# A violin plot combines the benefits of the previous two plots and simplifies them
# Denser regions of the data are fatter, and sparser thiner in a violin plot

sns.violinplot(x="Species", y="SepalLengthCm", data=iris, size=5).set_title('My Violin Plot')

# A final seaborn plot useful for looking at univariate relations is the kdeplot,
# which creates and visualizes a kernel density estimate of the underlying feature
sns.FacetGrid(iris, hue="Species", size=7) \
   .map(sns.kdeplot, "SepalLengthCm") \
   .add_legend()



# Another useful seaborn plot is the pairplot, which shows the bivariate relation
# between each pair of features
# 
# From the pairplot, we'll see that the Iris-setosa species is separataed from the other
# two across all feature combinations

sns.pairplot(iris.drop("Id", axis=1), hue="Species", size=4)



# Now that we've covered seaborn, let's go back to some of the ones we can make with Pandas
# We can quickly make a boxplot with Pandas on each feature split out by species
iris.drop("Id", axis=1).boxplot(by="Species", figsize=(14, 8))


# One cool more sophisticated technique pandas has available is called Andrews Curves
# Andrews Curves involve using attributes of samples as coefficients for Fourier series
# and then plotting these
from pandas.tools.plotting import andrews_curves
andrews_curves(iris.drop("Id", axis=1), "Species")


# Another multivariate visualization technique pandas has is parallel_coordinates
# Parallel coordinates plots each feature on a separate column & then draws lines
# connecting the features for each data sample
from pandas.tools.plotting import parallel_coordinates
parallel_coordinates(iris.drop("Id", axis=1), "Species")


# A final multivariate visualization technique pandas has is radviz
# Which puts each feature as a point on a 2D plane, and then simulates
# having each sample attached to those points through a spring weighted
# by the relative value for that feature

from pandas.tools.plotting import radviz
radviz(iris.drop("Id", axis=1), "Species")


#Violin plots are great for visualizing distributions. However, we may want to simply display #each point.
#That's where the swarm plot comes in. This visualization will show each point, while "stacking" those with similar values:


type_of_colors=['#78C850',  # Grass 
              '#F08030',  # Fire
              ]

sns.swarmplot(x='SepalWidthCm', y='PetalWidthCm', data=iris, 
              palette=type_of_colors).set_title('My Swarm Plot for Sepal & Petal Width in cm')





#We will try to overlay two plots using seaborn
#Overlaying swarm and violin plots


# Set figure size with matplotlib
plt.figure(figsize=(10,6))
 
# Create plot

sns.violinplot(x='SepalWidthCm',
               y='PetalWidthCm', 
               data=iris, 
               inner=None, # Remove the bars inside the violins
               palette=type_of_colors)

 
sns.swarmplot(x='SepalWidthCm', 
              y='PetalWidthCm', 
              data=iris, 
              color='k', # Make points black
              alpha=0.7) # and slightly transparent

 
# Set title with matplotlib
plt.title('Overlay plot of Violin and Swarm')


#We will try he Bokeh package for visualization 
#First we will try to create a line chart with Bokeh 
#Import library
from bokeh.charts import *

# Output to Line.HTML
output_file("lines.html", title="line plot example with Bokeh")


# create a new line chat with a title and axis labels
p = Bar(iris, title="Line Chart Example", xlabel='SepalLengthCm', ylabel='PetalLengthCm', width=500, height=600)

# show the results

show(p)

#Wrapping up:
#We used rich libraries for visualizations like matplotlib,  mpl_toolkits, sklearn, pandas, numpy, seaborn, Bokeh, etc. We performed basic operations on dataset to have a good look at it. We created Scatterplots, bar charts, joint plot, box plot, strip plot, pair plot, Andrew curves, swarm plots, violin plots, etc. We also used Bokeh package. Hope this helps you in creating good visualization using Python. 
