from django.test import TestCase
from .forms import ItemForm

# Create your tests here.
# THIS TEST WILL BE USED TO TEST OUR FFORMS.


#  We'll create a class called 'TestItemForm' which inherits the
# 'TestCase' class & contains all the tests for this form.
class TestItemForm(TestCase):

    # Every test is defined as a method that begins with the word 'test'
    # & will take in 'self' as its only parameter. 'self' here refers to
    # our 'TestItemForm' class which because it inherits the TestCase class
    # will have a bunch of pre-built methods and functionality that we
    # can use.
    def test_item_name_is_required(self):
        # We'll instantiate a form & we'll deliberately leave it without a name
        # to simulate a user who submitted the form without filling it out.
        # This form should not be valid so we'll use assertFalse to ensure that
        # that's the case.
        form = ItemForm({'name': ''})
        # This tests for if the form is invalid. If it is, it should send back
        # a dictionary of fields on which there were errors & the associated
        # error messages.
        self.assertFalse(form.is_valid())
        # We'll be more specific by using 'assertIn' to assert whether
        # or not there's a name key in the dictionary of form errors.
        # This tests that the error occurred on the 'name' field.
        self.assertIn('name', form.errors.keys())
        # We'll use 'assertEqual' to check whether the error message on
        # the 'name' field is 'this field is required.' Remember to include
        # the period at the end of our string as it has to match exactly.
        # NOTE: We're using the zero index also because the form will return
        # a list of errors on each field & this verifies that the first item
        # in that list is our string telling us the field is required.
        # The specific error message give below is what we expect.
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    # This test to ensure that the 'done' field is not required. It shouldn't
    # be required since it has a default value of false on the item model.
    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    # A test to check that the only fields that are displayed in the form are
    # the 'name' and 'done' fields.
    def test_fields_are_explicit_in_form_metaclass(self):
        # We instantiate an empty form.
        form = ItemForm()
        # We then use 'assertEqual' to check whether the 'form.meta.fields'
        # attribute is equal to a list with 'name' and 'done' variables in it.
        # This will ensure that the fields are defined explicitly so our form
        # won't allow any accidental display of information we don't want it
        # to. It will also protect the fields from being reordered since the
        # list must match exactly as stated in this test.
        self.assertEqual(form.Meta.fields, ['name', 'done'])
