import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
f = open("../data/1000-largest-us-cities.json", "r")
cities = json.load(f)
f.close()

def city_with_longest_name():
    city=0
    for city in cities:
        if len("city")>city