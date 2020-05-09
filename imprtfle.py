import csv

import os
def sum(a,b):
  c=a+b
  return c
def sub(a,b):
  c=a-b
  return c
def readfile(filename):
    with open(filename,'r') as csvfile:
     reader = csv.reader(csvfile)
     for row in reader:
         print(row)


def camera1():
    os.startfile("C:\Program Files (x86)\ArcSoft\WebCam Companion 3\\uWebCam.exe")
def notpad():
    os.system("notepad.exe")
