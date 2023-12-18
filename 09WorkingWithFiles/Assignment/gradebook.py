import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))



f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f) 
a=0
b=0
c=0
d=0
f=0
freshmentotal=0
freshnumber=0
freshaverage=0
sfailing= 0
for row in reader:
    name, gradelevel, percent = row
    percent= int(percent)
    gradelevel= int(gradelevel)
    if percent> 89:
        a=int(a+1)
    if percent> 79:
        b=int(b+1)
    if percent> 69:
        c=int(c+1)
    if percent> 59:
        d=int(d+1)
    if percent< 60:
        f=int(f+1)
    if gradelevel==9:
        freshmentotal= int(freshmentotal+ percent)
        freshnumber= int(freshnumber+1)
        freshaverage= freshmentotal/freshnumber
    if gradelevel==12 and percent<60:
        sfailing=int(sfailing+1)

print("a,b,c,d,e->",a,b,c,d,)
print("Freshman avergae",freshaverage)
print("seniors failing",sfailing)





        



