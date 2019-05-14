# Wine Quality - Project

  

## Target
Create a model to predict the quality of the wine based on some chemical parameters 
Find the best classification algorithm between:

- Support Vector Machine

- Random Forest Tree

- K-nearest Neighbor

## Dataset
We have 2 different datasets, one fore the white wine and one for the red ones.
The datasets are available on Kaggle (at: [Wine quality - Dataset](https://archive.ics.uci.edu/ml/datasets/wine+quality)).

### Desctription

The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine. For more details, consult: [Web Link](http://www.vinhoverde.pt/en/homepage) or the reference [Cortez et al., 2009]. Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).  

These datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are munch more normal wines than excellent or poor ones). Outlier detection algorithms could be used to detect the few excellent or poor wines. Also, we are not sure if all input variables are relevant. So it could be interesting to test feature selection methods.

  

## Attribute information

**The Dataset is composed of 11 features**:

For more information, read [Cortez et al., 2009].  
Input variables (based on physicochemical tests):  
1 - fixed acidity  
2 - volatile acidity  
3 - citric acid  
4 - residual sugar  
5 - chlorides  
6 - free sulfur dioxide  
7 - total sulfur dioxide  
8 - density  
9 - pH  
10 - sulphates  
11 - alcohol  
Output variable (based on sensory data):  

**And 6 Classes (value associated between brackets)**:

12 - quality (score between 0 and 10)


As shown, the number of classes is high and is not good for classification problem. The quality parameter will be mapped in a subset of 3 values:
- 0, 1, 2, 3, 4  mapped with 1
- 5, 6 mapped with 2 
- 7, 8, 9 mapped with 3

The comparison of these **three or four** algorithm helps to detect which ones is the best on this kind of problems