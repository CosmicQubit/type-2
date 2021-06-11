#Machine learning model
#Imported Modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, KFold

def fitting():
    #The dataset
    df = pd.read_csv("diabetes.csv") # df=dataframe; a pandas object
    X = df[["Age", "BMI", "Glucose", "BloodPressure"]].values #Getting values of all the features into a seperate pandas dataframe
    y = df["Target"].values #Getting values of all the targets and converting them into a numpy array

    #K-fold
    scores = []#Stores the models' accuracy scores
    kf = KFold(n_splits=5, shuffle=True)#creating the K-fold
    for train_data, test_data in kf.split(X):#function to split then test the K amount of models made
        X_train, X_test = X[train_data], X[test_data]
        y_train, y_test = y[train_data], y[test_data]
        model = LogisticRegression()#creates an instance of a model
        model.fit(X_train, y_train)#fits the 4 (K-1) training datasets
        scores.append(model.score(X_test, y_test))#tests the current model using the testing dataset

    #The model: building
    fitting.final_model = LogisticRegression()#creates an instance of the final model
    fitting.final_model.fit(X, y) #trains the model using the whole dataset

def prediction():
    #The model: prediction
    y_pred = fitting.final_model.predict_proba(userData)[:,1] #makes probability predictions using the final model
    return round(float(y_pred*100), 1)
