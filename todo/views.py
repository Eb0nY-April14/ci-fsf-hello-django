from django.shortcuts import render, redirect, get_object_or_404
# Since we need access to the item model in this file,
# we'll import it in order for Django to allow us to
# use the item model in our views.
from .models import Item
from .forms import ItemForm


# Create your views here.
# Django allows us to write all our HTML code in an actual
# HTML file e.g 'todo_list.html', pass it to the render
# function in our 'views.py' file, then Django does the
# work of rendering/displaying it to users.
def get_todo_list(request):
    # We'll use the 'render' function imported into this
    # views.py file on line 1 when we created our app to
    # return/display the template we created in 'todo_list.
    # html' file.
    # The render function takes 2 arguments: an HTTP request
    # & a template name & returns an HTTP response.
    # we need to get a query set of all the items in the
    # database using the next line of code below. We'll create
    # a variable named 'items' that will return multiple items.
    items = Item.objects.all()
    # We'll create another variable called 'context' which will
    # be a dictionary that contains all of our items in it.
    context = {
        'items': items
    }
    # We need to add that context as a 3rd argument to the render
    # function to ensure that we have access to it in our
    # 'todo_list.html' template.
    return render(request, 'todo/todo_list.html', context)


# THIS IS THE 'add_item' VIEW
def add_item(request):
    # To handle what happens when the user clicks submit
    # on the form, since we set the form action to our
    # 'add' URL, we need to add an if statement in the add
    # item view to check what type of requests this is. If
    # it is a 'POST' request, it means it came from someone
    # clicking the submit button on our form so we'll get
    # the information from the form that comes in from this
    # template (i.e add_item.html) & use it to create a new
    # item, then we'll redirect them back to the get_todo_list
    # view i.e 'todo_list.html' page/template which serves as
    # the 'Home Page' where they'll see their updated todo list.
    # We'll do this below.
    if request.method == "POST":
        # Instead of creating the item manually, our new form from
        # 'forms.py' will do it.
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        # To get the items name set as a 'name' variable below,
        # we need to look up request.post.get() & supply it with
        # the value we gave the name attribute in our 'add_item
        # form' which was 'item_name'
        # name = request.POST.get('item_name')
        # Since checkbox used for the 'done' has a boolean value,
        # to check if the item is done, we'll just check whether
        # the post data actually has a done property in it.
        # done = 'done' in request.POST
        # We'll now create an item using the code below
        # Item.objects.create(name=name, done=done)
        # This will redirect the user back to the 'get_todo_list' page
            return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form': form
    }
    # We'll use the 'render' function imported into this
    # views.py file on line 1 when we created our app to
    # return/display the template we created in 'todo_list.
    # html' file.
    # The render function takes 2 arguments: an HTTP request
    # & a template name & returns the 'add_item.html' view.
    # If the user makes a 'GET' request, we'll just return the
    # add_item HTML template by rendering it to them.
    return render(request, 'todo/add_item.html', context)


# THIS IS THE 'edit_item' VIEW
# The code in this function is similar to the one in add_item
# function
def edit_item(request, item_id):
    # We first get a copy of the 'item' from the database
    # using the get_object which we'll use to say we want
    # to get an instance of the item model with an ID equal
    # to the item ID that was passed into the view via the URL.
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        # We'll also give our form the specific 'item' instance
        # we want to update along with the 'request.POST'.
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    # Here below, we'll create an instance of our item form and
    # return it to the template in the context. Then, to pre-
    # populate the form with the item's current details, we'll
    # pass an instance argument to the form with the value of 'item'
    # which tells the form that it should be prefilled with the
    # information for the item we just got from the database.
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


# What this function does is toggle the item status & then redirect
# back to the to-do list. This view/function will be called toggle_item
# so it matches what we put in the toggle path in urls.py. It'll take in
# the request as well as the item ID the user wants to toggle.
# when a user clicks toggle, our 'view' will get the item & if its 'done'
# status is currently true, it will flip it to false and vice versa.
def toggle_item(request, item_id):
    # The code on next line will get the item in question.
    item = get_object_or_404(Item, id=item_id)
    # The code on next line will change its 'done' status to the opposite
    # by using 'not' which will just flip it to the opposite of whatever
    # it currently is.
    item.done = not item.done
    item.save()
    # The next line of code will simply redirect the user back to the
    # 'get_todo_list' view (i.e the todo_list.html template) which is
    # the home page.
    return redirect('get_todo_list')


def delete_item(request, item_id):
    # The code on next line will get the item in question.
    item = get_object_or_404(Item, id=item_id)
    # The code on next line will delete the item
    item.delete()
    # The next line of code will simply redirect the user back to the
    # 'get_todo_list' view (i.e the todo_list.html template) which is
    # the home page.
    return redirect('get_todo_list')
