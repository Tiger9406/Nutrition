import sqlite3

conn=sqlite3.connect('./foods.db')
c=conn.cursor()
# c.execute("""
#     CREATE TABLE recipe (
#         recipe_id INTEGER PRIMARY KEY,
#         title TEXT,
#         time INTEGER,
#         servings INTEGER,
#         calories INTEGER,
#         protein INTEGER,
#         carbs INTEGER,
#         sugar INTEGER,
#         fiber INTEGER,
#         total_fat INTEGER,
#         saturated INTEGER,
#         cholesteral INTEGER,
#         trans_fat INTEGER,
#         calcium INTEGER,
#         iron INTEGER,
#         sodium INTEGER,
#         vitaminC INTEGER,
#         potassium INTEGER
#     )
# """)

# c.execute("""
#     CREATE TABLE recipe_ingredient (
#         recipe_id INTEGER,
#         ingredient_id INTEGER,
#         quantity INTEGER,
#         FOREIGN KEY (recipe_id) REFERENCES recipe(recipe_id),
#         FOREIGN KEY (ingredient_id) REFERENCES ingredient(ingredient_id),
#         PRIMARY KEY (recipe_id, ingredient_id)
#     )
# """)

# c.execute("""
#     CREATE TABLE ingredient (
#         ingredient_id INTEGER PRIMARY KEY,
#         name TEXT,
#         category TEXT,
#         usda_id INTEGER,
#         calories INTEGER,
#         protein INTEGER,
#         carbs INTEGER,
#         sugar INTEGER,
#         fiber INTEGER,
#         total_fat INTEGER,
#         saturated INTEGER,
#         cholesteral INTEGER,
#         trans_fat INTEGER,
#         calcium INTEGER,
#         iron INTEGER,
#         sodium INTEGER,
#         vitaminC INTEGER,
#         potassium INTEGER
#     )
# """)



#inserting stuff


# recipe_data = (None, 'Chicken Soup', 30, 4, 200, 20, 30, 5, 5, 10, 5, 50, 0, 100, 10, 500, 50, 1000)

# Insert the recipe data into the recipe table
# c.execute("""
#     INSERT INTO recipe (
#         recipe_id, title, time, servings, calories, protein, carbs, sugar, fiber, total_fat, 
#         saturated, cholesteral, trans_fat, calcium, iron, sodium, vitaminC, potassium
#     ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
# """, recipe_data)

# ingredient_data = (None, 'Chicken', 'Meat', 1234, 335, 25, 0, 0, 0, 15, 4, 85, 0, 15, 1, 70, 0, 270)
# c.execute("""
#     INSERT INTO ingredient (
#         ingredient_id, name, category, usda_id, calories, protein, carbs, sugar, fiber, total_fat, 
#         saturated, cholesteral, trans_fat, calcium, iron, sodium, vitaminC, potassium
#     ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
# """, ingredient_data)

# # Get the ingredient_id of the new ingredient
# ingredient_id = c.lastrowid

# # Get the recipe_id of the recipe
# recipe_id = c.lastrowid

# # Insert a relationship between the recipe and the ingredient into the recipe_ingredient table
# recipe_ingredient_data = (recipe_id, ingredient_id, 1)
# c.execute("""
#     INSERT INTO recipe_ingredient (
#         recipe_id, ingredient_id, quantity
#     ) VALUES (?, ?, ?)
# """, recipe_ingredient_data)




conn.commit()
conn.close()