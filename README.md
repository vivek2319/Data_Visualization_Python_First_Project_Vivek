# Data_Visualization_Python_First_Project_Vivek

## Introduction: 
![Iris Dataset](http://jiangtanghu.com/blog/wp-content/uploads/2011/09/iris.gif)

[The Iris flower data set or Fisher's Iris data set](https://www.kaggle.com/uciml/iris) is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper _The use of multiple measurements in taxonomic problems_ as an example of [linear discriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis). 

It is sometimes called Anderson's Iris data set because [Edgar Anderson](https://en.wikipedia.org/wiki/Edgar_Anderson) collected the data to quantify the morphologic variation of Iris flowers of three related species.

Two of the three species were collected in the Gaspé Peninsula *"all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus".*
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the [sepals](https://en.wikipedia.org/wiki/Sepal) and [petals](https://en.wikipedia.org/wiki/Petal), in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.

**Source:** https://en.wikipedia.org/wiki/Iris_flower_data_set

This data sets consists of 3 different types of irises’ ( [Setosa](https://en.wikipedia.org/wiki/Iris_setosa), [Versicolour](https://en.wikipedia.org/wiki/Iris_versicolor), and [Virginica](https://en.wikipedia.org/wiki/Iris_virginica) ) petal and sepal length, stored in a 150x4 numpy.ndarray

                                            Two Dimensional View
![2D View](http://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dataset_002.png)

                                            Three Dimensional View
 
![The rows being the samples and the columns being: Sepal Length, Sepal Width, Petal Length and Petal Width](http://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dataset_001.png).

   **The rows being the samples and the columns being: Sepal Length, Sepal Width, Petal Length and Petal Width**


This is perhaps the best known database to be found in the pattern recognition literature. Fisher's paper is a classic in the field and is referenced frequently to this day. (See Duda & Hart, for example.) The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other. 

## Predicted attribute:

class of iris plant. 

This is an exceedingly simple domain. 
This data differs from the data presented in Fishers article (identified by Steve Chadwick, spchadwick '@' espeedaz.net ). The 35th sample should be: 4.9,3.1,1.5,0.2,"Iris-setosa" where the error is in the fourth feature. The 38th sample: 4.9,3.6,1.4,0.1,"Iris-setosa" where the errors are in the second and third features. 



## Attribute Information:
1. sepal length in cm 
2. sepal width in cm 
3. petal length in cm 
4. petal width in cm 
5. class: 
-- Iris Setosa 
-- Iris Versicolour 
-- Iris Virginica

**Source:** https://archive.ics.uci.edu/ml/datasets/iris



## Kernel used as reference for this project: 
[Ben Hammer](https://www.kaggle.com/benhamner/python-data-visualizations), IRIS Dataset.  

*P.S. Though I have specifically given links to results / graphs after each line of code, all the results / graphs can be found here: https://tinyurl.com/y8usb5m7
