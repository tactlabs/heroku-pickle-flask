#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: raja

Source:
    
'''

# Import necessary modules
import pickle

file_Name = "city"

def get_name_details(name):    
    return "Your name has " + str(len(name)) + " characters"

def store_city():
    city1 = {
                'name':'Chennai', 
                'country': 'India'
            } 
    city_list = []
    city_list.append(city1)

    city2 = {
                'name':'Toronto', 
                'country': 'Canada'
            } 
    city_list.append(city2)

    fileObject = open(file_Name,'wb') 

    pickle.dump(city_list, fileObject)     

def read_cities():

    fileObject = open(file_Name,'rb')  

    #print(type(fileObject))

    city_list = pickle.load(fileObject)  

    #print(city_list)     

    for city in city_list:
        print(city)
        #print(type(city))
        #print('['+str(city["name"])+'] - '+str(city["country"]))

    return city_list    

def add_city(city, country):
    city_list = read_cities()

    city3 = {
                'name': city, 
                'country': country
            } 
    city_list.append(city3)

    fileObject = open(file_Name,'wb') 

    pickle.dump(city_list, fileObject)     

if __name__ == '__main__':

    #store_city()

    #read_cities()

    #add_city('Montreal', 'Canada')

    pass

