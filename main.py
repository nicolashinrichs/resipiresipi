#https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,+sugar,+flour,+rice,+vanilla,+baking soda,+pears,+milk&number=10&apiKey=aceba4f6dcb2452098b2d81db2fdc588
#https:https://api.spoonacular.com/recipes/{id}/ingredientWidget.json?apiKey=aceba4f6dcb2452098b2d81db2fdc588
#Beispiel: https://api.spoonacular.com/recipes/490088/ingredientWidget.json?apiKey=aceba4f6dcb2452098b2d81db2fdc588
from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
import MySQLdb
import requests
import json
from jsonpath_ng import jsonpath, parse

app = Flask(__name__)
app.secret_key = "1234"

#Datenbank credentials werden in die app config eingetragen
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "appetite"

#Datenbank wird mit der App verknüpft
db = MySQL(app)


#Index
@app.route('/', methods=['GET', 'POST'])
def getIngredients():
    if request.method == 'GET': #Auch wenn der Button nicht gedrückt wird kommt eine Response. Beheben
        res = requests.get('https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,+sugar,+flour,+rice,+vanilla,+baking soda,+pears,+milk&number=2&apiKey=aceba4f6dcb2452098b2d81db2fdc588')
        jsonDoc = res.json()
        jsonpath_expression = parse('employees[*].id')
        print("Test")
    return render_template('testw3.html', testResponse = res.json())

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

#Registrierung-Funktion
@app.route('/new', methods=['GET', 'POST'])
def new_user():
    if request.method == "POST":
        if "username" in request.form and "email" in request.form and "password" in request.form:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("INSERT INTO users(username, email, password)VALUES(%s,%s,%s)",
                        (username, email, password))
            db.connection.commit()
            return redirect(url_for('index'))
    return render_template("registration.html")

#Ist der user angemeldet dann darf er in die Seite myAccount
@app.route('/new/profile')
def profile():
    if session['loginSuccess']:
        return render_template("myAccount.html")

#Seite zum Ausloggen
@app.route('/new/logout')
def logout():
    session.pop('loginSuccess', None)
    return redirect(url_for('index'))

# #Index
# @app.route('/index', methods=['GET', 'POST'])
# def getIngredients():
#     if request.method == 'GET':
#     r = requests.get('https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,+sugar,+flour,+rice,+vanilla,+baking soda,+pears,+milk&number=10&apiKey=aceba4f6dcb2452098b2d81db2fdc588')
#     print(r.json())
#     #return redirect(url_for('index'))



#Hier wird das Python-Programm aufgerufen
if __name__ == '__main__':
    app.run(debug=True)
