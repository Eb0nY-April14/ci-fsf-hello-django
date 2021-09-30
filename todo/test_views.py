from django.test import TestCase
from .models import Item


# Create your tests here.
# THIS TEST WILL BE USED TO TEST OUR VIEWS.
# To test the HTTP responses of the views, we can use a built-in HTTP
# client that comes with the Django testing framework.
# We'll create a class called 'TestViews' which inherits the built-in
# TestCase class & thereby giving us access to all its functionality.
class TestViews(TestCase):

    # We want to test that we can get the todo list which is the home page.
    def test_get_todo_list(self):
        # For the get_todo_list view, we'll set a variable named 'response'
        # equal to 'self.client.get' & provide the URL i.e 'slash' since we
        # just want to get the home page.
        response = self.client.get('/')
        # We'll then use 'assertEqual' to confirm that the 'response.status
        # code' is equal to 200 i.e the code for a successful HTTP response.
        self.assertEqual(response.status_code, 200)
        # To confirm the view uses the correct template, we'll use 'self.
        # assertTemplateUsed' & tell it the template we expect it to use
        # in the response.
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    # We want to test that we can get the add_item page.
    def test_get_add_item_page(self):
        # For the get_add_item view, we'll set a variable named 'response'
        # equal to 'self.client.get' & provide the URL i.e 'slash add' since we
        # just want to get the 'add item' page.
        response = self.client.get('/add')
        # We'll then use 'assertEqual' to confirm that the 'response.status
        # code' is equal to 200 i.e the code for a successful HTTP response.
        self.assertEqual(response.status_code, 200)
        # To confirm the view uses the correct template, we'll use 'self.
        # assertTemplateUsed' & tell it the template we expect it to use
        # in the response.
        self.assertTemplateUsed(response, 'todo/add_item.html')

    # We want to test that we can get the edit_item page.
    def test_get_edit_item_page(self):
        # For the get_edit_item view, how we implement it is slightly
        # different in the sense that we'll set a variable named
        # 'response' equal to 'self.client.get' & provide the URL i.e
        # 'slash edit slash a number e.g 99' so we can get the 'edit
        # item' page. If a static number is used, the test will only
        # pass if that item ID exists in our database so we'll comment
        # it out & be more generic. Django allows us to do crud
        # operations in Django tests. We'll import the item model at
        # the top & then create an item to use in this test.
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item.id}')
        # response = self.client.get('/edit/99')
        # We'll then use 'assertEqual' to confirm that the 'response.status
        # code' is equal to 200 i.e the code for a successful HTTP response.
        self.assertEqual(response.status_code, 200)
        # To confirm the view uses the correct template, we'll use 'self.
        # assertTemplateUsed' & tell it the template we expect it to use
        # in the response.
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    # We want to test that we can add item.
    # To test creating an item, we'll set the response equal to
    # 'self.client.post' on the add URL & give it a name 'Test
    # Added Item' as if we've just submitted the item form. If the
    # item is added successfully, the view should redirect back to
    # the home page.
    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    # We want to test that we can delete item.
    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        # If delete is successful, the view should redirect
        # us back to the home page (i.e todo_list.html)
        self.assertRedirects(response, '/')
        # To prove that the item has been deleted, we'll try
        # to get it from the database using '.filter' & passing
        # it the 'item id'. Since that item is the only one on
        # the database and we just deleted it, we can be sure the
        # view works by asserting whether the length of existing
        # items is zero.
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    # We want to test that we can toggle item.
    def test_can_toggle_item(self):
        # We'll create an item with a 'done status' of 'True'.
        item = Item.objects.create(name='Test Todo Item', done=True)
        # We then call the toggle URL on its ID
        response = self.client.get(f'/toggle/{item.id}')
        # If delete is successful, the view should redirect
        # us back to the home page (i.e todo_list.html)
        self.assertRedirects(response, '/')
        # After asserting that the view redirects us to the right page,
        # we'll get the item again giving it the name 'updated_item'
        updated_item = Item.objects.get(id=item.id)
        # We'll then use 'assertFalse' to check its done status.
        self.assertFalse(updated_item.done)

    # We want to test that we can edit an item.
    def test_can_edit_item(self):
        # We'll create an item.
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        # If 'edit item' is successful, the view should redirect
        # us back to the home page (i.e todo_list.html)
        self.assertRedirects(response, '/')
        # After asserting that the view redirects us to the right page,
        # we'll get the item again giving it the name 'updated_item'
        updated_item = Item.objects.get(id=item.id)
        # We'll then use 'assertEqual' to test that the updated item's
        # name is equal to updated name.
        self.assertEqual(updated_item.name, 'Updated Name')
