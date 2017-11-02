""" This module contains various objects  for the recipe app """
class User:
    ''' This class describes the user model '''
    def __init__ (self,name,username,password):
        self.username = username
        self.username = username
        self.password = password
        self.categories ={}

    def add_category(self,title):
        """ Adds a new category to the users category"""
        if title not in self.categories:
            self.categories[title] = Category(title)
            return "recipe category is added succesfully" #else
        return "recipe category already exists" #else

    def edit_category(self,title,newtitle):
        ''' updates the category with  newtitle'''
        if title in self.categories:
            if not newtitle in self.categories:
                self.categories[newtitle] = self.categories.pop(title)
                return "recipe_category edited succesfully" #else
            return "recipe_category already exists" #else
        return "not title found"

    def delete_category(self,title):
        """ deletes an existing category"""
        if title in self.categories:
            self.categories.pop(title)
            return "category deleted" #else
        return "category not found" #else


class Category:
    """ descibe the category model """
    def __init__(self,title):
        self.title = title
        self.recipes ={}

    def add_recipe(self,title, description):
        """ Adds a new recipe to the categories"""
        if description not in self.recipes:
            self.recipes[description] =Recipe(title,description)
            return "recipe added succesfully"
        return "recipe already exists"

    def edit_recipe(self,description,new_description):
        ''' update an existing recipe with a new one'''
        if description in self.recipes:
            if not new_description in self.recipes:
                self.recipes[new_description] = self.recipes.pop(description)
                return "recipe adited successfully"
            return "new_description already exist"
        return "description not found"
        
    
    def delete_recipe(self,title,description):
        """ deletes an existing recipe """
        if description in self.recipes:
            self.recipes.pop(title,description)
            return "recipe deleted"
        return "No recipe to delete"

class Recipe:
    """describe the recipe model """
      
    def __init__(self, title, description):
        self.recipe_title = title
        self.recipe_description = description
  