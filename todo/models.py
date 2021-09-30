from django.db import models


# Create your models here.
# Here, we inherited from the 'models' class.
# NOTE: If we need functionality from one class
# to be available in another, we need to inherit
# the one you need.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # By default, all models that inherit this base model class will use
    # its built-in string method to display their class name followed by
    # the word object. This is not descriptive enough as we saw in our
    # Django admin panel with the name 'Item object' so to change this,
    # we need to actually override that string method with our own by
    # redefining it here in our own class. This will now return the item
    # class's name attribute which in our case, will be the name that we
    # put into the form.
    # The beauty of class inheritance is that we still get all of the
    # default functionality of the default Django 'model class' but we
    # can override this string method just to change how our items are
    # displayed.

    def __str__(self):
        return self.name
