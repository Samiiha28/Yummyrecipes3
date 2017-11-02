import unittest
from models import User,Recipe

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("samiiha", "nsamiiha", "password")

   
    def test_add_recipe(self):
        self.assertEqual( self.user.add_recipe("matooke"),True)

    def test_add_recipename_already_exists(self):
        self.user.add_recipe("matooke")
        self.assertEqual( self.user.add_recipe("matooke"),False)


    def test_edit_recipe(self):
        self.assertEqual( self.user.edit_recipe("absent", "newtype"),False)

    def test_edit_category_successful(self):
        self.user.add_recipe("Snacks")
        self.assertEqual( self.user.edit_recipe("Snacks","local foods"),True)
        
    def test_delete_category_not_found(self):
        self.assertEqual( self.user.delete_recipe("not exist"), False)

    def test_delete_category_deleted(self):
        self.user.add_recipe("lunch recipes")
        self.assertEqual( self.user.delete_recipe("lunch recipes"),True)

class RecipeTest(unittest.TestCase):
    def setUp(self):
        self.recipe = Recipe("description")
