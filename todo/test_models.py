from django.test import TestCase
from .models import Item

# Create your tests here.
# THIS TEST WILL BE USED TO TEST OUR MODELS.
# NOTE: We are not testing the internal Django code because it's
# already been tested by the django developers themselves but one
# thing we can test just to demonstrate the philosophy is "to test
# that our 'todo items' will be created by default with the 'done
# status' of 'False'.


#  We'll create a class called 'TestModels' which inherits the built-in
# TestCase class & thereby giving us access to all its functionality.
class TestModels(TestCase):

    # Every test is defined as a method that begins with the word 'test'
    # & will take in 'self' as its only parameter. 'self' here refers to
    # our TestModels class which because it inherits the TestCase class
    # will have a bunch of pre-built methods and functionality that we
    # can use.
    def test_done_defaults_to_false(self):
        # We'll create an 'item' using 'item.objects.create()' & give it an
        # argument of 'name' with the value of 'Test Todo Item'.
        item = Item.objects.create(name='Test Todo Item')
        # We then use 'assertFalse' to confirm that its 'done status' is
        # truly 'False' by default.
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        # We'll create an item with the name of 'Tests Todo Item'.
        item = Item.objects.create(name='Test Todo Item')
        # We then use 'self.assertEqual' to confirm that this name
        # is returned when we render this item as a string.
        self.assertEqual(str(item), 'Test Todo Item')
