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
        <form action="" method="POST">
            <label for="word">
            Rotate by:
            <input type="text" name="rot" value=0 />
            <textarea name="text"></textarea>
            </label>
            <input type="submit" />
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    newtext = "<h1>" + rotate_string(text, rot) + "</h1>"
    return newtext

@app.route("/")
def index():
    return form

app.run()