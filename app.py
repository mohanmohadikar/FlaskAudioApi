from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
import datetime
from validate import validateParticipants, validatePodcast, validateName, validateDuration, validateAudioBook

# initializing fask app.
app = Flask(__name__)

app.secret_key = "secretkey"
app.config['MONGO_URI'] = "mongodb+srv://mohan:mohanmohan@cluster0.haxfw.mongodb.net/<dbname>?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/add', methods=['POST'])
def add_audio():
    _json = request.json
    _name = _json['name']
    _duration = _json['duration']
    _type = _json['type']
    _content = _json['content']
    _upload_time = datetime.datetime.now()
    _host = _json['host']
    _participants = _json['participants']
    _author = _json['author']
    _narrator = _json['narrator']

    if (validateName(_name) and validateDuration(_duration) 
    and _type and _content and _upload_time 
    and validatePodcast(_type, _host) 
    and validateParticipants(_participants) 
    and validateAudioBook(_type, _author, _narrator) 
    and request.method == 'POST'):
        id = mongo.db.audio.insert(
            {
                'type':_type,
                'audioFileMetadata':{
                    'name':_name,
                    'duration':_duration,
                    'content':_content,
                    'upload_time':_upload_time,
                    'host':_host,
                    'participants':_participants,
                    'author':_author,
                    'narrator':_narrator
                }
            }
        )

        resp = jsonify("AUDIO ADDED SUCCESSFULLY")
        resp.status_code = 200
        return resp
    else:
        return not_found()

@app.route('/audios')
def audios():
    audios = mongo.db.audio.find()
    resp = dumps(audios)
    return resp

@app.route('/audio/<id>')
def audio(id):
    audio = mongo.db.audio.find_one({
        '_id': ObjectId(id)
    })
    resp = dumps(audio)
    return resp

@app.route('/delete/<id>', methods=['DELETE'])
def delete_audio(id):
    mongo.db.audio.delete_one({
        '_id':ObjectId(id)
    })
    resp = jsonify("AUDIO DELETED SUCCESSFULLY")
    resp.status_code = 200
    return resp


@app.route('/update/<id>', methods=['PUT'])
def update_audio(id):
    _id = id
    _json = request.json
    _name = _json['audioFileMetadata']['name']
    _duration = _json['audioFileMetadata']['duration']
    _type = _json['type']
    _content = _json['audioFileMetadata']['content']
    _upload_time = datetime.datetime.now()
    _host = _json['audioFileMetadata']['host']
    _participants = _json['audioFileMetadata']['participants']
    _author = _json['audioFileMetadata']['author']
    _narrator = _json['audioFileMetadata']['narrator']

    if (validateName(_name) and validateDuration(_duration) 
    and _type and _content and _upload_time 
    and validatePodcast(_type, _host) 
    and validateParticipants(_participants) 
    and validateAudioBook(_type, _author, _narrator) 
    and request.method == 'PUT'):
        mongo.db.audio.update_one(
            {
                '_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)
            },
            {
                '$set':{
                    'type':_type,
                    'audioFileMetadata':{
                        'name':_name,
                        'duration':_duration,
                        'content':_content,
                        'upload_time':_upload_time,
                        'host':_host,
                        'participants':_participants,
                        'author':_author,
                        'narrator':_narrator
                    }
                }
            }
        )
        resp = jsonify("AUDIO UPDATED SUCCESSFULLY")
        resp.status_code = 200
        return resp
    
    else:
        return not_found()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status':404,
        'message':'NOT FOUND' + request.url + request.error
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


if __name__ == "__main__":
    app.run(debug=True)

