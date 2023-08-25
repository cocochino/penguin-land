'''
Created on Aug 25, 2023

@author: Miho
Using flask to make an api
ref https://www.geeksforgeeks.org/python-build-a-rest-api-using-flask/
'''

# import necessary libraries and functions
from flask import Flask, jsonify, request
  
# creating a Flask app
app = Flask(__name__)
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
  
        data = "Welcome to Penguin Land"
        return jsonify({'data': data})
  
  
# A simple function to double a number
# the number to be doubled is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000/baby/7
# this returns 14 (7 * 2 = 14)
@app.route('/baby/<int:num>', methods = ['GET'])
def baby(num):
  
    return jsonify({'data': f"You got {num*2} baby penguins!"})
    
  
# This function will return response code 201
# on the terminal type: curl http://127.0.0.1:5000/babt/7
@app.route('/colony/<string:col>', methods = ['POST'])
def colony(col):
  
    return jsonify({'colony': f"You built Colony {col}"}), 201
  
# driver function
if __name__ == '__main__':
 
    app.run(debug = True)
    
