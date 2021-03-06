# https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,+sugar,+flour,+rice,+vanilla,+baking soda,+pears,+milk&number=10&apiKey=aceba4f6dcb2452098b2d81db2fdc588
# https:https://api.spoonacular.com/recipes/{id}/ingredientWidget.json?apiKey=aceba4f6dcb2452098b2d81db2fdc588
# Beispiel: https://api.spoonacular.com/recipes/490088/ingredientWidget.json?apiKey=aceba4f6dcb2452098b2d81db2fdc588
# Wir brauchen "name" und "amount" (name of ingredients & the according amount)
# https://api.spoonacular.com/recipes/{id}/analyzedInstructions?apiKey=aceba4f6dcb2452098b2d81db2fdc588
# Beispiel: https://api.spoonacular.com/recipes/600288/analyzedInstructions?apiKey=aceba4f6dcb2452098b2d81db2fdc588
# Wir brauchen "step" (die Steps der Kochanleitung)

# $[*].id
# $[*].image

from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
from datetime import datetime
import MySQLdb
import requests
import json
import csv
from jsonpath_ng import jsonpath, parse

app = Flask(__name__)
app.secret_key = "1234"

# Datenbank credentials werden in die app config eingetragen
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "appetite"

# Datenbank wird mit der App verknüpft
db = MySQL(app)


# ApiKey from json file
with open("secret.json", "r") as myfile:
    data = myfile.read()
obj = json.loads(data)
apiKey = str(obj["apiKey"])


def readJsonFromJsonDoc(filename):
    with open("./testJsonFiles/" + filename, "r") as myfile:
        data = myfile.read()
    return data


def csvToArrayList(filename):
    with open(filename, "r") as csvfile:
        csvFile = csv.reader(csvfile, delimiter=";", quotechar='"')
        data = []
        for row in csvFile:
            data.append(row)
        return data


# Index
# @app.route('/', methods=['GET'])
# def index():
#    print("testindex")
#    return render_template('testw3.html')

# declare empty list
ingredients = []
ingredientsForTextArea = []


def listToStringWithNewLine(s):

    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele + "\n"
    # return string
    return str1


def listToString(s):

    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
    # return string
    return str1


def createSaisonList(ingredientsList, saisonData):
    data = []
    for ingredientsRow in ingredientsList:
        for saisonRow in saisonData:
            # print("row:" + ingredientsRow + "|" + saisonRow[0])
            if saisonRow[0] == ingredientsRow:
                # print("saisonRow[i]" + saisonRow[0])
                for i in range(1, 12):
                    # print("saisonRow[i]" + saisonRow[i])
                    # print(datetime.today().month)
                    if saisonRow[i] == "x":
                        # print(i)
                        if i == datetime.today().month:
                            # print("Result: " + saisonRow[i])
                            data.append(True)
                            break
    return data


# Index with receipts
@app.route("/", methods=["GET", "POST"])
def getIngredients():
    print("test1")
    if request.method == "POST" and "ingredientInput" in request.form:
        print("test2")
        if (
            request.form["ingredientsTextArea"]
            and request.form.get("submit_button_submit")
            and len(ingredients) > 0
        ):
            print("test3: submit_button_submit")
            print(ingredients)
            numberOfResults = 4
            url = "https://api.spoonacular.com/recipes/findByIngredients?ingredients={0}&number={1}&apiKey={2}".format(
                ingredients, numberOfResults, apiKey
            )
            res = requests.get(url)
            json_data = json.loads(res.text)
            # json_data = json.loads(readJsonFromJsonDoc("testResponse.json"))
            # jsonpath_expression_receipts = parse("$[*]")
            receipts_list = json_data
            images_list = json_data
            # 2. API Call
            print("test3: 2. API Call")
            vegetarianList = []
            veganList = []
            saisonList = []
            ingredientsAllReceipts = []
            saisonData = csvToArrayList("SaisonkalenderAppetite.csv")
            # for i in range(numberOfResults):
            for i in range(numberOfResults):
                print("Rezept")
                id = receipts_list[i]["id"]
                url = "https://api.spoonacular.com/recipes/{0}/information?apiKey={1}".format(
                    id, apiKey
                )
                res = requests.get(url)
                json_data = json.loads(res.text)
                vegetarianList.append(json_data["vegetarian"])
                veganList.append(json_data["vegan"])
                for row in json_data["extendedIngredients"]:
                    ingredientsAllReceipts.append(row["name"])
                saisonList.append(createSaisonList(ingredientsAllReceipts, saisonData))
                ingredientsAllReceipts.clear()
            # receipts_list = [
            #    match.value for match in jsonpath_expression_receipts.find(json_data)
            # ]
            # images_list = [
            #    match.value for match in jsonpath_expression_image.find(json_data)
            # ]

            # saisonList2 = []
            print("test: extendedIngredients")

            # print(json_data["extendedIngredients"])
            print("test: saisonList")
            print(saisonList)
            # for row in saisonData:
            #    saisonList2.append(row["Ingredient"])

            # print("test: Print saisonList")
            # print(saisonList)
            # for row in saisonList:
            #    print(row)
            # saisonList.append()
            print("test3: receipts_list")
            ingredients.clear()
            return render_template(
                "testw3.html",
                receipts_list=receipts_list,
                images_list=images_list,
                vegetarianList=vegetarianList,
                veganList=veganList,
                numberOfResults=numberOfResults,
                saisonList=saisonList,
            )
        elif request.form["ingredientInput"] and request.form.get("submit_button_add"):
            print("test4: submit_button_more")
            ingredients.append("+" + request.form["ingredientInput"] + ",")
            ingredientsForTextArea.append(request.form["ingredientInput"])
            print(ingredients)
            return render_template(
                "testw3.html",
                ingredientsList=listToStringWithNewLine(ingredientsForTextArea),
            )
        else:
            return render_template("testw3.html")
    if request.method == "GET":
        return render_template("testw3.html")


# #Show receipts
# @app.route('/', methods=['GET','POST'])
# def getReceipts():
#     if request.method == 'POST' and 'ingredientInput' in request.form:


# #Login-Funktion
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         if 'username' in request.form and 'password' in request.form:
#             username = request.form['username']
#             password = request.form['password']
#             cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
#             cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s",
#                            (username, password))
#             info = cursor.fetchone()
#             print(info)
#             if info is not None:
#                 if info['username'] == username and info['password'] == password:
#                     session['loginSuccess'] = True
#                     return redirect(url_for('profile'))
#                 else:
#                     return redirect(url_for('index'))
#
#     return render_template('testw3.html')

# Registrierung-Funktion
@app.route("/new", methods=["GET", "POST"])
def new_user():
    if request.method == "POST":
        if (
            "username" in request.form
            and "email" in request.form
            and "password" in request.form
        ):
            username = request.form["username"]
            email = request.form["email"]
            password = request.form["password"]
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(
                "INSERT INTO users(username, email, password)VALUES(%s,%s,%s)",
                (username, email, password),
            )
            db.connection.commit()
            return redirect(url_for("index"))
    return render_template("registration.html")


# Ist der user angemeldet dann darf er in die Seite myAccount
@app.route("/new/profile")
def profile():
    if session["loginSuccess"]:
        return render_template("myAccount.html")


# Seite zum Ausloggen
@app.route("/new/logout")
def logout():
    session.pop("loginSuccess", None)
    return redirect(url_for("index"))


# #Index
# @app.route('/index', methods=['GET', 'POST'])
# def getIngredients():
#     if request.method == 'GET':
#     r = requests.get('https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,+sugar,+flour,+rice,+vanilla,+baking soda,+pears,+milk&number=10&apiKey=aceba4f6dcb2452098b2d81db2fdc588')
#     print(r.json())
#     #return redirect(url_for('index'))


# Hier wird das Python-Programm aufgerufen
if __name__ == "__main__":
    app.run(debug=True)
