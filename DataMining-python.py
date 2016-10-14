import os
import pydotplus

import pandas as pd
import numpy as np
import scipy as sp

from IPython.display import Image

from sklearn.model_selection import train_test_split as tts
from sklearn.externals.six import StringIO
from sklearn.metrics import accuracy_score , precision_score , recall_score , f1_score
from sklearn.tree import export_graphviz
from sklearn import tree

# import data from csv file
df = pd.read_csv('D:\Python\Data\character-deaths.csv')
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

# split data 75% & 25%
attritube_TrainValue , attritube_TestValue , target_TrainValue , target_TestValue = tts(
    attritube_df , df['Death Year'] , test_size = 0.25 , train_size = 0.75
)

# build Decision Tree model
clf = tree.DecisionTreeClassifier(criterion='entropy' , max_depth=5)
clf = clf.fit(attritube_TrainValue , target_TrainValue)

# calculate score accuracy , precision , recall
accuracy = accuracy_score(target_TestValue , clf.predict(attritube_TestValue))
precision = precision_score(target_TestValue , clf.predict(attritube_TestValue))
recall = recall_score(target_TestValue , clf.predict(attritube_TestValue))
f_measure = f1_score(target_TestValue , clf.predict(attritube_TestValue))
print('accuracy: %s' % accuracy)
print('precision: %s' % precision)
print('recall: %s' % recall)
print('f Measure: %s' % f_measure)

# output data to dot file
with open("output/homework1.dot" , 'w') as f :
    f = tree.export_graphviz(clf , out_file=f)

# output data to graph
dot_data = StringIO()
tree.export_graphviz(clf, out_file = dot_data)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("output/homework1.pdf")
