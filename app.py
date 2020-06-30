from flask import Flask, render_template, request, session
import json
import requests

app=Flask(__name__)

with open('static/currency.json','r') as fhand:
    symbols=json.load(fhand)

base_url="http://data.fixer.io/api/latest?"
access_key="d04285ab839a6e10f1e74b4283856392"
url=base_url+"access_key="+access_key


@app.route("/", methods=["GET","POST"])
def index():
    try:
        res= requests.get(url)
        if res.status_code != 200:
            result='ERROR: API request unsuccessful'
        else:
            data = res.json()
            from_symbol = str(request.form.get("from_symbol"))
            to_symbol = str(request.form.get("to_symbol"))
            rate = (data['rates'][to_symbol])/(data['rates'][from_symbol])
            result = '1 ' + from_symbol + " = " + str(rate) + " " + to_symbol
    except:
        result=''
    return render_template("index.html", symbols=symbols, result=result)
