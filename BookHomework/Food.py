class food():
    def __init__(self, name, carbs, protein, fat):
        self.name = name
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
    def checkCalories(self):
        calories = 0
        fromCarbs = self.carbs*4
        fromProtein = self.protein*4
        fromFat = self.fat*9
        calories = fromCarbs + fromProtein + fromFat
        return calories

class recipe():
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
    def checkCalories(self):
        calories = 0
        for food in self.ingredients:
            calories = calories + food.checkCalories()
        return calories

recipes = [recipe('Spaghet', [food('Pasta', 20, 1, 5), food('Cheese', 5, 1, 20), food('Lemon', 1, 1, 2)]),
    recipe('Chanken', [food('Raw Chanken', 1, 20, 5), food('Olive Oil', 1, 1, 20), food('Salt', 1, 1, 1)])]

for recipe in recipes:
    totalCalories = 0
    totalCalories = totalCalories + recipe.checkCalories()
    print(recipe.name + ' conatins ' + str(totalCalories) + ' total calories.')