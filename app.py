# from flask_sqlalchemy import SQLAlchemy
from importlib.resources import Resource
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import json




url = open("databaseuri.txt", "r").read().rstrip()
app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = url
db = SQLAlchemy(app)
migrate = Migrate(app,db)



from model import *
# Return achievement based on input id
@app.route('/api/v1/achievement/id/<id>', methods = ['GET'])
def get_achievement(id):     
    x = AchievementModel.query.filter_by(id = id).all()
    return jsonify([s.serialized() for s in x])

# Return all achievements
@app.route('/api/v1/achievement/all')
def get_all_achievements():
    x = AchievementModel.query.all()
    return jsonify([s.serialized() for s in x])
# Return all achievements based on input dlc
@app.route('/api/v1/achievement/<dlc>')
def get_achievement_dlc(dlc):
    x = AchievementModel.query.filter_by(dlc = dlc).all()
    return jsonify([s.serialized() for s in x])
    
#TODO: Get achievements that dont require dlc
@app.route('/api/v1/achievement/None')
def get_no_dlc():
    x = AchievementModel.query
    return jsonify([s.serialized() for s in x])

#TODO: Get achievements that require dlc   
@app.route('/api/v1/achievement/Required')
def get_achievements_any_dlc():
    x = AchievementModel.query
    return jsonify([s.serialized() for s in x])


#TODO : Include versions before version specified   
@app.route('/api/v1/achievement/version/<version>')
def get_version_achievements(version):
    x=AchievementModel.query.filter_by(version=version).all()    
    return jsonify([s.serialized() for s in x])

#TODO: Difficulty route

if __name__=='__main__':
    app.run(debug=True)


#Endpoints
#  All achievements 
#  api/v1/achievement/all DONE
#
#  Each difficulty - Very Easy (VE), Easy (E), Medium (M), Hard (H), Very Hard (VH), Insane (I),Uncategorized (UC)-
#  api/v1/achievement/difficulty/VE api/v1/achievements/difficulty/E api/v1/achievements/difficulty/M api/v1/achievements/difficulty/H api/v1/achievements/difficulty/VH api/v1/achievements/difficulty/I api/v1/achievements/difficulty/UC
#
#  No DLC needed
#  api/v1/achievements/DLC/None
#
#  Achievements that require DLC
#  api/v1/achievements/DLC/Required
#
#  If choose play 1.28 include all those before 1.28
#  api/v1/achievements/version/1.28
#  api/v1/achievements/version/base
#
#
#
#
#
#
#