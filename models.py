""" This module contains various objects  for the recipe app """


class User:
    ''' This class describes the user model '''

    def __init__(self, name, username, password):
        self.username = username
        self.username = username
        self.password = password
        self.recipes = []

    def add_recipe(self, description):
        """ Adds a new recipe to the categories"""
        if description not in self.recipes:
            self.recipes.append(description)
            return True
        return False

    def edit_recipe(self, description, new_description):
        ''' update an existing recipe with a new one'''
        if description in self.recipes:
            if not new_description in self.recipes:
                self.recipes = [new_description for description in self.recipes]
                return True
            return False
        return False

    def delete_recipe(self, description):
        """ deletes an existing recipe """
        if description in self.recipes:
            self.recipes.remove(description)
            return True
        return False


class Recipe:
    """describe the recipe model """

    def __init__(self, description):
        self.recipe_description = description
