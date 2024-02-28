from flask import Flask
import sqlite3

app = Flask(__name__)

DATABASE = './foods.db'


def get_recipe(recipe_id):
    conn=sqlite3.connect(DATABASE)
    c=conn.cursor()
    c.execute("""
        SELECT * FROM recipe WHERE recipe_id=?
    """, (recipe_id,))
    return c.fetchone()

def get_ingredients(recipe_id):
    conn=sqlite3.connect(DATABASE)
    c=conn.cursor()
    c.execute("""
        SELECT * FROM ingredient
        JOIN recipe_ingredient ON ingredient.ingredient_id=recipe_ingredient.ingredient_id
        WHERE recipe_ingredient.recipe_id=?
    """, (recipe_id,))
    return c.fetchall()

@app.route('/')
def index():
    return get_ingredients(1)
    # return 'Healthy Eating!'

if __name__ == '__main__':
    app.run(debug=True)