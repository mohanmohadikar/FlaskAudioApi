# FlaskAudioApi
##This is a simple example of CRUD operations using Python(Flask) with NoSql(MongoDB).

### Heroku Base url : 
"https://flask-audio-api.herokuapp.com"
### LocalHost Base url : 
"http://localhost:5000" or "http://127.0.0.1:5000"

### endpoints:
1) Add audio:
```
baseUrl/add
```
```
{
    "name":"audiobook2",
    "duration":555,
    "type":"audiobook",
    "content":"audiobook2url",
    "host":"",
    "participants":[],
    "author":"a2",
    "narrator":"n2"
}
```

2) Fetch audios list:
```
baseUrl/audios
```

3) Fetch single audio:
```
baseUrl/audio/<id>
```

4) Delete audio:
```
baseUrl/delete/<id>
```

5) Update audio:
```
baseUrl/update/<id>
```
```
{
    "name":"audiobook2",
    "duration":555,
    "type":"audiobook",
    "content":"audiobook2url",
    "host":"",
    "participants":[],
    "author":"a2",
    "narrator":"n2"
}
```

### Convert Audio file to String:
```
python audioUtility.py
```
Resultant string will be stored into a variable.(Use "print(result_string)")
Note: Make sure your input audio file (for eg. "example.mp3" is present in current directory).


### Convert String to Audio file:
```
python audioUtility.py
```
Resultant Audio file will be generated as "example_op.mp3".(Use "print(result_string)")
