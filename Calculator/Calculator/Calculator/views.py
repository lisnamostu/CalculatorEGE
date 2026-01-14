"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, jsonify, request
from Calculator import app
import pandas as pd

def createTemplateDatabase():
    df = pd.DataFrame({
        "id": ["uni1","uni2","uni3","uni4","uni5","uni6","uni7","uni8","uni9","uni10","uni11","uni12","uni13","uni14","uni15"],
        "name": ["МГУ - Информатика","МГУ - Физика","ВШЭ - Анализ данных","СПбГУ - Программирование","МИФИ - Кибербезопасность",
                 "МГТУ Баумана - Робототехника","ИТМО - Искусственный интеллект","РУДН - Лингвистика","МГУ - Мехмат",
                 "ВШЭ - Экономика","СПбГУ - Математика","МИЭТ - Электроника","КФУ - Химия","РГУ нефти и газа - Геология","УрФУ - Металлургия"],
        "min score": [280,260,290,275,265,270,285,240,278,282,270,250,230,255,220],
        "places": [100,120,80,90,150,110,70,200,130,95,100,180,150,225,130]
        })
    df.to_csv("database.csv", index=False)
    print(df)

def loadDatabase():
    df = pd.read_csv("database.csv")
    return df

@app.route('/getUnivList', methods=["POST"])
def sendUnivList():
    univList = ""
    for univName in df["name"]:
        univList += univName + ";"
    return jsonify(univList=univList)

#createTemplateDatabase()
df = loadDatabase()

@app.route('/')
def Website():
    """Renders the Calculator page."""
    return render_template('Calculator.html')

@app.route('/calculatefive', methods=["POST"])
def CalculateFive():
    Math = request.json["Math"]
    Rus = request.json["Rus"]
    Phys = request.json["Phys"]
    Inf = request.json["Inf"]
    Eng = request.json["Eng"]
    Ach = request.json["Ach"]
    univId = request.json["Univ"]
    minScore = int(df["min score"][df["id"]==univId].iloc[0])
    Sum = Math + Rus + Phys
    chance = Sum/minScore*1000//2/10
    return jsonify(chance=chance, totalScore=Sum, minScore=minScore)

@app.route('/calculateall', methods=["GET", "POST"])
def CalculateAll():
    data = request.json["data"]