from pymongo import MongoClient
from flask import Flask, render_template, request, redirect
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient()
db = client.ab2019

import random

def get_messages():
	return db.messages.find()
	
@app.route('/', methods=["GET", "POST"])
def home():
	if request.method == "POST":
		sender = request.form['sender']
		body = request.form['body']
		db.messages.insert({
			"sender": sender,
			"body": body
		})	
	return render_template('home.html', messages=get_messages())

@app.route("/submit")
def submit():
	return render_template('submit.html')	

@app.route("/edit/<document_id>", methods=["GET", "POST"])
def edit(document_id):
	if request.method == "POST":
		sender = request.form['sender']
		body = request.form['body']
		db.messages = update_one({
		
