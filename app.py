from flask import Flask, render_template
import os
import sys
from flask import request
from random import randint
import tact_util as t_util

app = Flask(__name__)

@app.route('/')
def home():
    
    city_list = t_util.read_cities()

    result = {
        'apiresult' : 0,    
        'apimessage' : 'OK',    
        
        'details' : city_list        
    }
    
    return render_template('index.html', result = result)

@app.route('/', methods=['POST'])
def result():
    
    city  = request.form.get('city')   
    country  = request.form.get('country')   

    t_util.add_city(city, country)
    
    city_list = t_util.read_cities()

    result = {
        'apiresult' : 0,    
        'apimessage' : 'OK',    

        'details' : city_list        
    }
    
    return render_template('index.html', result = result)

if __name__ == "__main__":
    app.run()
