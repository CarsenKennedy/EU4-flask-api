import json
import psycopg2
import webscraper as webscraper
from model import AchievementModel
from app import db
url = open("databaseuri.txt", "r").read().rstrip()
db.create_all()
data = webscraper.scrape() 
for count,index in enumerate(data,1):
    a = AchievementModel(
        id = count,
        name = data[index]['achievement'],
        description=data[index]['description'],
        starting_condition=data[index]['starting'],
        requirements=data[index]['requirements'],
        version=float(data[index]['version']),
        difficulty=data[index]['difficulty'],
        dlc=data[index]['dlc'])
    db.session.add(a)   
db.session.commit()