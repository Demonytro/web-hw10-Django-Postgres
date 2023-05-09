from django.forms import ModelForm, CharField, TextInput, ModelMultipleChoiceField, SelectMultiple, Select, \
    ModelChoiceField
from .models import Quote, Tag, Author


class QuoteForm(ModelForm):
    quote = CharField(required=True, widget=TextInput())  # blank=True,
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by('name'), required=True, widget=SelectMultiple())  # blank=True,
    # author = CharField(required=True, widget=TextInput())
    author = ModelChoiceField(queryset=Author.objects.all().order_by('fullname'), widget=Select())

    # author = ModelMultipleChoiceField(queryset=Author.objects.get('fullname'), required=True, widget=Select())



    class Meta:
        model = Quote
        fields = ("quote", "author", "tags")
        # fields = ["quote"]
        # exclude = ['tags']
        # exclude = ["author", 'tags']


class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, required=True, widget=TextInput())
    born_date = CharField(max_length=50, required=True, widget=TextInput())
    born_location = CharField(max_length=150, required=True, widget=TextInput())
    bio = CharField(required=True, widget=TextInput())


    class Meta:
        model = Author
        fields = ("fullname", "born_date", "born_location", "bio")


class TagForm(ModelForm):
    name = CharField(min_length=2, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ["name"]


