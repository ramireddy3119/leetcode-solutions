class Solution:
    def findAllRecipes(self,recipes, ingredients, supplies):
        available = set(supplies)
        possible_recipes = set()
        recipes_left = True

        while recipes_left:
            recipes_left = False
            for i, recipe in enumerate(recipes):
                if recipe not in possible_recipes and all(ing in available for ing in ingredients[i]):
                    available.add(recipe)
                    possible_recipes.add(recipe)
                    recipes_left = True 

        return list(possible_recipes)

            