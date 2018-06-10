from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/Rotate" method="post" id="usrform">
            <label for="rot" >Rotate by:</label>
            <input id="rot" type="text" name="rot" value= '0'/>
            <textarea name="text" form="usrform"></textarea> 
            <input type="submit", value="Rotate"/>
        </form>

    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/Rotate", methods=['POST'])
def encrypt():    

    rot = request.form['rot']
    text = request.form['text']
    rotate_string (text, int(rot))
    return '<h1>ROT: ' + rot + ' TEXT: ' + text + ' NEW: ' + rotate_string (text, int(rot)) + '</h1>'
   
app.run()
