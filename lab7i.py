#!/usr/bin/env python3
# Student ID: 155871221

def function1():
    global schoolName
    schoolName = 'SICT'  # Modify the global object
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName
    schoolName = 'SSDO'  # Modify the global object
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'  # Initial global value
print('print() in main on schoolName:', schoolName)

function1()  # This will modify the global schoolName to 'SICT'
print('print() in main on schoolName:', schoolName)

function2()  # This will modify the global schoolName to 'SSDO'
print('print() in main on schoolName:', schoolName)
