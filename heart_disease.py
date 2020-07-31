# -*- coding: utf-8 -*-
"""heart Disease.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13hC4LLWwcKvsy1wQyLN62SZ1-8ha8qfc
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.cm import rainbow
# %matplotlib inline
import warnings
warnings.filterwarnings('ignore')

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

df=pd.read_csv('/content/heart.csv')

df.info()

df.describe()

import seaborn as sns
corrmat=df.corr()
top_corr_features=corrmat.index
plt.figure(figsize=(20,20))
g=sns.heatmap(df[top_corr_features].corr(),annot=True,cmap="RdYlGn")

df.hist()

sns.set_style('whitegrid')
sns.countplot(x='target',data=df,palette='RdBu_r')

dataset=pd.get_dummies(df,columns=['sex','cp','fbs','restecg','exang','slope','cp','thal'])

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
standardScaler = StandardScaler()
columns_to_scale = ['age','trestbps','chol','thalach','oldpeak']
dataset[columns_to_scale]=standardScaler.fit_transform(dataset[columns_to_scale])

dataset.head()

y=dataset['target']
x=dataset.drop(['target'],axis=1)

from sklearn.model_selection import cross_val_score
knn_scores=[]
for k in range(1,21):
      knn_classifier=KNeighborsClassifier(n_neighbors=k)
      score=cross_val_score(knn_classifier,x,y,cv=10)
      knn_scores.append(score.mean())

plt.plot([k for k in range(1,21)],knn_scores,color = 'red')
for i in range(1,21):
       plt.text(i,knn_scores[i-1],(i,knn_scores[i-1]))
       plt.xticks([i for i in range(1,21)])
       plt.ylabel(k)

knn_classifier=KNeighborsClassifier(n_neighbors=12)

score=cross_val_score(knn_classifier,x,y,cv=10)

knn_scores.append(score.mean())

knn_scores

score.mean()

from sklearn.ensemble import RandomForestClassifier

randomforest_classifier=RandomForestClassifier(n_estimators=10)
score=cross_val_score(randomforest_classifier,x,y,cv=10)

score.mean()

