from flask_socketio import SocketIO, send, join_room
from flask import Flask, flash, redirect, render_template, request, session, abort,url_for
import os
import re
import sqlite3
import pandas as pd
import numpy as np
import requests
import MySQLdb
from flask_table import Table, Col
import cv2
import numpy as np
import random
import json
import pickle

import random
import requests
import DTALG as DT
import Predict as PR



mydb = MySQLdb.connect(host='localhost',user='root',passwd='root',db='MedicalDetails')
conn = mydb.cursor()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
studentid=0
data=[]
data1=[]

@app.route('/')
def index():
	session['username']=""
	return render_template('login.html')


@app.route('/DoctorMain')
def DoctorMain():
	if not session.get('logged_in'):
		return render_template("login.html")
	else:
		return render_template('DoctorMain.html',username=session['username'])


@app.route('/PatientMain')
def PatinetMain():
	if not session.get('logged_in'):
		return render_template("login.html",username=session['username'])
	else:
		return render_template('PatientMain.html')
		
		
@app.route('/registerpage',methods=['POST'])
def reg_page():
    return render_template("register.html")
	
@app.route('/loginpage',methods=['POST'])
def log_page():
    return render_template("login.html")
    

    
    

@app.route('/UpdateDoctor')
def UpdateDoctor():
	sql="select * from login where username='"+session['username']+"'"
	print(sql)
	conn.execute(sql)
	results = conn.fetchall()
	print(results[0])
	return render_template("UpdateDoctor.html",results=results[0],username=session['username'])  	

@app.route('/UpdateDoctor1',methods=['POST'])
def UpdateDoctor1():
    	name=request.form['name']
    	username=request.form['uname']
    	password=request.form['password']

    	email=request.form['email']
    	mob=request.form['mob']
    	cmd="update login set name='"+str(name)+"',password='"+str(password)+"',email='"+str(email)+"',mobile='"+str(mob)+"' where username='"+session['username']+"'"
    	print(cmd)
    	conn.execute(cmd)
    	mydb.commit()
    	print("Update Successfully")
    	
    	sql="select * from login where username='"+session['username']+"'"
    	print(sql)
    	conn.execute(sql)
    	results = conn.fetchall()
    	print(results[0])
    	return render_template("UpdateDoctor.html",results=results[0],message="Update SuccesFully")

   
@app.route('/UpdatePatient')
def UpdatePatient():
	sql="select * from login where username='"+session['username']+"'"
	print(sql)
	conn.execute(sql)
	results = conn.fetchall()
	print(results[0])
	return render_template("UpdatePatient.html",results=results[0],username=session['username'])  	

@app.route('/UpdatePatient1',methods=['POST'])
def UpdatePatient1():
    	name=request.form['name']
    	username=request.form['uname']
    	password=request.form['password']

    	email=request.form['email']
    	mob=request.form['mob']
    	cmd="update login set name='"+str(name)+"',password='"+str(password)+"',email='"+str(email)+"',mobile='"+str(mob)+"' where username='"+session['username']+"'"
    	print(cmd)
    	conn.execute(cmd)
    	mydb.commit()
    	print("Update Successfully")
    	
    	sql="select * from login where username='"+session['username']+"'"
    	print(sql)
    	conn.execute(sql)
    	results = conn.fetchall()
    	print(results[0])
    	return render_template("UpdatePatient.html",results=results[0],message="Update SuccesFully")

@app.route('/Training',methods=['POST'])
def train():
	path=request.form['path']
	print("Train Images",path)
	DT.process(path)
	return render_template("Training.html",message="Training SuccesFully Finished")


	
	
    	
    			
    
    
    
@app.route('/register',methods=['POST'])
def reg():
	name=request.form['name']
	username=request.form['username']
	password=request.form['password']
	email=request.form['emailid']
	mobile=request.form['mobile']
	type=request.form['type']
	cmd="SELECT * FROM login WHERE username='"+username+"'"
	print(cmd)
	conn.execute(cmd)
	cursor=conn.fetchall()
	isRecordExist=0
	for row in cursor:
		isRecordExist=1
	if(isRecordExist==1):
	        print("Username Already Exists")
	        return render_template("register.html",message="Username Already Exists")
	else:
		print("insert")
		cmd="INSERT INTO login Values('"+str(name)+"','"+str(username)+"','"+str(password)+"','"+str(email)+"','"+str(mobile)+"','"+str(type)+"')"
		print(cmd)
		print("Inserted Successfully")
		conn.execute(cmd)
		mydb.commit()
		return render_template("register.html",message="Inserted SuccesFully")

@app.route('/login',methods=['POST'])
def log_in():
	#complete login if name is not an empty string or doesnt corss with any names currently used across sessions
	if request.form['username'] != None and request.form['username'] != "" and request.form['password'] != None and request.form['password'] != "":
		username=request.form['username']
		password=request.form['password']
		type=request.form['type']
		cmd="SELECT username,password,type FROM login WHERE username='"+username+"' and password='"+password+"' and type='"+type+"'"
		print(cmd)
		conn.execute(cmd)
		cursor=conn.fetchall()
		isRecordExist=0
		for row in cursor:
			isRecordExist=1
		if(isRecordExist==1):
			session['logged_in'] = True
			# cross check names and see if name exists in current session
			session['username'] = request.form['username']
			if type=="Doctor":
				return render_template("DoctorMain.html",username=session['username'])
			if type=="Patient":
				return render_template("PatientMain.html",username=session['username'])
		else:
			return render_template("login.html",message="Check UserName and Password")

	return redirect(url_for('index'))
	
@app.route("/logout")
def log_out():
    session.clear()
    return redirect(url_for('index'))
    

@app.route("/TrainingPage")
def TrainingPage():
    return render_template("Training.html",username=session['username'])

  
@app.route("/ViewDoctor")
def ViewDoctor():
	sql="select * from login where type='Doctor'"
	conn.execute(sql)
	results = conn.fetchall()
	return render_template("ViewDoctor.html",result=results,username=session['username'])  
	
@app.route("/ViewPatient")
def ViewPatient():
	sql="select * from login where type='Patient'"
	conn.execute(sql)
	results = conn.fetchall()
	return render_template("ViewPatient.html",result=results,username=session['username'])  	


@app.route("/Feedback")
def Feedback():
	sql="select username from login where type='Doctor'"
	print(sql)
	conn.execute(sql)
	doc = conn.fetchall()
	print("doctor",doc)
	sql="select * from feedback where username='"+session['username']+"'"
	print(sql)
	conn.execute(sql)
	results = conn.fetchall()
	print(results)

	return render_template("Feedback.html",doc=doc,result=results,username=session['username'])  	


@app.route("/SubmitFeedback",methods=['POST'])
def SubmitFeedback():
	name=request.form['name']
	uname=request.form['uname']
	feedback=request.form['feedback']
	
	cmd="INSERT INTO feedback Values('"+str(name)+"','"+str(uname)+"','"+str(feedback)+"')"
	print(cmd)
	print("Inserted Successfully")
	conn.execute(cmd)
	mydb.commit()
	
	message="Feedback Inserted Successfully"

	sql="select username from login where type='Doctor'"
	print(sql)
	conn.execute(sql)
	doc = conn.fetchall()
	print("doctors",doc)
	sql="select * from feedback where username='"+session['username']+"'"
	print(sql)
	conn.execute(sql)
	results = conn.fetchall()
	print(results)

	return render_template("Feedback.html",doc=doc,result=results,username=session['username'],message=message)  	

	
@app.route("/ViewFeedback")
def ViewFeedback():
	sql="select * from feedback where doctorusername='"+session['username']+"'"
	conn.execute(sql)
	results = conn.fetchall()
	return render_template("ViewFeedback.html",result=results,username=session['username'])  	
	


@app.route("/Prediction")
def Prediction():
	return render_template("Prediction.html")  	

@app.route('/Prediction1',methods=['POST'])
def Prediction1():
    	age=request.form['age']
    	sex=request.form['sex']
    	chestpain=request.form['chestpain']
    	restbp=request.form['restbp']
    	chol=request.form['chol']
    	fbs=request.form['fbs']
    	restecg=request.form['restecg']
    	maxhr=request.form['maxhr']
    	exang=request.form['exang']
    	oldpeak=request.form['oldpeak']
    	slope=request.form['slope']
    	ca=request.form['ca']
    	thal=request.form['thal']
    	X_test=[age,sex,chestpain,restbp,chol,fbs,restecg,maxhr,exang,oldpeak,slope,ca,thal]
    	res=PR.process("data.csv",X_test)
    	print(res)
    	results=(age,sex,chestpain,restbp,chol,fbs,restecg,maxhr,exang,oldpeak,slope,ca,thal,res)
    	return render_template("Prediction.html",results=results,message="Predicted SuccessFully")  	

    
# /////////socket io config ///////////////
#when message is recieved from the client    
@socketio.on('message')
def handleMessage(msg):
    print("Message recieved: " + msg)
 
# socket-io error handling
@socketio.on_error()        # Handles the default namespace
def error_handler(e):
    pass


  
  
if __name__ == '__main__':
    socketio.run(app,debug=True,host='127.0.0.1', port=4000)
