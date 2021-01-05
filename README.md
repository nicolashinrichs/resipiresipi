# appetite
tech basics ll, gostudent 

Requirements:

- GUI/Front End: ideally fully functioning website -> What GUI? How will we build the website? 
- Database/Back End: A database of recipes -> How is this possible? Is it possible to access certain websites
- User Input/Interaction: Login and data input from user 

Features:

- Login: Possibility to login with an email address or a username and password
- Creating a personalized profile: choosing food preferences (vegetarian, vegan, pescatarian etc), allergies or intolerances (nuts, gluten-free, lactose-free), possibility of focusing on seasonal and regional food, option of saving and rating recipies in a personal cookbook, how much time you have, cooking skills (beginner to pro, for the difficulty of recipes) 
- Advanced funtions: notes section like what you did well or what you would change, adding own recipes, Spice cabinet (since spices tend to run out much slower)
- What’s in your fridge: basically a filter function in which you can type what foods you have at home. The search engine will spit out recipes containing the ingredients you have. The more ingredients match the recipies, the higher up the rank list they’ll be, function saying for example (no more than 3 ingredients missing) 
The recipe-page: contains the recipe,  what you are missing and links to where you can buy them. 

14.12 To Do's: 
- READ ME Description vervollständigen: Was soll die Website machen? 
- Gucken wie man Github mit Atom connencten kann? 
- Englische Chefkoch Seite suchen: Filter anschauen, lösung für fehlende Kriterien überlegen (zB. keine "vegan"-Funktion etc.
- nach Konkurrenten suchen 

Lösungsvorschlag: User: Dropdown Menü mit den Optionen Vegan, Vegetarisch, Laktosefrei usw. - auswählbar
Cose: die Optionen sind im Code aber als Suchbegriffe hinterlegt sind und teil des Filters


Problem: 
- Glaubwürdigkeit ist fragwürdig, da man sich auf die Korrektheit des Contents (der User) der Rezeptplattform verlassen muss 


05.01.2021

A website that is designed to focus on supporting a sustainable diet. 

The homepage will show you an ingredient search algorithm, that will let the user add ingredients he/she/they have at home and would like to use to cook a meal. This is the key feature of the APPETITE website and can be used by anyone. Creating an account will unlock additional features, like a more detailed filtering system (aka for allergies and other diet preferances). The algorithm will then browse the database (Spoonacular API?) and filter accordingly. The results will show recipe posts (per recipe: a picture and an indication of how many ingredients one has or need to buy). 

Features: No Account 
- Access to the Homepage: simple search (just adding ingredients), restricted to 3 ingredients

Features: Account:
- Access to the Homepage: in addition the the regular functions, the user is free to add an up to 8 ingredients and will find more in-depth filtering options like price point, 
- When you log in/create your profile, you will be asked for…
        - Your name: for a more personal feeling („Welcome back, Miazia!“ etc.)
        - Your address: for the option of finding a farmer’s market, an organic or a packaging free grocery store close to you
        - Details about your diet: allergies, lactose-free, gluten-free, other priorities - these will automatically get considered in your searches
- ((A reward system for a certain number of „sustainably“ cooked meals: for every recipe review one writes, you unlock cooking tips and ideas that you can save to your account))

Website Pages:
- Homepage: with the main search function 
- Profile: with personal information & saved recipes ((& tips from the reward program))
- A recipe page: information on the recipe and a Google map showing where the nearest market is where you can buy the rest of the needed ingredients. 
- ((If enough time, add an ‚About Us‘, ‚Impressum‘…))

Bewertungssystem: 
Depending of what diet preferances the user listed, the search results will be divided into four main categories (work with icons): 
- Recipes with mainly regional and in-season ingredients
- Vegan recipes 
- Vegetarian recipes
- Other recipes (including fish and meat)
The results will be listed according to the category they fall into and ranked by the amount of ingredients the user listed (or whatever the user chooses to filter by eg. ingredients, price, likes?, )

Lösungsansatz: 

- Profile settings: Spoonacular -> Search Recipes 
- Home (ingredient filtering) -> Search Recipes by Ingredient
- Regional and seasonal -> Excel 

