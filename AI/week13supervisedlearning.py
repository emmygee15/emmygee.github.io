import numpy    
import seaborn    
import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import svm
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


#1. load dataset    
iris=pd.read_csv('Iris.csv') 

#2. dataset spliting    
array = iris.values  
X = array[:, :2]  # we only take the first two features else you exhaust max iterations.
Y = array[:,4]    
validation_size = 0.20    
seed = 7    
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=validation_size,     
random_state=seed)    
num_folds = 10    
num_instances = len(X_train)    
seed = 7    
scoring = 'accuracy'

#3.Train models    
models = []    
models.append(('LR', LogisticRegression()))    
models.append(('CART', DecisionTreeClassifier()))    
models.append(('NB', GaussianNB()))   
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('SVM', svm.SVC()))    

#4. Evaluate model to determine better algorithm    
print("Evaluate model to determine best algorithm\n----------------------------  ")    
results = []    
names = []    
for name, model in models:    
    kfold = KFold(n_splits = num_folds, shuffle=True)    
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)    
    results.append(cv_results)    
    names.append(name)    
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())    
    print(msg)   

#5. pretiction using best model   
svn = svm.SVC()    
svn.fit(X_train, Y_train)    
predictions = svn.predict(X_validation)    
print("\nSVM accuracy score\n----------------------------")

print(accuracy_score(Y_validation, predictions))    
print("\nSVM confusion matrix\n----------------------------")
print(confusion_matrix(Y_validation, predictions))    
print("\nSVM classification report\n----------------------------")
print(classification_report(Y_validation, predictions))

#display the decision tree
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

from sklearn.tree import DecisionTreeClassifier, plot_tree

#3 train the model
tree_viz = DecisionTreeClassifier().fit(X, Y)

plt.figure(figsize = (20,10))

plot_tree(tree_viz, filled=True      )
# Display the tree plot figure.
plt.show()
