"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# 'urls.py' contains the routing information that allows users to type a
# specific URL into their address bar & hit a specific Python function.
# This is similar to 'app.route' in flask.

from django.contrib import admin
from django.urls import path
# Any function/view we write in 'views.py' file must be
# imported into the 'urls.py' file so it can be access-
# ible to urls.py & we can be allowed to use it in our
# urls.py file. Since our list of imports is getting
# quite long, instead of importing each view individually,
# we'll remove them all and replace them with views. Then,
# weI can simply add 'views.' in front of all the views.
# from todo.views import get_todo_list, add_item, edit_item
from todo import views
# This built-in path function is responsible for defining the
# url that will trigger the 'say hello' function & return the
# http response to the browser. Typically, it takes 3 arguments
# which are:
# 1) the url that the user will type in i.e hello with a backslash
# 2) the view function that it's going to return i.e our say_hello
# 3) a name parameter called hello which will be explained later
# We'll now add 'views dot' in front of all the views since we've
# replaced all the functions imported above with 'views' to reduce
# the length of import items.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_todo_list, name='get_todo_list'),  # home page path
    path('add', views.add_item, name='add'),   # add item page path
    # The angular bracket syntax used with the item_id below is common
    # in Django URLs & it's the mechanism by which the item ID makes
    # its way from links or forms in our templates through the URL &
    # into the view which expects it as a parameter.
    # The path below takes 3 arguments i.e the 'edit/item_id',
    # 'edit_item' view & a name of 'edit'.
    # edit item page path on next line
    path('edit/<item_id>', views.edit_item, name='edit'),
    # toggle/delete item page path on next line
    path('toggle/<item_id>', views.toggle_item, name='toggle'),
    path('delete/<item_id>', views.delete_item, name='delete')
]
