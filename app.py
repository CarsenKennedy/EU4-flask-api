from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from sqlalchemy import or_ , cast
from sqlalchemy.dialects.postgresql import TEXT


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
@app.route('/api/v1/achievement/dlc/<dlc>')
def get_achievement_dlc(dlc):
    search_str = f'%{dlc.lower()}%'
    x = AchievementModel.query.filter(cast(AchievementModel.dlc, TEXT).ilike(search_str)).all()
    return jsonify([s.serialized() for s in x])
    
#Get achievements that dont require dlc
@app.route('/api/v1/achievement/dlc/None')
def get_no_dlc():
    x = AchievementModel.query.filter(AchievementModel.dlc.is_(None)).all()
    return jsonify([s.serialized() for s in x])

#Get achievements that require dlc   
@app.route('/api/v1/achievement/dlc/Required')
def get_achievements_any_dlc():
    x = AchievementModel.query.filter(AchievementModel.dlc.isnot(None)).all()
    return jsonify([s.serialized() for s in x])


#TODO : Include versions before version specified   
@app.route('/api/v1/achievement/version/<version>')
def get_version_achievements(version):
    x=AchievementModel.query.filter(version=version).all()    
    return jsonify([s.serialized() for s in x])

#General search endpoint
@app.route('/api/v1/achievement/search/<search>')
def get_search(search):
    search_str = f'%{search.lower()}%'
    try:
        version = float(search)
        x = AchievementModel.query.filter(or_(
            cast(AchievementModel.id, db.String()).ilike(search_str),
            AchievementModel.name.ilike(search_str),
            AchievementModel.description.ilike(search_str),
            AchievementModel.difficulty.ilike(search_str),
            cast(AchievementModel.dlc, TEXT).ilike(search_str),
            AchievementModel.version == version
        )).all()
    except ValueError:
        x = AchievementModel.query.filter(or_(
            cast(AchievementModel.id, db.String()).ilike(search_str),
            AchievementModel.description.ilike(search_str),
            AchievementModel.difficulty.ilike(search_str),
            cast(AchievementModel.dlc, TEXT).ilike(search_str)
        )).all()
    
    return jsonify([s.serialized() for s in x])

# Search by difficulty
@app.route('/api/v1/achievement/difficulty/<difficulty>')
def get_difficulty_achievements(difficulty):
    x=AchievementModel.query.filter(difficulty = difficulty).all()    
    return jsonify([s.serialized() for s in x])

@app.route('/api/v1/achievement/difficulty/VE')
def get_difficulty_VE():
    x=AchievementModel.query.filter(AchievementModel.difficulty == 'VE').all()    
    return jsonify([s.serialized() for s in x])

@app.route('/api/v1/achievement/difficulty/E')
def get_difficulty_E():
    x=AchievementModel.query.filter(AchievementModel.difficulty =='E').all()    
    return jsonify([s.serialized() for s in x])

@app.route('/api/v1/achievement/difficulty/M')
def get_difficulty_M():
    x=AchievementModel.query.filter(AchievementModel.difficulty == 'M').all()    
    return jsonify([s.serialized() for s in x])

@app.route('/api/v1/achievement/difficulty/H')
def get_difficulty_H():
    x=AchievementModel.query.filter(AchievementModel.difficulty == 'H').all()    
    return jsonify([s.serialized() for s in x])

@app.route('/api/v1/achievement/difficulty/VH')
def get_difficulty_VH():
    x=AchievementModel.query.filter(AchievementModel.difficulty=='VH').all()    
    return jsonify([s.serialized() for s in x])

@app.route('/api/v1/achievement/difficulty/I')
def get_difficulty_I():
    x=AchievementModel.query.filter(AchievementModel.difficulty=='I').all()    
    return jsonify([s.serialized() for s in x])

if __name__=='__main__':
    app.run(debug=True)

