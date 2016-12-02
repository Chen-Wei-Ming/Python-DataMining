import os

import pandas as pd
import numpy as np
import scipy as sp

from IPython.display import Image

from sklearn.model_selection import train_test_split as tts
from sklearn.externals.six import StringIO
from sklearn.metrics import accuracy_score , precision_score , recall_score , f1_score
from sklearn.tree import export_graphviz
from sklearn.datasets import dump_svmlight_file
from sklearn import tree

# import data from csv file
df = pd.read_csv('data/character-deaths.csv')
# transform NaN to 0
df = df.fillna(0)
# delete colums
del df['Book of Death'] , df['Name'] , df['Death Chapter']

# setting data value
df['Death Year'] = df['Death Year'].apply(lambda death : 1 if death > 0 else 0)
# df['Allegiances'] = df['Allegiances'].apply(lambda allegiances : 1 if allegiances == "")
# setting end

# settting colums
attritube_colums = ['Allegiances' , 'Book Intro Chapter' , 'Gender' , 'Nobility' , 'GoT' , 'CoK' , 'SoS' , 'FfC' , 'DwD']
# use setting colums to limit df colums
attritube_df = df[list(attritube_colums)]
attritube_df = pd.get_dummies(attritube_df)
print(attritube_df)

dump_svmlight_file(attritube_df,df['Death Year'],"output/deaths_svm_will.txt",zero_based=True,multilabel=False)
