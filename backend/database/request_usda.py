import requests

import os


API_KEY= os.environ.get('USDA_API_KEY')

def get_nutritional_info(ingredient_name):
    url = f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key={API_KEY}&query={ingredient_name}&fields=foodNutrients.nutrientName,foodNutrients.nutrientNumber,foodNutrients.unitName'
    response = requests.get(url)

    if(response.status_code != 200):
        return None
    data=response.json()
    if 'foods' in data and len(data['foods'])>0:
        nutrients= data['foods'][0]['foodNutrients']
        cleaned_nutrients = [{k: nutrient[k] for k in ['nutrientName', 'value', 'unitName']} for nutrient in nutrients]
        return cleaned_nutrients
    return None

# everything's per 100 gram

# print(get_nutritional_info('apple'))