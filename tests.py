import unittest
from models import User,Category,Recipe

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("samiiha", "nsamiiha", "password")

   
    def test_add_category(self):
        self.assertEqual( self.user.add_category("dinner"),
                        "recipe category is added succesfully")

    def test_add_category_name_already_exists(self):
        self.user.add_category("dinner")
        self.assertEqual( self.user.add_category
                         ("dinner"),
                         "recipe category already exists")


    def test_edit_category_not_found(self):
        self.assertEqual( self.user.edit_category("absent", "newtype"),
                         "not title found")

    def test_edit_category_successful(self):
        self.user.add_category("Snacks")
        self.assertEqual( self.user.edit_category("Snacks","local foods"),"recipe_category edited succesfully")
        
    def test_delete_category_not_found(self):
        self.assertEqual( self.user.delete_category("not exist"), "category not found")

    def test_delete_category_deleted(self):
        self.user.add_category("lunch recipes")
        self.assertEqual( self.user.delete_category("lunch recipes"),
                         "category deleted")
        
    
class Recipe_categoryTest(unittest.TestCase):
    
    def setUp(self):
        self.recipes = Category("")

    def test_recipe_instantiation(self):
        self.assertIsInstance(self.recipes, Category,
                              "Failed to instantiate")

    def test_add_recipe_added(self):
        self.assertEqual(self.recipes.add_recipe("pillawo",'discription'), "recipe added succesfully")

    def test_add_recipe_exists(self):
        self.recipes.add_recipe("pillawo",'description')
        self.assertEqual(self.recipes.add_recipe(
            "pillawo",'description'), "recipe already exists")

    def test_edit_recipe_not_found(self):
        self.assertEqual(self.recipes.edit_recipe(
            "chicken recipe", "beef recipe"), "description not found")

   
    def test_edit_recipe_edited_succesfully(self):
         self.recipes.add_recipe("pizza",'description')
         self.assertEqual(self.recipes.edit_recipe("pizza", "chicken"), "description not found")

    def test_delete_recipe_not_found(self):
        self.assertEqual(self.recipes.delete_recipe(
        "katogo",'description'), "No recipe to delete")

    def test_recipe_deleted(self):
        self.recipes.add_recipe("katogo",'description')
        self.assertEqual(self.recipes.delete_recipe("katogo",'description'), "recipe deleted")

class RecipeTest(unittest.TestCase):
    def setUp(self):
        self.recipe = Recipe("title","description")


    def test_create_item_instance(self):
        self.assertIsInstance(self.recipe, Recipe, "Failed to create instance")
