import pandas as pd
import numpy as np 
from matplotlib import pyplot
import seaborn as sns
from pandas.plotting import scatter_matrix

df_white = pd.read_csv('winequality-white.csv', sep=';')
df_red = pd.read_csv('winequality-red.csv' , sep=';')

