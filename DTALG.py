import numpy as np
import pandas as pd
from pandas import DataFrame,Series
import gaFeatureSelection as ga
from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score

from tkinter import filedialog
from tkinter import*
import time
import datetime
from pandas import read_csv
import matplotlib.pyplot as plt


import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
import csv
import warnings
warnings.filterwarnings("ignore")


def process(path):
	dataset = pd.read_csv(path)
	dataset=DataFrame(dataset)
	dataset.head()[:2]
    
	str_list = [] # empty list to contain columns with strings (words)
    
	for colname, colvalue in dataset.iteritems():
		if type(colvalue[1]) == str:
			str_list.append(colname)
		# Get to the numeric columns by inversion
		num_list = dataset.columns.difference(str_list)
		print(num_list)
		datasetnum = dataset[num_list]
		print(datasetnum)
	#datasetnum.to_csv(path)
	header=ga.gafeature(path)
	print("erere")
	print(header)
	df = pd.read_csv(path, sep=',')
	X = df[header]
	y = df["AHD"]
	print(X)
	print(y)

	X_train, X_test, y_train, y_test = train_test_split(X,y)
	
	model4 = DecisionTreeClassifier()
	model4.fit(X_train, y_train)
	y_pred = model4.predict(X_test)

	mse=mean_squared_error(y_test, y_pred)
	mae=mean_absolute_error(y_test, y_pred)
	r2=r2_score(y_test, y_pred)
	rms = np.sqrt(mean_squared_error(y_test, y_pred))
	ac=accuracy_score(y_test,y_pred.round())


	print("MSE VALUE FOR DecisionTree IS %f "  % mse)
	print("MAE VALUE FOR DecisionTree IS %f "  % mae)
	print("R-SQUARED VALUE FOR DecisionTree IS %f "  % r2)
	print("RMSE VALUE FOR DecisionTree IS %f "  % rms)
	print ("ACCURACY VALUE DecisionTree IS %f" % ac)
	print("------------------------------------------------------------------")	

	result2=open('static/results/DTMetrics.csv', 'w')
	result2.write("Parameter,Value" + "\n")
	result2.write("MSE" + "," +str(mse) + "\n")
	result2.write("MAE" + "," +str(mae) + "\n")
	result2.write("R-SQUARED" + "," +str(r2) + "\n")
	result2.write("RMSE" + "," +str(rms) + "\n")
	result2.write("ACCURACY" + "," +str(ac) + "\n")
	result2.close()
	
	
	df =  pd.read_csv('static/results/DTMetrics.csv')
	acc = df["Value"]
	alc = df["Parameter"]
	colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
	explode = (0.1, 0, 0, 0, 0)  
	
	fig = plt.figure()
	plt.bar(alc, acc,color=colors)
	plt.xlabel('Parameter')
	plt.ylabel('Value')
	plt.title('DecisionTree Metrics Value')
	fig.savefig('static/results/DTMetricsValue.png') 
	#plt.pause(5)
	#plt.show(block=False)
	#plt.close()


