#importer les librairies
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

col_names = ['company', 'job', 'degree', 'salary_more_than_100k']
data = pd.read_csv(r"C:\Users\IMAD\Documents\python udemy\ML+Resources\salaries.csv", header=None, names=col_names)

#diviser nos données les variables independante en x et dependante en y
feature_cols =['company', 'job', 'degree']
x = data[feature_cols]
y = data['salary_more_than_100k']

#import label encoder
from sklearn import preprocessing
#label_encoder object knows how to understand word labels
label_encoder = preprocessing.LabelEncoder()
#encode label in column
data['company']=label_encoder.fit_transform(data['company'])
data['job'] = label_encoder.fit_transform(data['job'])
data['degree'] = label_encoder.fit_transform(data['degree'])
print(data.head())

#split the dataset in features and target variable
feature_cols = ['company', 'job', 'degree']
x = data[feature_cols]
y = data['salary_more_than_100k']
#x = data.values[1:, :3]
#y = data.values[1:, 3] # 1:,3 one means we are not using the header
print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)

#Create Decision True classifier object using entropy
clf_entropy = DecisionTreeClassifier(criterion="entropy",max_depth=8)

#train decision tree classifier
clf_entropy = clf_entropy.fit(x_train, y_train)

#predict the response for test dataset
y_pred = clf_entropy.predict(x_test)

print("Accurancy", metrics.accuracy_score(y_test, y_pred))
