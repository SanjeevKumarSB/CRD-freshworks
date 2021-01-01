import threading as th
from threading import*
import op as p
import time
import json

a=int(input("1.create\n2.read\n3.delete\n4.exit\nEnter the option:"))
while a!=4:
  if(a==1):
    k=input("Enter the key to create:\n")
    c=(input("Enter the value:\n"))
    t=int(input("Enter the time to live(enter 0 when you dont need it):\n"))
    t1=th.Thread(target=(p.create),args=(k,c,t)) 
    t1.start()
    
  
  if(a==2):
    k=input("Enter the key to read:\n")
    t2=th.Thread(target=(p.read),args=[k]) 
    t2.start()
   
  if(a==3):
    k=input("Enter the key to be deleted:")
    t3=th.Thread(target=(p.delete),args=[k]) 
    t3.start()
    
  
  time.sleep(0.5)
  print("--------------------------------------------------")  
  a=int(input("1.create\n2.read\n3.delete\n4.exit\nEnter the option:"))
