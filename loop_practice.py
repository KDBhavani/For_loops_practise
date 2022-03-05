# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 17:15:01 2022

@author: sys
"""
# # prob1:
# # student_roll_number=[121,131,141,151]
# # create a list as student_roll_number_updated
# student_roll_number_updated=[221,231,241,251]

# 1stmethod***************************************************
student_roll_number=[121,131,141,151]
print(student_roll_number)
student_roll_number_updated=[]
for var in student_roll_number:
    print(var)
    x=var+100
    print(x)
    student_roll_number_updated.append(x)
    print("student_roll_number_updated.................",student_roll_number_updated)
student_roll_number_updated
    
   # 2nd method****************************************************************
student_roll_number=[121,131,141,151]
print(student_roll_number)
student_roll_number_updated=[]
for var in student_roll_number:
    print("var..................",var)
    addition=100
    print("addition................",addition)
    output=var+addition
    print("output.................",output)
    student_roll_number_updated.append(output)
    print("student_roll_number_updated.................",student_roll_number_updated)
student_roll_number_updated
    
# prob2:
# student_roll_number=[121,131,141,151]
# create a list as last_student_roll_number
# last_student_roll_number=[251]

student_roll_number=[121,131,141,151]
print(student_roll_number)
last_student_roll_number=[]
for value in student_roll_number:
    print("value..................",value)
    addition=100
    print("addition................",addition)
    output=value+addition
    print("output.................",output)
    last_student_roll_number.append(output)
    print("last_student_roll_number.................",last_student_roll_number)
print(last_student_roll_number[-1])
last_student_roll_number[-1]



# prob3:
# create a list as automated_list
# student_roll_number_updated=[10,20,30,40,50,60,70,80,90]
automated_list=[]
student_roll_number_updated=[]
for var in range(10,100,10):
    student_roll_number_updated.append(var)
    print(var)
student_roll_number_updated

# prob4:
# student_names=["ajay","ravi", "kiranmai","tanuja","hamida"]
# display all names like "The student is ajay" like that
student_names=["ajay","ravi", "kiranmai","tanuja","hamida"]

def student_names(names="*"):
    print("The student is "  ,    names )
student_names("ajay")   
student_names("ravi")
student_names("kiranmai")
student_names("tanuja")
student_names("hamida")

# student_names=["ajay","ravi", "kiranmai","tanuja","hamida"]
# student_names
# for name in student_names:
#     print(name)
#     output= " The student is " + name
#     print(output)





# prob5:
# student_names=["ajay","ravi", "kiranmai","tanuja","hamida"]
# create a list as student_names_updated 
# student_names_updated=["ajay 10thclass","ravi 10thclass", "kiranmai 10thclass","tanuja 10thclass","hamida 10thclass"]
student_names=["ajay","ravi", "kiranmai","tanuja","hamida"]
student_names
student_names_updated=[]
for name in student_names:
    print(name)
    output= name + " 10thclass"
    print(output)
    student_names_updated.append(output)
    print(student_names_updated)
print(student_names_updated)

# prob6:
# student_names=["ajay","ravi", "kiranmai","tanuja","hamida"]
# create a list as last_student_names
# last_student_names=["hamida"]
student_names=["ajay","ravi", "kiranmai","tanuja","hamida"]
last_student_names=[]
for names in student_names:
    print(names)
    last_student_names.append(names)
    print(last_student_names)
last_student_names[-1]
    



    
    
    


    

    
    
    

    