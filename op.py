import json
import threading as t
from threading import*
import time
import sys
import os


dic={} 
dic2={}


f=open('sample.json','w')

def create(key,value,timeout=0):
    if key in dic:
        print("error: this key already exists") 
    else:
        if(key.isalpha()):
            
            if os.path.getsize('sample.json')<(1024*1024*1024) and sys.getsizeof(value)<=(16*1024):
              print("Data with key ",key," and value ",value," is created successfully") 
              
              
              
              
              if len(key)<=32: 
                    dic[key]=value
                    dic2[key]=timeout
                    json_object = json.dumps(dic,indent = 4)
                    with open('sample.json', "w") as outfile: 
                      outfile.write(json_object) 
                    

            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")


            
def read(key):
    if key not in dic:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        if dic2[key]!=0:
            if time.time()<dic2[key]: 
                with open('sample.json', 'r') as openfile: 
   
                 json_object = json.load(openfile)
                print(key,":",json_object[key])
             
    
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
             with open('sample.json', 'r') as openfile: 
   
              json_object = json.load(openfile)
             print(key,":",json_object[key])
             
             
    


def delete(key):
    if key not in dic:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        if dic2[key]!=0:
            if time.time()<dic2[key]: 
                del dic[key]
                del dic2[key]
                print()
                json_object = json.dumps(dic,indent = 4) 
                with open('sample.json', "w") as outfile: 
                 outfile.write(json_object) 
                
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            del dic[key]
            del dic2[key]
            print("data with key ",key," is successfully deleted")
            json_object = json.dumps(dic,indent = 4) 
            with open('sample.json', "w") as outfile: 
              outfile.write(json_object) 
            
