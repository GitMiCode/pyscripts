from sklearn.datasets import load_iris
iris = load_iris()
print(list(iris.target_names)) # ['setosa', 'versicolor', 'virginica']

from sklearn import tree
classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(iris.data, iris.target)
#print(classifier.predict([[5.1, 3.5, 1.4, 0.5]]))  #response [0] 'setosa'
#print(classifier.predict([[6.4,3.2,4.5,1.5]]))     #response [1] 'versicolor'
print(classifier.predict([[6.3,3.3,6.0,2.5]]))      #response [2] 'virginica'


#from iris dataset values https://en.wikipedia.org/wiki/Iris_flower_data_set#Data_set use dataset from internal sklearn dataset