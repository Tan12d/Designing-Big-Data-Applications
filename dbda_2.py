# -*- coding: utf-8 -*-
"""DBDA_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RSWqcs26pzlIUQ1maO0wLZMew3mPtqPz
"""

from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset

iris = load_iris()

# Create a DataFrame to better visualize the dataset

iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Display basic information about the dataset

print("Number of Features:", iris_df.shape[1])
print("Number of Samples:", iris_df.shape[0])
print("\nAttribute Names (Features):")
print(iris_df.columns.tolist())
print("\nClasses (Target Names):")
print(iris.target_names)





# print(iris_df)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, ttest_ind
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.datasets import load_iris

# Load Iris dataset

iris = load_iris()
iris_data = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['species'])

# Question 1: Descriptive Statistics

mean_sepal_length = iris_data['sepal length (cm)'].mean()
median_sepal_length = iris_data['sepal length (cm)'].median()
std_sepal_length = iris_data['sepal length (cm)'].std()

print(f'Mean = {mean_sepal_length}')
print(f'Median = {median_sepal_length}')
print(f'Std = {std_sepal_length}')

# Question 2: Data Visualization

plt.figure(figsize=(10, 6))

for species in iris_data['species'].unique():
  species_data = iris_data[iris_data['species'] == species]
  plt.boxplot(species_data['petal width (cm)'], positions=[species], labels=[f'Species {int(species)}'])

plt.title('Box Plot- Petal Width Distribution for Each Species')
plt.xlabel('Species')
plt.ylabel('Petal Width (cm)')
plt.show()

# Question 3: Correlation Analysis

pearson_corr, _ = pearsonr(iris_data['sepal length (cm)'], iris_data['petal length (cm)'])

print(pearson_corr)
print(_)

# Question 4: Data Preprocessing

scaler = MinMaxScaler()

iris_data['sepal width (normalized)'] = scaler.fit_transform(iris_data[['sepal width (cm)']])

print(iris_data)

# Question 5: Hypothesis Testing

setosa_sepal_length = iris_data[iris_data['species'] == 0]['sepal length (cm)']
versicolor_sepal_length = iris_data[iris_data['species'] == 1]['sepal length (cm)']

t_stat, p_value =  ttest_ind(setosa_sepal_length, versicolor_sepal_length)

print(setosa_sepal_length)
print(versicolor_sepal_length)

print(t_stat)
print(p_value)

# Question 6: Decision Trees

X_train, X_test, y_train, y_test = train_test_split(iris_data.drop('species', axis=1), iris_data['species'], test_size=0.2, random_state=42)
dt_classifier = DecisionTreeClassifier(criterion='gini')
dt_classifier.fit(X_train, y_train)
dt_accuracy = accuracy_score(y_test, dt_classifier.predict(X_test))

print(X_train)
print(X_test)
print(y_train)
print(y_test)

print(dt_classifier)

print(dt_accuracy)

# Question 7: Support Vector Machines (SVM)

svm_classifier = SVC(kernel='rbf')
svm_classifier.fit(X_train, y_train)
svm_accuracy = accuracy_score(y_test, svm_classifier.predict(X_test))

print(svm_classifier)
print(svm_accuracy)

# Question 8: K-Means Clustering

kmeans = KMeans(n_clusters=3)
iris_data['cluster'] = kmeans.fit_predict(iris_data[['sepal length (cm)', 'sepal width (cm)']])
plt.scatter(iris_data['sepal length (cm)'], iris_data['sepal width (cm)'], c=iris_data['cluster'], cmap='viridis')
plt.title('K-Means Clustering- Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()

# Question 9: Principal Component Analysis (PCA)

pca = PCA()
iris_pca = pca.fit_transform(iris_data.drop(['species', 'cluster'], axis=1))
explained_variance_ratio = pca.explained_variance_ratio_
eigen_vectors = pca.components_

print(iris_pca)
print(explained_variance_ratio)
print(eigen_vectors)

# Question 10: Model Evaluation

logreg_classifier = LogisticRegression()
knn_classifier = KNeighborsClassifier()
logreg_classifier.fit(X_train, y_train)
knn_classifier.fit(X_train, y_train)
logreg_accuracy  = accuracy_score(y_test, logreg_classifier.predict(X_test))
knn_accuracy = accuracy_score(y_test, knn_classifier.predict(X_test))

print(f'Mean Sepal Length: {mean_sepal_length}')
print(f'Median Sepal Length: {median_sepal_length}')
print(f'Standard Deviation Sepal Length: {std_sepal_length}')
print(f'Pearson Correlation Coefficient: {pearson_corr}')
print(f'Petal Width Min-Max Scaled Values:\n{iris_data["sepal width (normalized)"]}')
print(f'T-Test p-value: {p_value}')
print(f'Decision Tree Accuracy: {dt_accuracy}')
print(f'SVM Classifier Accuracy: {svm_accuracy}')
print(f'Principal Components Explained Variance Ratio: {explained_variance_ratio}')
print(f'Eigen Vectors:\n{eigen_vectors}')
print(f'Logistic Regression Accuracy: {logreg_accuracy}')
print(f'KNN Classifier Accuracy: {knn_accuracy}')

# print(iris_data)