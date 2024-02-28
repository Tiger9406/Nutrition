import sqlite3

conn=sqlite3.connect('./database/foods.db')
c=conn.cursor()
c.execute("""
    CREATE TABLE recipe (
        recipe_id INTEGER PRIMARY KEY,
        title TEXT,
        time INTEGER,
        servings INTEGER,
    )
""")

c.execute("""
    CREATE TABLE recipe_ingredient (
        recipe_id INTEGER,
        ingredient_id INTEGER,
        quantity INTEGER,
        FOREIGN KEY (recipe_id) REFERENCES recipe(recipe_id),
        FOREIGN KEY (ingredient_id) REFERENCES ingredient(ingredient_id),
        PRIMARY KEY (recipe_id, ingredient_id)
    )
""")

c.execute("""
    CREATE TABLE ingredient (
        ingredient_id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        usda_id INTEGER,
        calories INTEGER,
        protein INTEGER,
        carbs INTEGER,
        sugar INTEGER,
        fiber INTEGER,
        total_fat INTEGER,
        saturated INTEGER,
        cholesteral INTEGER,
        trans_fat INTEGER,
        calcium INTEGER,
        iron INTEGER,
        sodium INTEGER,
        vitaminC INTEGER,
        potassium INTEGER,
    )
""")

conn.commit()
conn.close()