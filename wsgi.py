from flask import Flask, jsonify 

app=Flask(__name__)

@app.route('/')
def home():
	return jsonify({ 'roll':0 })

@app.route('/welcome')
def ww():
	return jsonify({ 'roll':2 })