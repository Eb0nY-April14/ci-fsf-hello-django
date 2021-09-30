from django import forms
from.models import Item


# we'll create a new class called 'ItemForm' that will
# inherit all the functionality of forms.ModelForm. The 
# idea of creating this form in Django is that rather than 
# writing an entire form ourselves in HTML, we can simply 
# render it out as a template variable.
class ItemForm(forms.ModelForm):
    # to tell the form which model it's going to be associated
    # with, we need to provide an inner class called meta.This
    # inner class just gives our form some information about itself
    # such as which fields it should render, how it should display
    # error messages etc.
    class Meta:
        model = Item
        fields = ['name', 'done']
