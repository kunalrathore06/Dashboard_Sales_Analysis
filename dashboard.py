# from crypt import methods
from flask import Flask, request, render_template , jsonify
import speech_recognition as sr
import pandas as pd
import mysql.connector
# import os
# import sys


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    charset = 'utf8mb4',
    database = 'dashboardkeywords'
)

mycursor = mydb.cursor()
query = "SELECT *  from keyword"

mycursor.execute(query)
string = "sales in january ?"
string = string.split()
values_from_dataset = []

app = Flask(__name__)
@app.route('/')

def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register_form.html")

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/settings')
def setting():
    return render_template('settings.html')

@app.route('/client')
def client():
    return render_template('client.html')

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/help')
def help():
    return render_template('help.html')

r = sr.Recognizer()

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        df = pd.read_csv(file)
        X_axis = request.form.get("xaxis")
        Y_axis = request.form.get("yaxis")
        X_axis_values = df[X_axis].values
        Y_axis_values = df[Y_axis].values
        columns = list(df.columns)
        null_values = df.isnull().sum()
        return render_template('index.html', X=X_axis_values, Y=Y_axis_values,shape=df.shape, columnName=columns,nullValues = null_values)
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        print('method is post')
        text = recognize()
        text1 = split_string(text)
        first = text1[1]
        second = text1[0]
        print(text1)
        print('recognised result: ',  text)
        return jsonify(result=text,result_first=first,result_second=second)

def recognize():
    try:
        with sr.Microphone() as source:
            # read the audio data from the default microphone 
            print('listening...')
            audio_data = r.record(source, duration=10)
            print("Recognizing...")
            text = str(r.recognize_google(audio_data))
            return text
            
    except Exception as E:
        print(E)
def split_string(text):
    b = ["sales","aakash","january","july","month","a","b"]
    text = text.lower()
    text = text.split()
    c = []
    for i in text:
        if i in b:
            c.append(i)
    return c
    

if __name__ == '__main__':
    app.run(debug=True)
