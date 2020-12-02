import threading 
from threading import*
import time

dic={} #ditionary

def create(key,value,t_out=0):
    if key in dic:
        print("error: this key already present") #error message1
    else:
        if(key.isalpha()):
            if len(dic)<(1069547520) and value<=(16777216): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if t_out==0:
                    l=[value,t_out]
                else:
                    l=[value,time.time()+t_out]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    dic[key]=l
            else:
                print("error: Not Enough Memory\n")#error message2
        else:
            print("error: key not valid")#error message3

#for read operation
#use syntax "read(key_name)"
            
def read(key):
    if key not in dic:
        print("error: Key does not exist") #error message4
    else:
        b=dic[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                strng=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return strng
            else:
                print("error: ",key,"has expired") #error message5
        else:
            strng=str(key)+":"+str(b[0])
            return strng

#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in dic:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=dic[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del dic[key]
                print("key is successfully deleted")
            else:
                print("error:",key,"has expired") #error message5
        else:
            del dic[key]
            print("key is successfully deleted")

#I have an additional operation of modify in order to change the value of key before its expiry time if provided

#for modify operation 
#use syntax "modify(key_name,new_value)"

def modify(key,value):
    b=dic[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in dic:
                print("error:key not found in database") #error message6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                dic[key]=l
        else:
            print("error: time-to-live of",key,"has expired") #error message5
    else:
        if key not in dic:
            print("error: key not found in database") #error message6
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            dic[key]=l
