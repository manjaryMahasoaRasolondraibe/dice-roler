from flask import Flask, jsonify 
import random

app=Flask(__name__)

@app.route('/')
def home():
	return jsonify({ 'roll':random.randint(1,6) })