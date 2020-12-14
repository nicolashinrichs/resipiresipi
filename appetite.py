from flask import Flask, render_template, request
app = Flask(__name__)

database = {
    "Pfannkuchen": ["mehl","eier","milch","zucker"],
    "Cabonara": ["spaghetti","speck","eier","parmesan","mehl"]
}

@app.route('/', methods = ['post', 'get'])
def index ():
    if request.method == 'POST':
        ingredient1 = request.form.get('ingredient1')
        ingredient1 = ingredient1.lower()
        ingredient2 = request.form.get('ingredient2')
        ingredient2 = ingredient2.lower()

        #print ('Wir haben: ' + ingredient1 + ingredient2)
        #age = request.form.get('age')
        #print ('Ich bin ' + age + ' Jahre alt.')
        meals = []
        allIngredients = []
        for meal in database:
            ingredients = database[meal]
            if (ingredient1 in ingredients and ingredient2 in ingredients):
                meals.append(meal)
                allIngredients.append(ingredients)

    return render_template('home_index.html', meals=meals, ingredients=allIngredients)

if __name__ == '__main__' :
    app.run()
